Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li = []
li
[]
type(li)
<class 'list'>
tp = ()
tp
()
type(tp)
<class 'tuple'>
tp2 = tuple()
tp2 = tuple()
tp2
()
type(tp2)
<class 'tuple'>
num = 2.
num
2.0
type(num)
<class 'float'>
num = 2,
num
(2,)
type(num)
<class 'tuple'>
num = (2, )
t = tuple()
t
()
tuple(1)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    tuple(1)
TypeError: 'int' object is not iterable
isinstance(t, tuple)
True
isinstance(t, list)
False

n = (1, 2, 3, 4, 5)
n
(1, 2, 3, 4, 5)
n[0]
1
n[-1]
5
n[2]
3
n[1] = 9999
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    n[1] = 9999
TypeError: 'tuple' object does not support item assignment
n
(1, 2, 3, 4, 5)
liN = list (n)
liN[2] = 333
liN
[1, 2, 333, 4, 5]
n
(1, 2, 3, 4, 5)
n = tuple(liN)
n
(1, 2, 333, 4, 5)

t = (1, 23, 4)
a,b,c = t
a
1
b
23
c
4
li
[]
li = [1, 2, 3, 4]
a,b,c,d = li
a
1
b
2
c
3
d
4
s = "a b c"
s = "abc"
s
'abc'
a
1
a,b,c = s
a
'a'
b
'b'
c
'c'
li
[1, 2, 3, 4]
s = "abc"
t = (1,2,3,4,5,6,7)
a,b,c = t
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a,b,c = t
ValueError: too many values to unpack (expected 3)
a,b,*c = t
a
1
b
2
c
[3, 4, 5, 6, 7]
type(c)
<class 'list'>
t
(1, 2, 3, 4, 5, 6, 7)
a,*b,c = t
a
1
b
[2, 3, 4, 5, 6]
c
7
st = "jgfjf,gjk"
a,*b,c = st
c
'k'
a
'j'
b
['g', 'f', 'j', 'f', ',', 'g', 'j']
def numbers():
    return 1, 2, 3, 4, 5

numbers()
(1, 2, 3, 4, 5)
a, *b = numbers()
a
1
b
[2, 3, 4, 5]
result = numbers()
result
(1, 2, 3, 4, 5)
def numbers():
    return "error:...",1,2,3,4,5

numbers()
('error:...', 1, 2, 3, 4, 5)
err, *tp_n = numbers()
err
'error:...'
tp_n
[1, 2, 3, 4, 5]
if err == error:...":
SyntaxError: unterminated string literal (detected at line 1)
if err == "error:...":
    print(123)

    
123
t
(1, 2, 3, 4, 5, 6, 7)
t[:]
(1, 2, 3, 4, 5, 6, 7)
aaa = t
aaa
(1, 2, 3, 4, 5, 6, 7)
aaa[1] = 99
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    aaa[1] = 99
TypeError: 'tuple' object does not support item assignment
t
(1, 2, 3, 4, 5, 6, 7)t
t[1:]
(2, 3, 4, 5, 6, 7)
t[1:]
(2, 3, 4, 5, 6, 7)
t[1:5]
(2, 3, 4, 5)
t
(1, 2, 3, 4, 5, 6, 7)
t[1:]
(2, 3, 4, 5, 6, 7)
t[1:-1]
(2, 3, 4, 5, 6)
t[::2]
(1, 3, 5, 7)
t[::-2]
(7, 5, 3, 1)
t
(1, 2, 3, 4, 5, 6, 7)
t += 1
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    t += 1
TypeError: can only concatenate tuple (not "int") to tuple
t += (1,)
t
(1, 2, 3, 4, 5, 6, 7, 1)
t + t
(1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1)
t * 6
(1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1)
t +=  4
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    t +=  4
TypeError: can only concatenate tuple (not "int") to tuple
5 in t
True
99999 in t
False
t *= 4

t
(1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1)
a
1
b
[2, 3, 4, 5]
c
'k'
b = "kjgkgf"
a,b,c
(1, 'kjgkgf', 'k')
ordersId (1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    ordersId (1,2,3,4,5)
NameError: name 'ordersId' is not defined
ordersId = (1,2,3,4,5)
ordersId += (len(ordersId)+1, )
ordersId += (len(ordersId)+1, )
ordersId += (len(ordersId)+1, )
ordersId += (len(ordersId)+1, )
ordersId += (len(ordersId)+1, )
ordersId
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
ordersId += (len(ordersId)+1
ordersId += len(ordersId)+1
             
SyntaxError: '(' was never closed
t = (1,2,3,4)
             
155
             
155
144
             
144
t[1:3]
             
(2, 3)
(155, )
             
(155,)
(144, )
             
(144,)
t = (155, ) + t[1:3] + (144, )
             
t
             
(155, 2, 3, 144)
t.count(2)
             
1
t.count(8888)
             
0
t.index(2)
             
1
t.index(144)
             
3
del t[0]
             
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    del t[0]
TypeError: 'tuple' object doesn't support item deletion
del t
             
t
             
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    t
NameError: name 't' is not defined. Did you mean: 'tp'?
t = (4,3,2,1)
             
for value in t:
    print(value)

             
4
3
2
1
for value in t:
    print(value) *2 ==4:
             
SyntaxError: invalid syntax
for value in t:
    if value *2 == 4:
        continue
    print(value)

    
4
3
1
t
(4, 3, 2, 1)
n
(1, 2, 333, 4, 5)
n = len(t)
n
4
for i in range(n):
    print(i, ", value:", t[i])

    
0 , value: 4
1 , value: 3
2 , value: 2
3 , value: 1






di = {}
type ()
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    type ()
TypeError: type() takes 1 or 3 arguments
type(di)
<class 'dict'>
di1 = dict()
di1
{}
type(di)
<class 'dict'>
se
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    se
NameError: name 'se' is not defined. Did you mean: 's'?
se = {1, 2 , 55, 9, 8}
se
{1, 2, 55, 8, 9}
di = {1:"value", "sd":423}
se
{1, 2, 55, 8, 9}
di
{1: 'value', 'sd': 423}
hash
<built-in function hash>
a = 3
b = 6.
c = "fgg"
li = []
se = {}
tp = (1,2,3,4)
hash(a)
3
hash(b)
6
hash(c)
2460463713805887654
hash(tp)
590899387183067792
hash(se)
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    hash(se)
TypeError: unhashable type: 'dict'
hash(li)
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    hash(li)
TypeError: unhashable type: 'list'
def a():
    pass

a
<function a at 0x0000022C44130900>
hash(a)
149321494672
di
{1: 'value', 'sd': 423}
hash(di)
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    hash(di)
TypeError: unhashable type: 'dict'
dd = {1:"d", 2.:"jhg", s:"jhgg", a:"5587"}
dd
{1: 'd', 2.0: 'jhg', 'abc': 'jhgg', <function a at 0x0000022C44130900>: '5587'}
dd[1]
'd'
dd[111]
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    dd[111]
KeyError: 111
dd[s]
'jhgg'
dd[s]
'jhgg'
dd
{1: 'd', 2.0: 'jhg', 'abc': 'jhgg', <function a at 0x0000022C44130900>: '5587'}
fs = frozenset([12,2,34,5])
fs
frozenset({2, 5, 12, 34})
type(fs)
<class 'frozenset'>
hash(fs)
8453542846474786068
dd = {1:"d", 2.:"jhg", s:"jhgg", a:"5587", }
dd = {1:"d", 2.:"jhg", s:"jhgg", a:"5587", fs:"froz set"}
dd[fs]
'froz set'
for v in dd.values():
    print(v)

    
d
jhg
jhgg
5587
froz set
for v in dd.keys():
    print(v)

    
1
2.0
abc
<function a at 0x0000022C44130900>
frozenset({2, 5, 12, 34})
for v in dd.items():
    print(k, ":", v)

             
Traceback (most recent call last):
  File "<pyshell#228>", line 2, in <module>
    print(k, ":", v)
NameError: name 'k' is not defined
for tp in dd.items():
             print(tp)

             
(1, 'd')
(2.0, 'jhg')
('abc', 'jhgg')
(<function a at 0x0000022C44130900>, '5587')
(frozenset({2, 5, 12, 34}), 'froz set')
dd[1]
             
'd'
dd.get(1123)
             
dd[-4] = "vkjsfhjdf"
             
dd[0]
             
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    dd[0]
KeyError: 0
dd.keys()
             
dict_keys([1, 2.0, 'abc', <function a at 0x0000022C44130900>, frozenset({2, 5, 12, 34}), -4])
dd[1] = 123
             
dd
             
{1: 123, 2.0: 'jhg', 'abc': 'jhgg', <function a at 0x0000022C44130900>: '5587', frozenset({2, 5, 12, 34}): 'froz set', -4: 'vkjsfhjdf'}
dd.update((55, "555555"))
             
Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    dd.update((55, "555555"))
TypeError: cannot convert dictionary update sequence element #0 to a sequence
dd.update({55, "555555"})
             
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    dd.update({55, "555555"})
ValueError: dictionary update sequence element #0 has length 6; 2 is required
dd.update({5:"555555"})
             
dd
             
{1: 123, 2.0: 'jhg', 'abc': 'jhgg', <function a at 0x0000022C44130900>: '5587', frozenset({2, 5, 12, 34}): 'froz set', -4: 'vkjsfhjdf', 5: '555555'}
dd.update([2, 222), (5,5555)])
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
dd.update([(2, 222), (5,5555)])
dd
{1: 123, 2.0: 222, 'abc': 'jhgg', <function a at 0x0000022C44130900>: '5587', frozenset({2, 5, 12, 34}): 'froz set', -4: 'vkjsfhjdf', 5: 5555}
len(dd)
7
dd.pop(1)
123
dd.popitem()
(5, 5555)
del dd["s"]
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    del dd["s"]
KeyError: 's'
1 in dd
False
key = input()
ff
dd
{2.0: 222, 'abc': 'jhgg', <function a at 0x0000022C44130900>: '5587', frozenset({2, 5, 12, 34}): 'froz set', -4: 'vkjsfhjdf'}
if ff in dd:
    dd.pop(ff)
else:
    print("nety")

    
Traceback (most recent call last):
  File "<pyshell#257>", line 1, in <module>
    if ff in dd:
NameError: name 'ff' is not defined. Did you mean: 'fs'?
if key in dd:
    dd.pop(ff)
else:
    print("nety")

    
nety
key = 2.0
if key in dd:
    dd.pop(key)
    print("OK")
else:
...     print("nety")
... 
...     
222
OK
>>> if key in dd:
...     dd.pop(key)
...     print("OK")
... else:
...     print("nety")
... 
...     
nety
>>> li = []
>>> li.pop()
Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    li.pop()
IndexError: pop from empty list
>>> di = {i:i**3 for i in range(50, 60)}
>>> di
{50: 125000, 51: 132651, 52: 140608, 53: 148877, 54: 157464, 55: 166375, 56: 175616, 57: 185193, 58: 195112, 59: 205379}
>>> {50: 125000, 51: 132651, 52: 140608, 53: 148877, 54: 157464, 55: 166375, 56: 175616, 57: 185193, 58: 195112, 59: 205379}
{50: 125000, 51: 132651, 52: 140608, 53: 148877, 54: 157464, 55: 166375, 56: 175616, 57: 185193, 58: 195112, 59: 205379}
>>> 
>>> di = {i**3 for i in range(50, 60)}
>>> type(di)
<class 'set'>
