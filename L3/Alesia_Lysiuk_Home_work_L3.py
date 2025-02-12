Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li =  []
print(li)
[]
li1 = list()

print(lil)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(lil)
NameError: name 'lil' is not defined. Did you mean: 'li'?
a = [1,2,3,True, "edfe"]
a
[1, 2, 3, True, 'edfe']
a[3]
True

a[4]
'edfe'
a["1"]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a["1"]
TypeError: list indices must be integers or slices, not str
a[5]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a[5]
IndexError: list index out of range
print(li1)
[]
type(li)
<class 'list'>
type(a)
<class 'list'>
type(a[0])
<class 'int'>
st = "Hello"
st.upper()
'HELLO'
st
'Hello'
q = 100
q.upper()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    q.upper()
AttributeError: 'int' object has no attribute 'upper'
a.upper()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.upper()
AttributeError: 'list' object has no attribute 'upper'
"hhh".upper()
'HHH'
a = [4, 3, 45, 18, 15, 2]
a
[4, 3, 45, 18, 15, 2]
a.append(777)
a
[4, 3, 45, 18, 15, 2, 777]
a.insert(2, 9)
a
[4, 3, 9, 45, 18, 15, 2, 777]
len(a)
8
a.revers()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.revers()
AttributeError: 'list' object has no attribute 'revers'. Did you mean: 'reverse'?
a.reverse
<built-in method reverse of list object at 0x00000177FD7DE100>
a
[4, 3, 9, 45, 18, 15, 2, 777]
a.pop()
777
a
[4, 3, 9, 45, 18, 15, 2]
a.pop()
2
a
[4, 3, 9, 45, 18, 15]
res = a.pop(3)
a
[4, 3, 9, 18, 15]
del a[5]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    del a[5]
IndexError: list assignment index out of range
del li
li
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    li
NameError: name 'li' is not defined. Did you mean: 'li1'?
a.remove (1)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.remove (1)
ValueError: list.remove(x): x not in list
a.remove (18)
a
[4, 3, 9, 15]
toDel = 555
if toDel in a:
    a.remove(toDel)

    
a.count(9)
1
a
[4, 3, 9, 15]
a.count(777)
0
a.clear()
a
[]
a.index()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.index()
TypeError: index expected at least 1 argument, got 0
a = [4, 3, 9, 15]
a.index(3)
1
li = [7,7,7]
a += li
a
[4, 3, 9, 15, 7, 7, 7]
hat_list = [1, 2, 3, 4, 5]
hat_list
[1, 2, 3, 4, 5]
len(hat_list)
5
hat_list.replace(2, 11)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    hat_list.replace(2, 11)
AttributeError: 'list' object has no attribute 'replace'
hat_list.insert(2, 9)
hat_list
[1, 2, 9, 3, 4, 5]
hat_list.del(7)
SyntaxError: invalid syntax
hat_list.clear(7)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    hat_list.clear(7)
TypeError: list.clear() takes no arguments (1 given)
>>> [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
>>> hat_list = [1,2,3,4,5]
... print(len(hat_list))
... hat_list[2] = int(input('enter any number: '))
... print(hat_list)
... hat_list.pop(-1)
... print(hat_list)
... print(len(hat_list))
... 
... 5
... enter any number: 222
... [1, 2, 222, 4, 5]
... [1, 2, 222, 4]
... 4
SyntaxError: multiple statements found while compiling a single statement
>>> print(len(hat_list))
6
>>> hat_list[2] = int(input('enter any number: '))
enter any number: 
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    hat_list[2] = int(input('enter any number: '))
ValueError: invalid literal for int() with base 10: ''
>>> hat_list.pop(-1)
5
>>> print(hat_list)
[1, 2, 9, 3, 4]
>>> print(len(hat_list))
5
>>> enter any number: 222
SyntaxError: invalid syntax
