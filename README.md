# tkterminal

[![PyPI](https://img.shields.io/pypi/v/tkterminal)](https://pypi.org/project/tkterminal)
[![CodeFactor](https://www.codefactor.io/repository/github/saadmairaj/tkterminal/badge)](https://www.codefactor.io/repository/github/saadmairaj/tkterminal)
[![Downloads](https://pepy.tech/badge/tkterminal)](https://pepy.tech/project/tkterminal)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSaadmairaj%2Ftkterminal.svg?type=small)](https://app.fossa.com/projects/git%2Bgithub.com%2FSaadmairaj%2Ftkterminal?ref=badge_small)
![Platform](https://img.shields.io/powershellgallery/p/Pester?color=blue)

This library gives Terminal widget support to the Tkinter library. Perform almost all the operations of a terminal with tkterminal.

<p align="center">
  <img width="600" alt="demo_dark" src="https://user-images.githubusercontent.com/46227224/113672526-8811cb00-96d5-11eb-8527-5f8c559482fc.png">
  <img width="600" alt="demo_light" src="https://user-images.githubusercontent.com/46227224/113672749-bf807780-96d5-11eb-801e-c60edcc72672.png">
</p>

## Installation

Use the package manager pip to install with the following command:

```bash
pip install tkterminal
```

If you would like to get the latest master or branch from GitHub, you could also:

```bash
pip install git+https://github.com/Saadmairaj/tkterminal
```

Or even select a specific revision _(branch/tag/commit)_:

```bash
pip install git+https://github.com/Saadmairaj/tkterminal@master
```

## Usage

Terminal widget is easy to use. Type the commands just like you type in the terminal.

```python
import tkinter as tk
from tkterminal import Terminal

root = tk.Tk()
terminal = Terminal(pady=5, padx=5)
terminal.pack(expand=True, fill='both')
root.mainloop()
```

  <p align="center">
    <img src="https://user-images.githubusercontent.com/46227224/113672865-e2129080-96d5-11eb-8152-f043f0ed2fa8.gif"/>
  </p>

- Enable shell (**`shell=True`**)

  If the shell is True, the specified command will be executed through the shell. This can be useful if you are using Python primarily for the enhanced control flow it offers over most system shells and still want convenient access to other shell features such as shell _pipes_, _filename wildcards_, _environment variable expansion_, and _expansion of ~ to a user’s home directory_. However, note that Python itself offers implementations of many shell-like features (in particular, `glob`, `fnmatch`, `os.walk()`, `os.path.expandvars()`, `os.path.expanduser()`, and `shutil`).

  To have shell enabled terminal then set the shell to true like so

  ```python
  terminal = Terminal()
  terminal.shell = True
  ```

- Enable line number bar for the terminal (**`linebar=True`**)

  If linebar is True, the terminal will have a line number bar on the left side which tells the number of the line by numbering each line of the terminal. Clicking on any number will select the specific line in the terminal. The line with the insert will be highlighted in the number bar.

  To have line number bar enabled terminal then set linebar to true like so.

  ```python
  terminal = Terminal()
  terminal.linebar = True
  ```

  <p align="center">
    <img width="700" alt="linebar" src="https://user-images.githubusercontent.com/46227224/113672881-e474ea80-96d5-11eb-933a-56a0a0af9948.png">
  </p>

- Command that requires input.

  The tkterminal is using subprocess python module where the input can only be passed before running the command and cannot be passed after the command has ran. So the input can be pass with methods:

  - Through _`run_command(cmd, give_input=None)`_ method.

    Input can be passed directly to the parameter `give_input` of run_command method along with the actual command.

    Example:

    ```python
    import tkinter as tk
    from tkterminal import Terminal

    root = tk.Tk()
    terminal = Terminal(pady=5, padx=5)
    terminal.shell = True
    terminal.linebar = True
    terminal.pack(expand=True, fill='both')
    b1 = tk.Button(
        root, text="Uninstall tkterminal", fg="Black",
        command=lambda: terminal.run_command('pip uninstall tkterminal', 'y'))
    b1.pack()
    root.mainloop()
    ```

  - Directly typing into the Terminal window.

    We can directly pass input into the terminal after typing the command between these HTML tags `<input> ... </input>` these tags are just to read user input from the command.

    Example:

    ```bash
    pip uninstall tkterminal <input>y</input>
    ```

## Documentation

Terminal widget is created from the Tkinter Text widget class that makes it support all the options of a Text widget.

- Configurable options for a Terminal widget. Syntax: `Terminal(root, options=value, ...)`

  | Options               | Description                                                                                                                                                                                                                                   |
  | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _background_          | The default background color of the terminal widget.                                                                                                                                                                                          |
  | _borderwidth_         | The width of the border around the terminal widget. Default is 2 pixels.                                                                                                                                                                      |
  | _cursor_              | The cursor that will appear when the mouse is over the terminal widget.                                                                                                                                                                       |
  | _exportselection_     | Normally, text selected within a terminal widget is exported to be the selection in the window manager. Set `exportselection=0` if you don't want that behavior.                                                                              |
  | _font_                | The default font for text inserted into the widget.                                                                                                                                                                                           |
  | _foreground_          | The color used for text within the widget. You can change the color for tagged regions; this option is just the default.                                                                                                                      |
  | _height_              | The height of the widget in lines (not pixels!), measured according to the current font size.                                                                                                                                                 |
  | _highlightbackground_ | The color of the focus highlight when the terminal widget does not have focus.                                                                                                                                                                |
  | _highlightcolor_      | The color of the focus highlight when the terminal widget has the focus.                                                                                                                                                                      |
  | _highlightthickness_  | The thickness of the focus highlight. Default is 0.                                                                                                                                                                                           |
  | _insertbackground_    | The color of the insertion cursor. Default is black.                                                                                                                                                                                          |
  | _insertborderwidth_   | Size of the 3-D border around the insertion cursor. Default is 0.                                                                                                                                                                             |
  | _insertofftime_       | The number of milliseconds the insertion cursor is off during its blink cycle. Set this option to zero to suppress blinking. Default is 300.                                                                                                  |
  | _insertontime_        | The number of milliseconds the insertion cursor is on during its blink cycle. Default is 600.                                                                                                                                                 |
  | _insertwidth_         | Width of the insertion cursor (its height is determined by the tallest item in its line). Default is 2 pixels.                                                                                                                                |
  | _padx_                | The size of the internal padding added to the left and right of the text area. Default is one pixel.                                                                                                                                          |
  | _pady_                | The size of the internal padding added above and below the text area. Default is one pixel.                                                                                                                                                   |
  | _relief_              | The 3-D appearance of the terminal widget. Default is `relief=SUNKEN`.                                                                                                                                                                        |
  | _selectbackground_    | The background color to use displaying selected text.                                                                                                                                                                                         |
  | _selectborderwidth_   | The width of the border to use around selected text.                                                                                                                                                                                          |
  | _spacing1_            | This option specifies how much extra vertical space to add between displayed lines of text when a logical line wraps. Default is 0.                                                                                                           |
  | _spacing2_            | This option specifies how much extra vertical space to add between displayed lines of text when a logical line wraps. Default is 0.                                                                                                           |
  | _spacing3_            | This option specifies how much extra vertical space is added below each line of text. If a line wraps, this space is added only after the last line it occupies on the display. Default is 0.                                                 |
  | _state_               | Normally, terminal widgets respond to keyboard and mouse events; set state=NORMAL to get this behavior. If you set state=DISABLED, the terminal widget will not respond, and you won't be able to pass commands into the terminal.            |
  | _tabs_                | This option controls how tab characters position text.                                                                                                                                                                                        |
  | _width_               | The width of the widget in characters (not pixels!), measured according to the current font size.                                                                                                                                             |
  | _wrap_                | This option controls the display of lines that are too wide. Set wrap=WORD and it will break the line after the last word that will fit. With the default behavior, `wrap=CHAR`, any line that gets too long will be broken at any character. |
  | _xscrollcommand_      | To make the terminal widget horizontally scrollable, set this option to the `set()` method of the horizontal scrollbar.                                                                                                                       |
  | _yscrollcommand_      | To make the terminal widget vertically scrollable, set this option to the `set()` method of the vertical scrollbar.                                                                                                                           |

- Methods on `Terminal` widget objects:

  | Methods                                 | Description                                                                                                                                                                                                                                                                                                         |
  | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _.clear()_                              | Clears the console completely.                                                                                                                                                                                                                                                                                      |
  | _.get_output()_                         | Get the output of the recently run command. Returns None if no command has run else the function will return a dictionary of error and output.                                                                                                                                                                      |
  | _.run_command(cmd, give_input=None)_    | Run the command into the terminal.                                                                                                                                                                                                                                                                                  |
  | _.tag_config(tagname, option=value...)_ | You can use this method to configure the tag properties, which include:- <br>- _background_<br>- _foreground_<br>- _font_<br>- _justify_ (center, left, or right), <br>- _tabs_ (this property has the same functionality of the Text widget tabs's property)<br>- _underline_ (used to underline the tagged text). |

- Properties on `Terminal` widget objects:

  | Properties          | Description                                                                                                                                                                                                                                  |
  | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _terminal.basename_ | Change the basename of the terminal. Default is **tkterminal$**                                                                                                                                                                              |
  | _terminal.linebar_  | Line number bar tells the number of the line by numbering each line of the terminal. Clicking on any number will select the specific line in the terminal. The line with the insert will be highlighted in the number bar. Default is False. |

- Configure output, error, basename and linebar:

  - All output text have tag name _output_ which can be configured with `terminal.tag_config("output", option=value...)` method.
  - All error text also have a tag name _error_ which can be configured with `terminal.tag_config("error", option=value...)` method.
  - The basename also have a tag name _basename_ configured with `terminal.tag_config("basename", option=value...)` method.
  - The linebar is an object of Tkinter Canvas widget which can be configured with `terminal.linebar.configure(option=value ...)`. And each number line is a canvas item whose tag name is the number itself that can be configured with `terminal.linebar.itemconfigure('item', options...)`.
