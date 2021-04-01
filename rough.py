import tkinter as tk
from subprocess import Popen, PIPE
import threading


def threaded(fn=None, **kw):
    """To use as decorator to make a function call threaded.
    takes function as argument. To join=True pass @threaded(True)."""

    def wrapper(*args, **kwargs):
        kw['return'] = kw['function'](*args, **kwargs)

    def _threaded(fn):
        kw['function'] = fn

        def thread_func(*args, **kwargs):
            thread = threading.Thread(
                target=wrapper, args=args,
                kwargs=kwargs, daemon=kw.get('daemon', True))
            thread.start()
            if kw.get('join'):
                thread.join()
            return kw.get('return', thread)
        return thread_func

    if fn and callable(fn):
        return _threaded(fn)
    return _threaded


class TextIndex(str):
    def __init__(self, index):
        self._index = index
        self._row, self._col = self._index.split('.')

    @property
    def row(self):
        return int(self._row)

    @property
    def column(self):
        return int(self._col)

    def __str__(self):
        return self._index

    def __repr__(self):
        return "<(%s) rol: %s column: %s>" % (
            self.__class__.__name__, self.row, self.column)


class Terminal(tk.Text):
    def __init__(self, *ags, **kw):
        super().__init__(*ags, **kw)
        self._basename = "Saad$ "
        self._limit_backspace = 0

        self.bind_class(self, "<Return>", self._return_event, True)
        self.bind_class(self, "<Return>", self._run, True)
        # self.bind_class(self, "<Command-x>", lambda _: "break")
        self.bind_class(self, '<BackSpace>', self._backspace_event)
        self.event_delete("<<Cut>>", "<Command-x>")
        self.tag_config('error', foreground='red')
        self.tag_config('output', foreground='grey')
        self.tag_config('command')  # edit later

        self.insert(1.0, self._basename)

    def index(self, index):
        return TextIndex(super().index(index))
    

    def _get_commands(self):
        ln = 1
        index_col = 0
        base_index = (str(self.index(f'end-{ln}l').row) + 
                  str('.') + str(len(self._basename)))
        if self.get(f'end-{ln}l', base_index) == self._basename:
            index_col = len(self._basename)
        print(index_col)

        initial_index = lambda ln: str(
            max(self.index(f'end-{ln}l').row - ln, 1)
            ) + '.%s'% index_col
        cmd = self.get(initial_index(ln), 'end-1c')
        print(cmd, initial_index(ln))
        while cmd[:2] == '> ':
            ln += 1
            cmd = self.get(initial_index(ln), 'end-1c')
        if ln > 1:
            cmd = cmd.replace("> ", "")
        self.tag_add('command', initial_index(ln), 'end-1c')
        if cmd and cmd[-1] == '\\':
            return None
        return cmd

    # @threaded
    # Add threading with more improved and stable method.
    # Current method is single threaded.
    def _run(self, evt):
        cmd = self._get_commands()
        if cmd is None:
            return
        print(cmd)
        # self.insert('end', '\n')
        
        with Popen(cmd, stdout=PIPE, stderr=PIPE, 
                   bufsize=1, universal_newlines=True, 
                   shell=True) as p:
            
            for line in p.stdout:
                # print(line, end='')
                before_index = self.index("end-1c")
                self['state'] = "normal"
                self.insert('end', line)
                self.tag_add('output', before_index, self.index("insert"))
                self.update()
                self['state'] = "disabled"
            
            for eline in p.stderr:
                # print(eline, end='')
                before_index = self.index("end-1c")
                self['state'] = "normal"
                self.insert('end', eline)
                self.tag_add('error', before_index, self.index("insert"))
                self.update()
                self['state'] = "disabled"
        self['state'] = "normal"

    def _return_event(self, _):
        if (self._backspace_event(None)
                and self.index('insert') != self.index('end-1c')):
            return "break"
        if (self.get('end-2c') == '\\'
                or self.get('end-1l', 'end-1c') == '> '):
            self.after(1, lambda: self.insert('end', '> '))
            self._limit_backspace = 2
        else:
            # self.after(1, lambda: self.insert('end', self._basename))
            self._limit_backspace = 0 #len(self._basename) + 1

    def _backspace_event(self, _):
        insert_idx = self.index('insert')
        lastline_idx = self.index('end-1c')
        if (insert_idx.column <= self._limit_backspace
                or insert_idx != lastline_idx):
            return "break"


def main():
    root = tk.Tk()
    terminal = Terminal(padx=5, pady=5)
    terminal.pack()
    root.mainloop()


main()
