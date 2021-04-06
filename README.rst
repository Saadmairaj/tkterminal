tkterminal
==========

This library gives Terminal widget support to the Tkinter library.
Perform almost all the operations of a terminal with tkterminal.

.. raw:: html

   <p align="center">

.. raw:: html

   </p>

Installation
------------

Use the package manager pip to install with the following command:

.. code:: bash

   pip install tkterminal

If you would like to get the latest master or branch from GitHub, you
could also:

.. code:: bash

   pip install git+https://github.com/Saadmairaj/tkterminal

Or even select a specific revision *(branch/tag/commit)*:

.. code:: bash

   pip install git+https://github.com/Saadmairaj/tkterminal@master

Usage
-----

Terminal widget is easy to use. Type the commands just like you type in
the terminal.

.. code:: python

   import tkinter as tk
   from tkterminal import Terminal

   root = tk.Tk()
   terminal = Terminal(pady=5, padx=5)
   terminal.pack(expand=True, fill='both')
   root.mainloop()

.. raw:: html

   <p align="center">

.. raw:: html

   </p>

-  Enable shell (**``shell=True``**)

   If the shell is True, the specified command will be executed through
   the shell. This can be useful if you are using Python primarily for
   the enhanced control flow it offers over most system shells and still
   want convenient access to other shell features such as shell *pipes*,
   *filename wildcards*, *environment variable expansion*, and
   *expansion of ~ to a user’s home directory*. However, note that
   Python itself offers implementations of many shell-like features (in
   particular, ``glob``, ``fnmatch``, ``os.walk()``,
   ``os.path.expandvars()``, ``os.path.expanduser()``, and ``shutil``).

   To have shell enabled terminal then set the shell to true like so

   .. code:: python

      terminal = Terminal()
      terminal.shell = True

-  Enable line number bar for the terminal (**``linebar=True``**)

   If linebar is True, the terminal will have a line number bar on the
   left side which tells the number of the line by numbering each line
   of the terminal. Clicking on any number will select the specific line
   in the terminal. The line with the insert will be highlighted in the
   number bar.

   To have line number bar enabled terminal then set linebar to true
   like so.

   .. code:: python

      terminal = Terminal()
      terminal.linebar = True

   .. raw:: html

      <p align="center">

   .. raw:: html

      </p>

-  Command that requires input.

   The tkterminal is using subprocess python module where the input can
   only be passed before running the command and cannot be passed after
   the command has ran. So the input can be pass with methods:

   -  Through *``run_command(cmd, give_input=None)``* method.

      Input can be passed directly to the parameter ``give_input`` of
      run_command method along with the actual command.

      Example:

      .. code:: python

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

   -  Directly typing into the Terminal window.

      We can directly pass input into the terminal after typing the
      command between these HTML tags ``<input> ... </input>`` these
      tags are just to read user input from the command.

      Example:

      .. code:: bash

         pip uninstall tkterminal <input>y</input>

Documentation
-------------

Terminal widget is created from the Tkinter Text widget class that makes
it support all the options of a Text widget.

-  Configurable options for a Terminal widget. Syntax:
   ``Terminal(root, options=value, ...)``

   +----+-----------------------------------------------------------------+
   | O  | Description                                                     |
   | pt |                                                                 |
   | io |                                                                 |
   | ns |                                                                 |
   +====+=================================================================+
   | *b | The default background color of the terminal widget.            |
   | ac |                                                                 |
   | kg |                                                                 |
   | ro |                                                                 |
   | un |                                                                 |
   | d* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *  | The width of the border around the terminal widget. Default is  |
   | bo | 2 pixels.                                                       |
   | rd |                                                                 |
   | er |                                                                 |
   | wi |                                                                 |
   | dt |                                                                 |
   | h* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *c | The cursor that will appear when the mouse is over the terminal |
   | ur | widget.                                                         |
   | so |                                                                 |
   | r* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *  | Normally, text selected within a terminal widget is exported to |
   | ex | be the selection in the window manager. Set                     |
   | po | ``exportselection=0`` if you don’t want that behavior.          |
   | rt |                                                                 |
   | se |                                                                 |
   | le |                                                                 |
   | ct |                                                                 |
   | io |                                                                 |
   | n* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *f | The default font for text inserted into the widget.             |
   | on |                                                                 |
   | t* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *f | The color used for text within the widget. You can change the   |
   | or | color for tagged regions; this option is just the default.      |
   | eg |                                                                 |
   | ro |                                                                 |
   | un |                                                                 |
   | d* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *h | The height of the widget in lines (not pixels!), measured       |
   | ei | according to the current font size.                             |
   | gh |                                                                 |
   | t* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *  | The color of the focus highlight when the terminal widget does  |
   | hi | not have focus.                                                 |
   | gh |                                                                 |
   | li |                                                                 |
   | gh |                                                                 |
   | tb |                                                                 |
   | ac |                                                                 |
   | kg |                                                                 |
   | ro |                                                                 |
   | un |                                                                 |
   | d* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *h | The color of the focus highlight when the terminal widget has   |
   | ig | the focus.                                                      |
   | hl |                                                                 |
   | ig |                                                                 |
   | ht |                                                                 |
   | co |                                                                 |
   | lo |                                                                 |
   | r* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *h | The thickness of the focus highlight. Default is 0.             |
   | ig |                                                                 |
   | hl |                                                                 |
   | ig |                                                                 |
   | ht |                                                                 |
   | th |                                                                 |
   | ic |                                                                 |
   | kn |                                                                 |
   | es |                                                                 |
   | s* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *i | The color of the insertion cursor. Default is black.            |
   | ns |                                                                 |
   | er |                                                                 |
   | tb |                                                                 |
   | ac |                                                                 |
   | kg |                                                                 |
   | ro |                                                                 |
   | un |                                                                 |
   | d* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *  | Size of the 3-D border around the insertion cursor. Default is  |
   | in | 0.                                                              |
   | se |                                                                 |
   | rt |                                                                 |
   | bo |                                                                 |
   | rd |                                                                 |
   | er |                                                                 |
   | wi |                                                                 |
   | dt |                                                                 |
   | h* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *  | The number of milliseconds the insertion cursor is off during   |
   | in | its blink cycle. Set this option to zero to suppress blinking.  |
   | se | Default is 300.                                                 |
   | rt |                                                                 |
   | of |                                                                 |
   | ft |                                                                 |
   | im |                                                                 |
   | e* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *i | The number of milliseconds the insertion cursor is on during    |
   | ns | its blink cycle. Default is 600.                                |
   | er |                                                                 |
   | to |                                                                 |
   | nt |                                                                 |
   | im |                                                                 |
   | e* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *  | Width of the insertion cursor (its height is determined by the  |
   | in | tallest item in its line). Default is 2 pixels.                 |
   | se |                                                                 |
   | rt |                                                                 |
   | wi |                                                                 |
   | dt |                                                                 |
   | h* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *p | The size of the internal padding added to the left and right of |
   | ad | the text area. Default is one pixel.                            |
   | x* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *p | The size of the internal padding added above and below the text |
   | ad | area. Default is one pixel.                                     |
   | y* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *r | The 3-D appearance of the terminal widget. Default is           |
   | el | ``relief=SUNKEN``.                                              |
   | ie |                                                                 |
   | f* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *s | The background color to use displaying selected text.           |
   | el |                                                                 |
   | ec |                                                                 |
   | tb |                                                                 |
   | ac |                                                                 |
   | kg |                                                                 |
   | ro |                                                                 |
   | un |                                                                 |
   | d* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *  | The width of the border to use around selected text.            |
   | se |                                                                 |
   | le |                                                                 |
   | ct |                                                                 |
   | bo |                                                                 |
   | rd |                                                                 |
   | er |                                                                 |
   | wi |                                                                 |
   | dt |                                                                 |
   | h* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *s | This option specifies how much extra vertical space to add      |
   | pa | between displayed lines of text when a logical line wraps.      |
   | ci | Default is 0.                                                   |
   | ng |                                                                 |
   | 1* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *s | This option specifies how much extra vertical space to add      |
   | pa | between displayed lines of text when a logical line wraps.      |
   | ci | Default is 0.                                                   |
   | ng |                                                                 |
   | 2* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *s | This option specifies how much extra vertical space is added    |
   | pa | below each line of text. If a line wraps, this space is added   |
   | ci | only after the last line it occupies on the display. Default is |
   | ng | 0.                                                              |
   | 3* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *  | Normally, terminal widgets respond to keyboard and mouse        |
   | st | events; set state=NORMAL to get this behavior. If you set       |
   | at | state=DISABLED, the terminal widget will not respond, and you   |
   | e* | won’t be able to pass commands into the terminal.               |
   +----+-----------------------------------------------------------------+
   | *t | This option controls how tab characters position text.          |
   | ab |                                                                 |
   | s* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *  | The width of the widget in characters (not pixels!), measured   |
   | wi | according to the current font size.                             |
   | dt |                                                                 |
   | h* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *w | This option controls the display of lines that are too wide.    |
   | ra | Set wrap=WORD and it will break the line after the last word    |
   | p* | that will fit. With the default behavior, ``wrap=CHAR``, any    |
   |    | line that gets too long will be broken at any character.        |
   +----+-----------------------------------------------------------------+
   | *x | To make the terminal widget horizontally scrollable, set this   |
   | sc | option to the ``set()`` method of the horizontal scrollbar.     |
   | ro |                                                                 |
   | ll |                                                                 |
   | co |                                                                 |
   | mm |                                                                 |
   | an |                                                                 |
   | d* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *y | To make the terminal widget vertically scrollable, set this     |
   | sc | option to the ``set()`` method of the vertical scrollbar.       |
   | ro |                                                                 |
   | ll |                                                                 |
   | co |                                                                 |
   | mm |                                                                 |
   | an |                                                                 |
   | d* |                                                                 |
   +----+-----------------------------------------------------------------+

-  Methods on ``Terminal`` widget objects:

   +-------+--------------------------------------------------------------+
   | Me    | Description                                                  |
   | thods |                                                              |
   +=======+==============================================================+
   | *.cle | Clears the console completely.                               |
   | ar()* |                                                              |
   +-------+--------------------------------------------------------------+
   | *.get | Get the output of the recently run command. Returns None if  |
   | _outp | no command has run else the function will return a           |
   | ut()* | dictionary of error and output.                              |
   +-------+--------------------------------------------------------------+
   | *.r   | Run the command into the terminal.                           |
   | un_co |                                                              |
   | mmand |                                                              |
   | (cmd, |                                                              |
   | gi    |                                                              |
   | ve_in |                                                              |
   | put=N |                                                              |
   | one)* |                                                              |
   +-------+--------------------------------------------------------------+
   | *     | You can use this method to configure the tag properties,     |
   | .tag_ | which include:- - *background*\ - *foreground*\ - *font*\ -  |
   | confi | *justify* (center, left, or right), - *tabs* (this property  |
   | g(tag | has the same functionality of the Text widget tabs’s         |
   | name, | property)- *underline* (used to underline the tagged text).  |
   | optio |                                                              |
   | n=val |                                                              |
   | ue…)* |                                                              |
   +-------+--------------------------------------------------------------+

-  Properties on ``Terminal`` widget objects:

   +----+-----------------------------------------------------------------+
   | Pr | Description                                                     |
   | op |                                                                 |
   | er |                                                                 |
   | ti |                                                                 |
   | es |                                                                 |
   +====+=================================================================+
   | *  | Change the basename of the terminal. Default is **tkterminal$** |
   | te |                                                                 |
   | rm |                                                                 |
   | in |                                                                 |
   | al |                                                                 |
   | .b |                                                                 |
   | as |                                                                 |
   | en |                                                                 |
   | am |                                                                 |
   | e* |                                                                 |
   +----+-----------------------------------------------------------------+
   | *t | Line number bar tells the number of the line by numbering each  |
   | er | line of the terminal. Clicking on any number will select the    |
   | mi | specific line in the terminal. The line with the insert will be |
   | na | highlighted in the number bar. Default is False.                |
   | l. |                                                                 |
   | li |                                                                 |
   | ne |                                                                 |
   | ba |                                                                 |
   | r* |                                                                 |
   +----+-----------------------------------------------------------------+

-  Configure output, error, basename and linebar:

   -  All output text have tag name *output* which can be configured
      with ``terminal.tag_config("output", option=value...)`` method.
   -  All error text also have a tag name *error* which can be
      configured with ``terminal.tag_config("error", option=value...)``
      method.
   -  The basename also have a tag name *basename* configured with
      ``terminal.tag_config("basename", option=value...)`` method.
   -  The linebar is an object of Tkinter Canvas widget which can be
      configured with ``terminal.linebar.configure(option=value ...)``.
      And each number line is a canvas item whose tag name is the number
      itself that can be configured with
      ``terminal.linebar.itemconfigure('item', options...)``.
