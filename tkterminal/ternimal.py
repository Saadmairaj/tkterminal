
# ADD::
    # <input: ""> give input like that
    # Implement threading

    
# FIX::
    # stop key presses above the end line.
    
    # bug Saad$ \
        # > 
        # /bin/sh: line 1: Saad$: command not found
        # Saad$ 
    
    # try cursor not going up neither by mouse.





import tempfile
from subprocess import PIPE, Popen
from tkterminal.text import Text


class _TerminalFunctionality:

    def _set_basename(self,):
        self.insert('end', self._basename)
        self.tag_add('basename', 'end-1l', 'end-1c')

    def _create_propreties(self):
        options = self.config()
        for op in options:
            print(op)
            pr = property(lambda op=op: op)
            pr.setter(lambda val, op=op: self.config({op: val}))

    def command_decorator(self, fn, cmd):
        pass

    def run_command(self, cmd, give_input=None):
        return self._run(None, _cmd=cmd, _input=give_input)

    # def _get_commands(self):
    #     ln = 1
    #     cmd = self.get(f'end-{ln}l', 'end-1c')
    #     while cmd[:2] == '> ':
    #         ln += 1
    #         cmd = self.get(f'end-{ln}l', 'end-1c')
    #     if ln > 1:
    #         cmd = cmd.replace("> ", "")
    #     self.tag_add('command', f'end-{ln}l', 'end-1c')
    #     if not cmd or cmd[-1] == '\\':
    #         return None
    #     return cmd

    def _get_commands(self):
        ln = 1
        index_col = 0
        base_index = (
            str(self.index(f'end-{ln}l').row) + 
            str('.') + str(len(self._basename)))

        print("Line :", ln, base_index, self.get(f'end-{ln}l', base_index))
        if self._basename and self.get(f'end-{ln}l', base_index) == self._basename:
            index_col = len(self._basename)
    
        initial_index = lambda ln: str(max((self.index(f'end-{ln}l').row), 1)) + '.%s'% index_col
        print(initial_index(ln), self.index('end-1c'))
        cmd = self.get(initial_index(ln), 'end-1c')

        while cmd[:2] == '> ':
            ln += 1
            cmd = self.get(initial_index(ln), 'end-1c')
            print('while loop: ', initial_index(ln), cmd)

        if ln > 1:
            cmd = cmd.replace("> ", "")
        self.tag_add('command', initial_index(ln), 'end-1c')
        if cmd and cmd[-1] == '\\':
            return None
        return cmd

    def _update_output_line(self, tag, line, update=False):
        before_index = self.index("end-1c")
        self['state'] = "normal"
        self.insert('end', line)
        self.tag_add(tag, before_index, self.index("insert"))
        if update:
            self.update()
        self['state'] = "disabled"

    # @threaded
    # Add threading with more improved and stable method.
    # Current method is single threaded.
    def _run(self, evt, _cmd=None, _input=None):
        cmd = self._get_commands()
        if _cmd is not None:
            self.insert("end-1c", _cmd)
            cmd = _cmd
        print('cmd: ', cmd)
        if cmd is None or cmd == '': 
            return  

        out, err = '', ''
        self.insert('end', '\n')
        self['state'] = 'disable'
        stdin = PIPE
        if _input:
            stdin = tempfile.TemporaryFile()
            stdin.write(_input.encode())
            stdin.seek(0)
        with Popen(cmd, stdout=PIPE, stderr=PIPE, stdin=stdin,
                   bufsize=1, universal_newlines=True,
                   shell=self.shell) as p:
            for line in p.stdout:
                out += line
                self._update_output_line('output', line, True)
            for line in p.stderr:
                err += line
                self._update_output_line('error', line, True)
        self['state'] = "normal"
        if _input:
            stdin.close()
        self.after(1, self._set_basename)
        return out, err

    def _return_event(self, _):
        if (self._backspace_event(None)
                and self.index('insert') != self.index('end-1c')):
            return "break"
        if (self.get('end-2c') == '\\'
                or self.get('end-1l', 'end-1c') == '> '):
            self.after(0, lambda: self.insert('end', '> '))
            self._limit_backspace = 2
        else:
            if not self._get_commands():
                self.after(1, self._set_basename)
                self._limit_backspace = len(self._basename)

    def _backspace_event(self, _):
        insert_idx = self.index('insert')
        lastline_idx = self.index('end-1c')
        if (insert_idx.column <= self._limit_backspace
                or insert_idx != lastline_idx):
            return "break"


class Terminal(Text, _TerminalFunctionality):
    def __init__(self, *ags, **kw):
        kw['highlightthickness'] = 0
        super().__init__(*ags, **kw)
        self.shell = False
        self._basename = "Saad$ "
        self._limit_backspace = 0

        # self.bind("<<Change>>", lambda _: self.mark_set("insert", "end"), True)
        self.bind("<Return>", self._return_event, True)
        self.bind("<Return>", self._run, True)
        # self.bind_class(self, "<Command-x>", lambda _: "break")
        self.bind('<BackSpace>', self._backspace_event)
        self.event_delete("<<Cut>>", "<Command-x>")

        self.tag_config('basename', foreground='green')
        self.tag_config('error', foreground='red')
        self.tag_config('output', foreground='darkgrey')
        self.tag_config('command')  # edit later

        self.insert(1.0, self._basename)
        self.tag_add('basename', 1.0, 'end-1c')
        self._limit_backspace = len(self._basename)

        # self._create_propreties()




