Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
q [1, 3, 5, 6]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    q [1, 3, 5, 6]
NameError: name 'q' is not defined
li
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    li
NameError: name 'li' is not defined
li=[44, 55, 66, 777]
li
[44, 55, 66, 777]
li.reverse()
li
[777, 66, 55, 44]
li.append(1000)
li
[777, 66, 55, 44, 1000]
print(li)
[777, 66, 55, 44, 1000]
sorted(li)
[44, 55, 66, 777, 1000]
li
[777, 66, 55, 44, 1000]
for i in sorted (li):
    print(i, sep='')

    
44
55
66
777
1000
li
[777, 66, 55, 44, 1000]
sorted(li, reverse=True)
[1000, 777, 66, 55, 44]
li
[777, 66, 55, 44, 1000]

li = [3, 5, 0, -10, 4]

a, b = 66, 77
tmp = a
a = b
b = tmp
a
77
b
66
a, b = 66, 77
a, b = b, a
a
77
b
66


li = [3, 5, 0, -10, 4]
li[1], li[2] = li[2], li[1]
li
[3, 0, 5, -10, 4]
li[2], li[3] = li[3], li[2]
li
[3, 0, -10, 5, 4]
li[0], li[1] = li[1], li[0]
li
[0, 3, -10, 5, 4]

max min sum
SyntaxError: invalid syntax

max(li)
5
min(li)
-10
sum(li)
2
sum(li)/len(li)
0.4
print
<built-in function print>
max
<built-in function max>
li - [1,2,3,4]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    li - [1,2,3,4]
TypeError: unsupported operand type(s) for -: 'list' and 'list'
li = [1,2,3,4]
a = li
li
[1, 2, 3, 4]
a
[1, 2, 3, 4]
id(li)
2513130749376
a[1] = 99999
a
[1, 99999, 3, 4]
li
[1, 99999, 3, 4]
li = [1,2,3,4]
a - li.copy()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a - li.copy()
TypeError: unsupported operand type(s) for -: 'list' and 'list'
a = li.copy()
a
[1, 2, 3, 4]
li = [1,2,3,4]
a = li[:]
a
[1, 2, 3, 4]
id(a)
2513130749312
li
[1, 2, 3, 4]
li[:]
[1, 2, 3, 4]
li[:3]
[1, 2, 3]
li[1:]
[2, 3, 4]
li
[1, 2, 3, 4]
li += li
li
[1, 2, 3, 4, 1, 2, 3, 4]
kk = li[::2]
kk
[1, 3, 1, 3]
li
[1, 2, 3, 4, 1, 2, 3, 4]
li[::-1]
[4, 3, 2, 1, 4, 3, 2, 1]
li
[1, 2, 3, 4, 1, 2, 3, 4]
777 in li
False
4 in li
True
li.count()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    li.count()
TypeError: list.count() takes exactly one argument (0 given)


s = {}
type(s)
<class 'dict'>
s = set()
type(s)
<class 'set'>
s = {"gf", 1, 2, 3, 5, 6, 7}
s = {"gf", 1, 2, 3, 5, 6, 7}
s
{1, 2, 3, 5, 6, 7, 'gf'}
s.add(1)
s
{1, 2, 3, 5, 6, 7, 'gf'}
for v in s:
    print(v, end="")

    
123567gf
999 in s
False
1 in s
True
s.update({1, 5, 3, 9})
s
{1, 2, 3, 5, 6, 7, 'gf', 9}
s.clear()
s
set()
s= {1, 2, 3, 4, 666}
s.remove(555)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    s.remove(555)
KeyError: 555
s.remove(4)
s
{1, 2, 3, 666}
s.discard(2)
s
{1, 3, 666}
len(s)
3
li = list(set(li))
li
[1, 2, 3, 4]
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list
[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
str(my_list)
'[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]'
print(set(my_list))
{1, 2, 4, 6, 9}
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list.reverse
<built-in method reverse of list object at 0x000002492243FDC0>
my_list[::-1]
[9, 2, 6, 2, 4, 1, 4, 4, 2, 1]
li = [1,2,3,4,5]
resList = []
for v in li:
    resList.append(v**2)

    
li
[1, 2, 3, 4, 5]
resList
[1, 4, 9, 16, 25]

li = [1,2,3,4,5]
resList = [v**2 for v in li]
resList
[1, 4, 9, 16, 25]
li = [1,2,3,4,5,6]
resList = [v**2 for in li if v%2==0]
SyntaxError: invalid syntax
resList
[1, 4, 9, 16, 25]
numbers = [int(input("-->")) for i in range(int(input("-->")))]
-->
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    numbers = [int(input("-->")) for i in range(int(input("-->")))]
ValueError: invalid literal for int() with base 10: ''
>>> li
[1, 2, 3, 4, 5, 6]
>>> 
>>> 
>>> 
>>> li = [1,2,3,4]
>>> li[0]
1
>>> li[1]
2
>>> li = [[], [], []]
>>> li[0]
[]
>>> li[2]
[]
>>> li = [[1,2,3], [11,22,33], [0,5,8]]
>>> li[0]
[1, 2, 3]
>>> li[1]
[11, 22, 33]
>>> li[2]
[0, 5, 8]
>>> li[0][2]
3
>>> li[1][1]
22
>>> li = [[1,2,3], [11,22,33], [0,5,8]]
>>> li[0].append(333)
>>> li
[[1, 2, 3, 333], [11, 22, 33], [0, 5, 8]]
