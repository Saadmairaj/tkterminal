#                    Copyright 2021 Saad Mairaj

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


from tkterminal.utils import threaded
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
        if (self.get('end-2c') == '\\'
                or self.get('end-1l', 'end-1c') == '> '
                or self.index('end-1l').row != self.index('insert').row):
            return "break"
        if insert_newline:
            self.insert('end', '\n')
        self.insert('end', self._basename)
        self.tag_add('basename', 'end-1l', 'end-1c')
        self.see('end')
        self._limit_backspace = len(self._basename)
        self.linebar.trigger_change_event()

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
            return None, None
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
        if (self.get('end-2c') == '\\'
                or self.get('end-1l', 'end-1c') == '> '):
            index = "end-1c" if self.get('end-2c') == '\\' else "end"
            self.insert(index, '\n')
            self.insert('end', '> ')
            self._limit_backspace = 2
            return False
        if not self._get_commands()[0]:
            self._limit_backspace = len(self._basename)
            return True

    def _ignore_keypress(self, evt=None):
        """Internal function"""
        insert_idx = self.index('insert')
        if (insert_idx.column < self._limit_backspace):
            return "break"

    def _on_return(self, evt=None):
        """Internal function.

        Event callback on return key press."""
        self._set_initials()
        self._run_on_return(evt)
        return 'break'

    def _on_keypress(self, evt=None):
        """Internal function.

        Event callback on any keybroad key press."""
        last_line = self.get('end-1l', 'end-1c')
        if ((self._ignore_keypress(evt)
                and len(last_line) >= 2 and last_line[:2] == '> ')
                or (evt.keysym not in ALLOWED_KEYSYM
                and self.index('insert').row != self.index('end-1l').row)
                # or (evt.state == 8 and evt.keysym == 'v'
                #     and insert_idx.row != self.index('end-1l').row)
                ):
            return "break"

    def _on_backspace(self, evt=None):
        """Internal function.

        Event callback on backspace key press."""
        insert_idx = self.index('insert')
        if (insert_idx.column <= self._limit_backspace
                or insert_idx.row != self.index('end-1c').row):
            return "break"

    def _on_cut(self, evt=None):
        """Internal function.

        Event "cut" callback."""
        return self._ignore_keypress(evt)

    def _on_paste(self, evt=None):
        """Internal function.

        Event "paste" callback."""
        return self._ignore_keypress(evt)


class Terminal(Text, _TerminalFunctionality):
    """Ternimal widget."""

    def __init__(self, *ags, **kw):
        """Construct a ternimal widget with the parent MASTER.

        STANDARD OPTIONS

            background, borderwidth, cursor,
            exportselection, font, foreground,
            highlightbackground, highlightcolor,
            highlightthickness, insertbackground,
            insertborderwidth, insertofftime,
            insertontime, insertwidth, padx, pady,
            relief, selectbackground,
            selectborderwidth, selectforeground,
            setgrid, takefocus,
            xscrollcommand, yscrollcommand,

        WIDGET-SPECIFIC OPTIONS

            autoseparators, height, maxundo,
            spacing1, spacing2, spacing3,
            state, tabs, undo, width, wrap,

        """
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

        self.tag_config('basename', foreground='pink')
        self.tag_config('error', foreground='red')
        self.tag_config('output', foreground='darkgrey')

        self._set_basename()

    @property
    def basename(self):
        """Returns the basename."""
        return self.basename

    @basename.setter
    def basename(self, val):
        """Change the basename of the terminal."""
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

    def clear(self):
        """Clear the console."""
        self.delete('1.0', 'end')
        self._set_basename()

    def get_output(self):
        """Get output from the recent command. 

        Returns None if no command has run else 
        the function will return a dictionary 
        of error and output."""
        if self._out or self._err:
            return {
                "error": self._err,
                "output": self._out}

    def run_command(self, cmd, give_input=None):
        """Run the command into the terminal."""
        self._run_on_return(_cmd=cmd, _input=give_input)
