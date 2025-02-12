Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 input("Дай мне пароль?")
 
SyntaxError: unexpected indent
input("Дай мне пароль?")
Дай мне пароль?hvjvj123
'hvjvj123'
password = input("Дай мне пароль?")
Дай мне пароль?
print(password)

input = 12345
a = input (msg)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a = input (msg)
NameError: name 'msg' is not defined

number = input('lfq vyt xbckj:')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    number = input('lfq vyt xbckj:')
TypeError: 'int' object is not callable
a = '123'
b = '3.5'
c = 123
type(a)
<class 'str'>
type(b)
<class 'str'>
type(c)
<class 'int'>
d = 5.5
type (d)
<class 'float'>
<class 'float'>
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
a = 1.777
print(a)
1.777
b = 555.
print(b)
555.0
print(2**3)
8
2 ** 3 ** 2
512
512
512
12/0
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    12/0
ZeroDivisionError: division by zero
0/6
0.0
0 // 555
0
s, ss = 'hello', 'lol'
print(s, ss)
hello lol
s
'hello'
ss
'lol'
s + ss
'hellolol'
res = s + s + s + ss
res
'hellohellohellolol'
ss
'lol'
ss * 5
'lollollollollol'
ss * 5.
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    ss * 5.
TypeError: can't multiply sequence by non-int of type 'float'
ss
'lol'
s
'hello'
len(s)
5
len(ss)
3
a = 'ghf' 'jjj' 'jjj'
a
'ghfjjjjjj'
print('1', 'ngfh', '12' '555')
1 ngfh 12555
a = '*' * 50
a =
SyntaxError: invalid syntax

a
'**************************************************'
len(a)
50
print(1, '+', 2, '=', 1+2)
1 + 2 = 3
print(a, '+', b, '=', a+b)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(a, '+', b, '=', a+b)
TypeError: can only concatenate str (not "float") to str
a, b = 1, 2
a
1
b
2
print(a, "+", b, "=", a+b)
1 + 2 = 3
print(f'{a} + {b} ={a+b}")
      
SyntaxError: unterminated f-string literal (detected at line 1)
pass
      
import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(f"{a} + {b} = {a+b}")
1 + 2 = 3
1 + 2 = 3
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
a = int(input("-->"))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a = int(input("-->"))
TypeError: 'int' object is not callable
a = int(input("-->"))
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a = int(input("-->"))
TypeError: 'int' object is not callable

=================== RESTART: Shell ===================
a = int(input("-->"))
-->
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a = int(input("-->"))
ValueError: invalid literal for int() with base 10: ''
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
