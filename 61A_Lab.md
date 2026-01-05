# OK

### Test specific questions

To test a specific question, use the `-q` option with the name of the question:

```
python3 ok -q ### Q1
```

### Test all questions

You can run all the tests with the following command:

```
python3 ok
```

### Display all tests

By default, only tests that **fail** will appear. If you want to see how you did on all tests, you can use the `-v` option:

```
python3 ok -v
```

### Test locally

If you do not want to send your progress to our server or you have any problems logging in, add the `--local` flag to block all communication:

```
python3 ok --local
```



### 



# 0

Documents folder = folder = directory

Terminal: The terminal is a program that allows you to interact with your computer by entering commands.

You already have one called `Windows PowerShell`. Open it up and you should be good to go.



Python Interpreter

code editor - VS code; do not use word, there is some added content that python interpreter cannot understand



### Window terminal 

Common commands

command line interface - CLI

file explorer: an example of graphic user interface



`cd ~`

`~` is a special shorthand way of referring to the home directory. It is a path to the home directory.

Right click on the "address bar" at the top of the window and click "Copy Address".



`mkdir`



`cd ..` (two dots). The `..` means "the parent directory", or one directory above your current directory.



文件名最好不要有空格，文件名有空格用terminal 怎么打开？

## Your First Assignment

### 1. What Would Python Do? (WWPD)

```
python3 ok -q python-basics -u 
python3 ok -q python-basics -u --local [如果你没有UCB ACCOUNT]
```

The command `python3 ok -q python-basics -u` tells the Python interpreter to run the file with the name `ok` in the current working directory. `-q python-basics -u` are inputs provided to the `ok` program that identify which question to run.

As stated in the setup section, if the `python3` command does not work, please try using `python` or `py`.





## Appendix: Useful Python Command Line Options

Here are the most common ways to run Python on a file.

1. Using no command-line options will run the code in the file you provide and return you to the command line. If your file just contains function definitions, you'll see no output unless there is a syntax error.

   ```
   python3 lab00.py
   ```

2. **`-i`**: The `-i` option runs the code in the file you provide, then opens an interactive session (with a `>>>` prompt). You can then evaluate expressions such as calling functions you defined. To exit, type `exit()`. You can also use the keyboard shortcut `Ctrl-D` on Linux/Mac machines or `Ctrl-Z Enter` on Windows.

   If you edit the Python file while running it interactively, you will need to exit and restart the interpreter in order for those changes to take effect.

   Here's how we can run `lab00.py` interactively:

   ```
   python3 -i lab00.py
   ```

3. **`-m doctest`**: Runs the doctests in a file, which are the examples in the docstrings of functions.

   Each test in the file consists of `>>>` followed by some Python code and the expected output.

   Here's how we can run the doctests in `lab00.py`:

   ```
    python3 -m doctest lab00.py
   ```

   When our code passes all of the doctests, no output is displayed. Otherwise, information about the tests that failed will be displayed.



# 02

## Short Circuiting

It evaluates to `True` because Python's `and` and `or` operators *short-circuit*. That is, they don't necessarily evaluate every operand.

| Operator | Checks if:                 | Evaluates from left to right up to: | Example                                |
| :------- | :------------------------- | :---------------------------------- | :------------------------------------- |
| AND      | All values are true        | The first false value               | `False and 1 / 0` evaluates to `False` |
| OR       | At least one value is true | The first true value                | `True or 1 / 0` evaluates to `True`    |





## Core rule (must remember)

> **`and` returns the first “false” value,
>  or the last value if all are “true”.**

In Python:

- `False`, `0`, `None`, `''`, `[]`, etc. are **falsey**
- everything else is **truthy**



> **`or` returns the first truthy value it finds;
>  if none are truthy, it returns the last value.**

It also **short-circuits**.





# 8

If you choose to use VS Code as your text editor (instead of the web-based editor), install the [vscode-scheme](https://marketplace.visualstudio.com/items?itemName=sjhuangx.vscode-scheme) extension so that parentheses are highlighted.

![image-20251211191338530](C:\Users\boying.chen\AppData\Roaming\Typora\typora-user-images\image-20251211191338530.png)

**Tip:** You can open the terminal in VS Code by pressing **Control + `** (the key above Tab).



### q1

 (if (= num1 num2) 0)

 (if (> num1 num2) 1)

### q2

 (define (add-sum inc) (+ inc num) )