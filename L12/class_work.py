Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print()

print(1,2,3)
1 2 3
def Pront(values):
    fot val in vals:
        
SyntaxError: invalid syntax
def Pront(values):
    for val in vals:
        print(val, end="")
        print()

        
Pront([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Pront([1,2,3,4])
  File "<pyshell#7>", line 2, in Pront
    for val in vals:
NameError: name 'vals' is not defined. Did you mean: 'val'?
def Pront(*values):
    for val in vals:
        print(val, end="")
        print()

        
Pront(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    Pront(1,2,3,4,5)
  File "<pyshell#10>", line 2, in Pront
    for val in vals:
NameError: name 'vals' is not defined. Did you mean: 'val'?
def balances(**balance)
SyntaxError: expected ':'
def balances(**balance):
    print(balance)
    print(type(balance))
    for k, w in balance.items():
        print("\t", k, ":", w)
        print()

        
balances(1,2,3,4,4)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    balances(1,2,3,4,4)
TypeError: balances() takes 0 positional arguments but 5 were given
balances(name="Vasia", cash=12000)
{'name': 'Vasia', 'cash': 12000}
<class 'dict'>
	 name : Vasia

	 cash : 12000

def numbers(name="Jo", *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

    
numbers()
Jo
()
{}
numbers("Vova", 1,2,3,4,6, "jhgjhg", age=100, apples=99)
Vova
(1, 2, 3, 4, 6, 'jhgjhg')
{'age': 100, 'apples': 99}

def num_sum(*args):
    s = 0
    for i in args:
        s+= i
        print(s)

        
def numbers(*args, **kwargs):
    print(args)
    print(kwargs)
    num_sum(args)

    
numbers(1,2,)
(1, 2)
{}
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    numbers(1,2,)
  File "<pyshell#40>", line 4, in numbers
    num_sum(args)
  File "<pyshell#35>", line 4, in num_sum
    s+= i
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
3
def num_sum(*args):
    print(args)
    s = 0
    for i in args:
        s+= i
        print(s)

        
def numbers(*args, **kwargs):
    print(args)
    print(kwargs)
    num_sum(args)

    
numbers(1,2,)
(1, 2)
{}
((1, 2),)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    numbers(1,2,)
  File "<pyshell#45>", line 4, in numbers
    num_sum(args)
  File "<pyshell#43>", line 5, in num_sum
    s+= i
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
def numbers(*args, **kwargs):
    print(args)
    print(kwargs)
    num_sum(*args)

    
numbers(1,2,)
(1, 2)
{}
(1, 2)
1
3

li1, li2 = [1,2,3], [4,5,6]
li1
[1, 2, 3]
li2
[4, 5, 6]
li3 = li1+li2
li3
[1, 2, 3, 4, 5, 6]
li3 = [*li1, *li2]
li3
[1, 2, 3, 4, 5, 6]
st = [khg]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    st = [khg]
NameError: name 'khg' is not defined
st = ["kfhg"]
st
['kfhg']
li = [*st]
li
['kfhg']
li
['kfhg']
di = {"1":2, "2":3}
di = {"11":22, "22":33}
di1 = {"1":2, "2":3}
di3 = {**di, **di1}
di3
{'11': 22, '22': 33, '1': 2, '2': 3}
*ttt, = "gjg"
ttt
['g', 'j', 'g']
a, *ttt = "hhh"
a
'h'
ttt
['h', 'h']



def D(b, a, c):
    return b**2 - 4*a*c

D
<function D at 0x000001E940C439C0>
# def cond(z,x,y, b,a,c):

  
lambda: 2
<function <lambda> at 0x000001E940C40A40>
def retTwo():
    return 2

retTwo()
2
(lambda: 2)()
2
(lambda: 2)
<function <lambda> at 0x000001E940C43B00>


li - [2,3,4,5]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    li - [2,3,4,5]
TypeError: unsupported operand type(s) for -: 'list' and 'list'
li = [2,3,4,5]
for i in li:
    print(i)

    
2
3
4
5
li_iter = iter()li
SyntaxError: invalid syntax
li_iter = iter(li)
next(li_iter)
2
next(li_iter)
3
next(li_iter)
4
next(li_iter)
5
next(li_iter)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    next(li_iter)
StopIteration


class powFive:
    def __init__(self, maxn):
    self.maxn = maxn
    
SyntaxError: expected an indented block after function definition on line 2
class powFive:
    def __init__(self, maxn):
        self.maxn = maxn

        
class PowFive:
    def __init__(self, maxn):
        self.maxn = maxn
    def __iter__(self):
        self.counter = 1
        return self
    def __next__(self):
        if self.counter <= self.maxn:
            res = 5 ** self.counter
            self.counter += 1
            return res
        raise StopIteration

    
p = PowFive(15)
p
<__main__.PowFive object at 0x000001E940C1E060>
p = PowFive(4)
for i in p:
    print(i)

    
5
25
125
625
li = [i**2 for i in range (10)]
li
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
gen = (i**2 for i in range (10))
gen
<generator object <genexpr> at 0x000001E940BFD630>
for val in gen:
    print(val)

    
0
1
4
9
16
25
36
49
64
81
for val in gen:
    print(val)

    
gen = (i**2 for i in range (10))
next(gen)
0

next(gen)
1
next(gen)
4
next(gen)
9
next(gen)
16
next(gen)
25
next(gen)
36
next(gen)
49
next(gen)
64
next(gen)
81
next(gen)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    next(gen)
StopIteration
gen = (i**2 for i in range (10))

li = [i**2 for i in gen]
li
[0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561]
next(gen)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    next(gen)
StopIteration


def retNumbers(n):
    for i in range(n):
        return i

    
refNumbers(5)
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    refNumbers(5)
NameError: name 'refNumbers' is not defined. Did you mean: 'retNumbers'?
retNumbers(5)
0
retNumbers(5)
0
def retNumbers(n):
    for i in range(n):
        yield i**2

        
r = retNumbers(5)
r
<generator object retNumbers at 0x000001E940BFD560>
next(r)
0
next(r)
1
next(r)
4
next(r)
9
next(r)
16
next(r)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    next(r)
StopIteration


def a():
    x =10

    
def a():
    x =10
    def inner(number):
        retyrn number**x
        
SyntaxError: invalid syntax
def a():
    x =10
    def inner(number):
        return number**x
    return inner

res = a()
res
<function a.<locals>.inner at 0x000001E940C42700>
res(6)
60466176
def numPowTwo():
    num = 0

    
def numPowTwo():
    num = 0
    def inner():
        nonlocal num
        num *= 2
        return num
    return inner

res = numPowTwo()
res
<function numPowTwo.<locals>.inner at 0x000001E940C407C0>
res()
0
def numPowTwo():
    num = 2
    def inner():
        nonlocal num
        num *= 2
        return num
    return inner

res = numPowTwo()
res
<function numPowTwo.<locals>.inner at 0x000001E940C40860>
res()
4
res()
8
res()
16
res()
32
res()
64
res()
128
res()
256
res()
512
res()
1024
res()
2048
res()
4096
res()
8192
res()
16384
res()
32768
res()
65536
res()
131072
res()
262144
res()
524288
res()
1048576
res()
2097152
res()
4194304
res()
8388608
res()
16777216
res()
33554432
>>> res()
67108864
>>> res()
134217728
>>> res()
268435456
>>> res()
536870912
>>> res()
1073741824
>>> res()
2147483648
>>> res()
4294967296
>>> res()
8589934592
>>> res()
17179869184
>>> res()
34359738368
>>> res()
68719476736
>>> res()
137438953472
>>> res()
274877906944
>>> res()
549755813888
>>> res()
1099511627776
>>> res()
2199023255552
>>> 
>>> 
