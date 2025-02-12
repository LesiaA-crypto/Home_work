Python 3.10.5 (main, Jul 22 2022, 17:09:35) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 1+1
2
>>> (print)
<built-in function print>
>>> print()

>>> print(123)
123
>>> print
<built-in function print>
>>> print("Hello word!")
Hello word!
>>> Print(Hello)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> print (123
... print 123)
  File "<stdin>", line 1
    print (123
           ^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> lol
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lol' is not defined
>>> print("Hello\n")
Hello

>>> print("Hello world\nday for beginning")
Hello world
day for beginning
>>> print("Hello world nday for beginning")
Hello world nday for beginning
>>> print('Hello')
Hello
>>> print('"hhhh"')
"hhhh"
>>> print("ппп\jjj")
ппп\jjj
>>> print("А", "П", "р")
А П р
>>> rint ("Hm\tHello\n'world!'")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rint' is not defined. Did you mean: 'print'?
>>> Hm Hello
  File "<stdin>", line 1
    Hm Hello
       ^^^^^
SyntaxError: invalid syntax
>>> 'world!'
'world!'
>>> print(1,2,3,4)
1 2 3 4
>>> print(1,2,3,4 sep="***")
  File "<stdin>", line 1
    print(1,2,3,4 sep="***")
                ^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(1, 2, 3, 4 sep="***")
  File "<stdin>", line 1
    print(1, 2, 3, 4 sep="***")
                   ^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> prinr()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'prinr' is not defined. Did you mean: 'print'?
>>> print(1, 2, 3, 4, sep="***")
1***2***3***4
>>> print(programming, Essentials,"in...Python", sep="***")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'programming' is not defined
>>> print(programming, Essentials sep="***")
  File "<stdin>", line 1
    print(programming, Essentials sep="***")
                       ^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(programming, Essentials, sep="***")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'programming' is not defined
>>> print("Programming", "Essentials", "in", sep="***", end="...Python")
Programming***Essentials***in...Python>>> 
>>> print("Programming", "Essentials", "in", sep="***", end="...Python")
Programming***Essentials***in...Python>>> >>> print("Hello world\nday for beginning")
  File "<stdin>", line 1
    >>> print("Hello world\nday for beginning")
    ^^
SyntaxError: invalid syntax
>>> 
>>> Hello world
  File "<stdin>", line 1
    Hello world
          ^^^^^
SyntaxError: invalid syntax
>>> print(-123)
-123
>>> print(111_11)
11111
>>> print(2.3)
2.3
>>> print(2,3)
2 3
>>> print(2, 3)
2 3
>>> print("""ллллл
... 123
... оооо
... \n
... 111""")
ллллл
123
оооо


111
>>> print("""
... "1+1"
... """)

"1+1"

>>> type(1)
<class 'int'>
>>> type(False)
<class 'bool'>
>>> print(""")I m leaning Python"""
... 
... type(False)
  File "<stdin>", line 1
    print(""")I m leaning Python"""
          ^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("I'm"
... "hello"
... "python"
... )
I'mhellopython
>>> print("""
... ... "I'm"
... ... ""Learning""
... ... \"""Python\""")
... ... """)

... "I'm"
... ""Learning""
... """Python""")
... 
>>> name = "Алеся"
>>> print(name)
Алеся
>>> 1 cat = 77
  File "<stdin>", line 1
    1 cat = 77
      ^^^
SyntaxError: invalid syntax
>>> h+h = 99
  File "<stdin>", line 1
    h+h = 99
    ^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> name = "алеся"
>>> name = "алеся"
>>> Name = "алеся"
>>> print("Name")
Name
>>> Name = true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> name = True
>>> print(name)
True
>>> 5*6
30
>>> 5.0*7
35.0
>>> х = 10
>>> х
10
>>> х +=5
>>> х
15
>>> q=d=r=t=5
>>> q
5
>>> 2* (4/5) + 6
7.6
>>> 8/4
2.0
>>> 0.8*2
1.6
>>> Jonn = 3
>>> Adam = 5
>>> Mary = 2
>>> Jonn + Adam + Mary 
10
>>> john,mary,adam=3,5,7
>>> >>> total_apples=john+mary+adam
  File "<stdin>", line 1
    >>> total_apples=john+mary+adam
    ^^
SyntaxError: invalid syntax
>>> >>> print(total_apples)
  File "<stdin>", line 1
    >>> print(total_apples)
    ^^
SyntaxError: invalid syntax
Алеся
>>>  john,mary,adam=3,5,7
  File "<stdin>", line 1
    john,mary,adam=3,5,7
IndentationError: unexpected indent
>>> >>> total_apples=john+mary+adam
  File "<stdin>", line 1
    >>> total_apples=john+mary+adam
    ^^
SyntaxError: invalid syntax
>>> >>> print(total_apples)
  File "<stdin>", line 1
    >>> print(total_apples)
    ^^
SyntaxError: invalid syntax
>>> john,mary,adam=3,5,7
>>> total_apples=john+mary+adam
>>> print(total_apples)
15
>>> 