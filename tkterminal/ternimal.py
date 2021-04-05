from tkterminal.utils import _bind, threaded
from tkterminal.text import Text, TextIndex
from subprocess import PIPE, Popen
import tempfile


ALLOWED_KEYSYM = ('Left', 'Right', 'Up', 'Down')
ALLOWED_STATE = ('Shift', 'Lock', 'Control', 'Mod1',
                 'Mod2', 'Mod3', 'Mod4', 'Mod5')
MS_DELAY = 1


class _TerminalFunctionality:
    """Internal class for Terminal widget."""

    def _set_basename(self, insert_newline=False):
        """Internal function"""
        if self.index('end-1l').row != self.index('insert').row:
            return "break"
        if insert_newline:
            self.insert('end', '\n')
        self.insert('end', self._basename)
        self.tag_add('basename', 'end-1l', 'end-1c')
        self.see('end')
        self.event_generate("<<Change>>", when="tail")

    def _create_propreties(self):
        """Internal function"""
        options = self.config()
        for op in options:
            print(op)
            pr = property(lambda op=op: op)
            pr.setter(lambda val, op=op: self.config({op: val}))

    def _get_commands(self):
        """Internal function"""

        def initial_index(ln):
            """Internal function."""
            index_col = 0
            base_index = (
                str(self.index(f'end-{ln}l').row) +
                str('.') + str(len(self._basename)))
            if self._basename and self.get(f'end-{ln}l', base_index) == self._basename:
                index_col = len(self._basename)
            return str(max((self.index(f'end-{ln}l').row), 1)) + '.%s' % index_col

        ln = 1
        _input = None
        cmd = self.get(initial_index(ln), 'end-1c')
        add_more = self.get('end-1l', 'end-1c') == '> '
        while cmd[:2] == '> ':
            ln += 1
            cmd = self.get(initial_index(ln), 'end-1c')
        if cmd.find("<input>"):
            _input = cmd.split('<input>')[-1].split('</input>')[0]
            cmd = cmd.replace(f"<input>{_input}</input>", "")
        cmd = cmd.replace("> ", "") if ln > 1 else cmd
        if cmd and cmd[-1] == '\\' or add_more:
            return
        return cmd, _input

    def _update_output_line(self, tag, line, update=False):
        """Internal function"""
        before_index = self.index("end-1c")
        self['state'] = "normal"
        self.insert('end', line)
        self.tag_add(tag, before_index, self.index("insert"))
        if update:
            self.update()
        self['state'] = "disabled"
        self.see('end')

    # UPDATE: threading is working,
        # Need more stable method.
    @threaded
    def _run_on_return(self, evt=None, _cmd=None, _input=None):
        """Internal function"""
        cmd, _inp = self._get_commands()
        if _input is None and _inp:
            _input = _inp
        print(_input)
        if _cmd is not None:
            self.insert("end-1c", _cmd)
            cmd = _cmd
        if cmd is None or cmd == '':
            return self._set_basename(True)

        stdin = PIPE
        _original_state = self['state']
        self._out, self._err = '', ''
        self.insert('end', '\n')
        self['state'] = 'disable'

        if _input:
            stdin = tempfile.TemporaryFile()
            stdin.write(_input.encode())
            stdin.seek(0)
        with Popen(cmd, stdout=PIPE, stderr=PIPE, stdin=stdin,
                   bufsize=1, universal_newlines=True,
                   shell=self.shell) as p:
            for line in p.stdout:
                self._out += line
                self._update_output_line('output', line, True)
            for line in p.stderr:
                self._err += line
                self._update_output_line('error', line, True)
        self['state'] = _original_state
        if _input:
            stdin.close()
        self._set_basename(True)

    def _set_initials(self, evt=None):
        """Internal function"""
        if (self._ignore_keypress(None)
                and self.index('insert') != self.index('end-1c')):
            return "break"
        if (self.get('end-2c') == '\\'
                or self.get('end-1l', 'end-1c') == '> '):
            self._limit_backspace = 2
            self.after(MS_DELAY, lambda: self.insert('end', '> '))
            return True
        if not self._get_commands()[0]:
            self._limit_backspace = len(self._basename)
            return True

    def _ignore_keypress(self, evt=None):
        """Internal function"""
        insert_idx = self.index('insert')
        if (insert_idx.column <= self._limit_backspace
                or insert_idx != self.index('end-1c')):
            return "break"

    def _on_return(self, evt=None):
        """Internal function.

        Event callback on return key press."""
        self._set_initials(evt)
        self._run_on_return(evt)
        return 'break'

    def _on_keypress(self, evt=None):
        """Internal function.

        Event callback on any keybroad key press."""
        insert_idx = self.index('insert')
        if (insert_idx.column < self._limit_backspace
            or (evt.keysym not in ALLOWED_KEYSYM
                and insert_idx.row != self.index('end-1l').row)
                or (evt.state == 8 and evt.keysym == 'v'
                    and insert_idx.row != self.index('end-1l').row)):
            return "break"

    def _on_backspace(self, evt=None):
        """Internal function.

        Event callback on backspace key press."""
        return self._ignore_keypress(evt)

    def _on_cut(self, evt=None):
        """Internal function.

        Event "cut" callback."""
        return self._ignore_keypress(evt)

    def _on_paste(self, evt=None):
        """Internal function.

        Event "paste" callback."""
        return self._ignore_keypress(evt)


class Terminal(Text, _TerminalFunctionality):
    def __init__(self, *ags, **kw):
        kw['highlightthickness'] = kw.get('highlightthickness', 0)
        super().__init__(*ags, **kw)
        self.shell = False
        self._basename = "tkterminal$ "
        self._limit_backspace = 0
        self._limit_backspace = len(self._basename)

        self.bind("<<Cut>>", self._on_cut, True)
        self.bind("<<Paste>>", self._on_paste, True)

        self.bind("<Return>", self._on_return, True)
        self.bind("<KeyPress>", self._on_keypress, True)
        self.bind('<BackSpace>', self._on_backspace, True)

        # (issue) _bind not working.
        # _bind(self,
        #     dict(className="on_keypress", sequence="<KeyPress>", func=self._on_keypress),
        #     dict(className="on_return", sequence="<Return>", func=self._on_return),
        #     dict(className="on_backspace", sequence="<BackSpace>", func=self._on_backspace),
        #     # dict(className="Cut", sequence="<<Cut>>", func=self._on_cut),
        #     )

        self.tag_config('basename', foreground='pink')
        self.tag_config('error', foreground='red')
        self.tag_config('output', foreground='darkgrey')
        self.tag_config('command')  # edit later

        self.insert(1.0, self._basename)
        self.tag_add('basename', 1.0, 'end-1c')

    @property
    def basename(self):
        return self.basename

    @basename.setter
    def basename(self, val):
        if not val.endswith(' '):
            val += ' '
        for i in self.tag_ranges('basename'):
            start_index = TextIndex(i)
            end_index = TextIndex(
                str(start_index.line) + str('.') +
                str(start_index.char+len(self._basename)))
            text = self.get(start_index, end_index)
            if text == self._basename:
                self.delete(start_index, end_index)
                self.insert(start_index, val)
                self.tag_add('basename', start_index, end_index)
        self._basename = val

    @property
    def get_output(self):
        if self._out or self._err:
            return {
                "error": self._err,
                "output": self._out}

    def run_command(self, cmd, give_input=None):
        """Run the command into the terminal."""
        self._run_on_return(_cmd=cmd, _input=give_input)
