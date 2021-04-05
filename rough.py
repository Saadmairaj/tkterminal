
import tkinter as tk
from tkterminal.ternimal import Terminal


def main():
    root = tk.Tk()
    terminal = Terminal(padx=5, pady=5)
    terminal.shell = True
    terminal.linebar = True
    # linebar = LineNumberBar(root, padx=5, width=50)
    # linebar.text = terminal
    # linebar.pack(side="left", expand=True, fill='y')
    terminal.pack(side="left")

    tk.Button(root, text='Run', command=lambda: print(terminal.run_command("pip uninstall tkmacosx", 'y'))).pack()

    root.mainloop()


main()

