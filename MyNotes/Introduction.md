# INTRODUCTION

**The points which I thought were new from LECTURE 1 INTRODUCTION of the course and I ought to remember in the future as well.**

&nbsp;

## Introducing Python

### What is Python?

Python is an interpreted high level programming language.  It is often classified as a
["scripting language"](https://en.wikipedia.org/wiki/Scripting_language) and
is considered similar to languages such as Perl, Tcl, or Ruby.  The syntax
of Python is loosely inspired by elements of C programming.

Python was created by Guido van Rossum around 1990 who named it in honor of Monty Python.

### Why was Python created?

In the words of Python's creator:

> My original motivation for creating Python was the perceived need
> for a higher level language in the Amoeba [Operating Systems]
> project. I realized that the development of system administration
> utilities in C was taking too long. Moreover, doing these things in
> the Bourne shell wouldn't work for a variety of reasons. ... So,
> there was a need for a language that would bridge the gap between C
> and the shell.
>
> - Guido van Rossum

### Where is Python on my Machine?

Although there are many environments in which you might run Python,
Python is typically installed on your machine as a program that runs
from the terminal or command shell. From the terminal, you should be
able to type `python` like this:

```
bash $ python
Python 3.8.1 (default, Feb 20 2020, 09:29:22)
[Clang 10.0.0 (clang-1000.10.44.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hello world")
hello world
>>>
```

### Getting help

Use the `help()` command to get help on the `abs()` function. Then use
`help()` to get help on the `round()` function. Type `help()` just by
itself with no value to enter the interactive help viewer.

One caution with `help()` is that it doesn’t work for basic Python
statements such as `for`, `if`, `while`, and so forth (i.e., if you type
`help(for)` you’ll get a syntax error). You can try putting the help
topic in quotes such as `help("for")` instead. If that doesn’t work,
you’ll have to turn to an internet search.

Followup: Go to <http://docs.python.org> and find the documentation for
the `abs()` function (hint: it’s found under the library reference
related to built-in functions).

### Running Python

Python programs always run inside an interpreter.

The interpreter is a "console-based" application that normally runs
from a command shell.

```bash
python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Expert programmers usually have no problem using the interpreter in
this way, but it's not so user-friendly for beginners.  You may be using
an environment that provides a different interface to Python.  That's fine,
but learning how to run Python terminal is still a useful skill to know.

### Interactive Mode

When you start Python, you get an *interactive* mode where you can experiment.

If you start typing statements, they will run immediately. There is no
edit/compile/run/debug cycle.

```python
>>> print('hello world')
hello world
>>> 37*42
1554
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>>
```

This so-called *read-eval-print-loop* (or REPL) is very useful for debugging and exploration.

If you're using an IDE, it might be hidden behind a menu option or other window.

Let's take a closer look at the elements of the REPL:

- `>>>` is the interpreter prompt for starting a new statement.
- `...` is the interpreter prompt for continuing a statement. Enter a blank line to finish typing and run what you've entered.

The `...` prompt may or may not be shown depending on your environment. For this course,
it is shown as blanks to make it easier to cut/paste code samples.

The underscore `_` holds the last result.

```python
>>> 37 * 42
1554
>>> _ * 2
3108
>>> _ + 50
3158
>>>
```

*This is only true in the interactive mode.* You never use `_` in a program.

### Case Sensitivity

Python is case sensitive. Upper and lower-case letters are considered different letters.
These are all different variables:

```python
name = 'Jake'
Name = 'Elwood'
NAME = 'Guido'
```

Language statements are always lower-case.

```python
while x < 0:   # OK
WHILE x < 0:   # ERROR
```

### Indentation best practices

* Use spaces instead of tabs.
* Use 4 spaces per level.
* Use a Python-aware editor.

Python's only requirement is that indentation within the same block
be consistent.   For example, this is an error:

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
        day = day + 1 # ERROR
    num_bills = num_bills * 2
```

### Printing

The `print` function produces a single line of text with the values passed.

```python
print('Hello world!') # Prints the text 'Hello world!'
```

You can use variables. The text printed will be the value of the variable, not the name.

```python
x = 100
print(x) # Prints the text '100'
```

If you pass more than one value to `print` they are separated by spaces.

```python
name = 'Jake'
print('My name is', name) # Print the text 'My name is Jake'
```

`print()` always puts a newline at the end.

```python
print('Hello')
print('My name is', 'Jake')
```

This prints:

```code
Hello
My name is Jake
```

The extra newline can be suppressed:

```python
print('Hello', end=' ')
print('My name is', 'Jake')
```

This code will now print:

```code
Hello My name is Jake
```

### User input

To read a line of typed user input, use the `input()` function:

```python
name = input('Enter your name:')
print('Your name is', name)
```

`input` prints a prompt to the user and returns their response.
This is useful for small programs, learning exercises or simple debugging.
It is not widely used for real programs.

### pass statement

Sometimes you need to specify an empty code block. The keyword `pass` is used for it.

```python
if a > b:
    pass
else:
    print('Computer says false')
```

This is also called a "no-op" statement. It does nothing. It serves as a placeholder for statements, possibly to be added later.

## Numbers

This section discusses mathematical calculations.

### Types of Numbers

Python has 4 types of numbers:

* Booleans
* Integers
* Floating point
* Complex (imaginary numbers)

### Booleans (bool)

Booleans have two values: `True`, `False`.

```python
a = True
b = False
```

Numerically, they're evaluated as integers with value `1`, `0`.

```python
c = 4 + True # 5
d = False
if d == 0:
    print('d is False')
```

*But, don't write code like that. It would be odd.*

### Integers (int)

Signed values of arbitrary size and base:

```python
a = 37
b = -299392993727716627377128481812241231
c = 0x7fa8      # Hexadecimal
d = 0o253       # Octal
e = 0b10001111  # Binary
```

Common operations:

```
x + y      Add
x - y      Subtract
x * y      Multiply
x / y      Divide (produces a float)
x // y     Floor Divide (produces an integer)
x % y      Modulo (remainder)
x ** y     Power
x << n     Bit shift left
x >> n     Bit shift right
x & y      Bit-wise AND
x | y      Bit-wise OR
x ^ y      Bit-wise XOR
~x         Bit-wise NOT
abs(x)     Absolute value
```

### Floating point (float)

Use a decimal or exponential notation to specify a floating point value:

```python
a = 37.45
b = 4e5 # 4 x 10**5 or 400,000
c = -1.345e-10
```

Floats are represented as double precision using the native CPU representation [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754).
This is the same as the `double` type in the programming language C.

> 17 digits of precision  
> Exponent from -308 to 308

Be aware that floating point numbers are inexact when representing decimals.

```python
>>> a = 2.1 + 4.2
>>> a == 6.3
False
>>> a
6.300000000000001
>>>
```

This is **not a Python issue**, but the underlying floating point hardware on the CPU.

Common Operations:

```
x + y      Add
x - y      Subtract
x * y      Multiply
x / y      Divide
x // y     Floor Divide
x % y      Modulo
x ** y     Power
abs(x)     Absolute Value
```

These are the same operators as Integers, except for the bit-wise operators.
Additional math functions are found in the `math` module.

```python
import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
```


### Comparisons

The following comparison / relational operators work with numbers:

```
x < y      Less than
x <= y     Less than or equal
x > y      Greater than
x >= y     Greater than or equal
x == y     Equal to
x != y     Not equal to
```

You can form more complex boolean expressions using

`and`, `or`, `not`

Here are a few examples:

```python
if b >= a and b <= c:
    print('b is between a and c')

if not (b < a or b > c):
    print('b is still between a and c')
```

### Converting Numbers

The type name can be used to convert values:

```python
a = int(x)    # Convert x to integer
b = float(x)  # Convert x to float
```

Try it out.

```python
>>> a = 3.14159
>>> int(a)
3
>>> b = '3.14159' # It also works with strings containing numbers
>>> float(b)
3.14159
>>>
```

### Mystery question

`int()` and `float()` can be used to convert numbers.  For example,

```python
>>> int("123")
123
>>> float("1.23")
1.23
>>>
```

With that in mind, can you explain this behavior?

```python
>>> bool("False")
True
>>>
```

**My Answer:** it is checking if "False" is a string or not and therefore returning TRUE as a boolean.

## Strings

### Representing Literal Text

String literals are written in programs with quotes.

```python
# Single quote
a = 'Yeah but no but yeah but...'

# Double quote
b = "computer says no"

# Triple quotes
c = '''
Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
not around the eyes,
don't look around the eyes,
look into my eyes, you're under.
'''
```

Normally strings may only span a single line. Triple quotes capture all text enclosed across multiple lines
including all formatting.

There is no difference between using single (') versus double (")
quotes. *However, the same type of quote used to start a string must be used to
terminate it*.

### String escape codes

Escape codes are used to represent control characters and characters that can't be easily typed
directly at the keyboard.  Here are some common escape codes:

```
'\n'      Line feed
'\r'      Carriage return
'\t'      Tab
'\''      Literal single quote
'\"'      Literal double quote
'\\'      Literal backslash
```

### String Indexing

Strings work like an array for accessing individual characters. You use an integer index, starting at 0.
Negative indices specify a position relative to the end of the string.

```python
a = 'Hello world'
b = a[0]          # 'H'
c = a[4]          # 'o'
d = a[-1]         # 'd' (end of string)
```

You can also slice or select substrings specifying a range of indices with `:`.

```python
d = a[:5]     # 'Hello'
e = a[6:]     # 'world'
f = a[3:8]    # 'lo wo'
g = a[-5:]    # 'world'
```

The character at the ending index is not included.  Missing indices assume the beginning or ending of the string.

### String operations

Concatenation, length, membership and replication.

```python
# Concatenation (+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say ' + a          # 'Say HelloWorld'

# Length (len)
s = 'Hello'
len(s)                  # 5

# Membership test (`in`, `not in`)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# Replication (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'
```

### String methods

Strings have methods that perform various operations with the string data.

Example: stripping any leading / trailing white space.

```python
s = '  Hello '
t = s.strip()     # 'Hello'
```

Example: Case conversion.

```python
s = 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'
```

Example: Replacing text.

```python
s = 'Hello world'
t = s.replace('Hello' , 'Hallo')   # 'Hallo world'
```

**More string methods:**

Strings have a wide variety of other methods for testing and manipulating the text data.
This is a small sample of methods:

```python
s.endswith(suffix)     # Check if string ends with suffix
s.find(t)              # First occurrence of t in s
s.index(t)             # First occurrence of t in s
s.isalpha()            # Check if characters are alphabetic
s.isdigit()            # Check if characters are numeric
s.islower()            # Check if characters are lower-case
s.isupper()            # Check if characters are upper-case
s.join(slist)          # Join a list of strings using s as delimiter
s.lower()              # Convert to lower case
s.replace(old,new)     # Replace text
s.rfind(t)             # Search for t from end of string
s.rindex(t)            # Search for t from end of string
s.split([delim])       # Split string into list of substrings
s.startswith(prefix)   # Check if string starts with prefix
s.strip()              # Strip leading/trailing space
s.upper()              # Convert to upper case
```

### String Mutability

Strings are "immutable" or read-only.
Once created, the value can't be changed.

```python
>>> s = 'Hello World'
>>> s[1] = 'a'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

**All operations and methods that manipulate string data, always create new strings.**

### String Conversions

Use `str()` to convert any value to a string. The result is a string holding the
same text that would have been produced by the `print()` statement.

```python
>>> x = 42
>>> str(x)
'42'
>>>
```

### Raw Strings

Raw strings are string literals with an uninterpreted backslash. They
are specified by prefixing the initial quote with a lowercase "r".

```python
>>> rs = r'c:\newdata\test' # Raw (uninterpreted backslash)
>>> rs
'c:\\newdata\\test'
```

The string is the literal text enclosed inside, exactly as typed.
This is useful in situations where the backslash has special
significance. Example: filename, regular expressions, etc.

### f-Strings

A string with formatted expression substitution.

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> a = f'{name:>10s} {shares:10d} {price:10.2f}'
>>> a
'       IBM        100      91.10'
>>> b = f'Cost = ${shares*price:0.2f}'
>>> b
'Cost = $9110.00'
>>>
```

### Exercise 1.18: Regular Expressions

One limitation of the basic string operations is that they don't
support any kind of advanced pattern matching.  For that, you
need to turn to Python's `re` module and regular expressions.
Regular expression handling is a big topic, but here is a short
example:

```python
>>> text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
>>> # Find all occurrences of a date
>>> import re
>>> re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
>>> # Replace all occurrences of a date with replacement text
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'
>>>
```

For more information about the `re` module, see the official documentation at
[https://docs.python.org/library/re.html](https://docs.python.org/3/library/re.html).

### Checking different operations that can be done on a string

As you start to experiment with the interpreter, you often want to
know more about the operations supported by different objects.  For
example, how do you find out what operations are available on a
string?

Depending on your Python environment, you might be able to see a list
of available methods via tab-completion.  For example, try typing
this:

```python
>>> s = 'hello world'
>>> s.<tab key>
>>>
```

If hitting tab doesn't do anything, you can fall back to the
builtin-in `dir()` function.  For example:

```python
>>> s = 'hello'
>>> dir(s)
['__add__', '__class__', '__contains__', ..., 'find', 'format',
'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']
>>>
```

`dir()` produces a list of all operations that can appear after the `(.)`.
Use the `help()` command to get more information about a specific operation:

```python
>>> help(s.upper)
Help on built-in function upper:

upper(...)
    S.upper() -> string

    Return a copy of the string S converted to uppercase.
>>>
```