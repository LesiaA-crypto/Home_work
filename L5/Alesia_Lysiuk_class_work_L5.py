Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n = 10
users = []
user_apassword = input('pass:')
pass:12345
user_a_name = input('name:')
name:vasia
users.append([user_a_name, user_apassword],)
userssers
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    esers
NameError: name 'esers' is not defined. Did you mean: 'users'?
users
[['vasia', '12345']]
def register():
    user_a_name = input('name:')
    user_apassword = input ('pass:')
    users.append([user_a_name, user_apassword],)
    print('Done...')

    
register()
name:kolya
pass:123
Done...
users
[['vasia', '12345'], ['kolya', '123']]
n = 8
for i in range(n):
    register()

    
name:hjgjh
pass:125
Done...
name:jgjh
pass:155
Done...
name:,khgkl
pass:444
Done...
name:
pass:112
Done...
name:dfhh
pass:111
Done...
name:gdd
pass:255
Done...
name:gd
pass:55
Done...
name:gdd
pass:22
Done...
register()
name:
pass:
Done...

pass:444
SyntaxError: invalid syntax


def hello():
    print('Hello')

    
hello
<function hello at 0x000001B53F313F60>
hello()
Hello
def hello():
    user = input('your name:')
    print(f'Hello, {user}!')

    
hello{}
SyntaxError: invalid syntax
hello()
your name:anya
Hello, anya!
hello()
your name:mhv
Hello, mhv!
print()

def hello():
    user = input('your name:')
    print(f'Hello, {user}!')
    for i in range(3):
        print(i, end='')
    d = 88
    if d == 88:
        print('XXX')
    print(55666)

    
hello()
your name:jhgk
Hello, jhgk!
012XXX
55666
hello = 55
hello()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    hello()
TypeError: 'int' object is not callable
def hello (user):
    print ('Hello', user)

    
hello()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    hello()
TypeError: hello() missing 1 required positional argument: 'user'
hello(123)
Hello 123
def hello(a, b, c):
    print('Hello', a, b, c)

    
hello()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    hello()
TypeError: hello() missing 3 required positional arguments: 'a', 'b', and 'c'
hello (1, 2, 3)
Hello 1 2 3
def hello(a, b, c):
    print('Hello', a, b, c)

    
hello (b=5, c=7, a=8)
Hello 8 5 7
def hello (name, age):
    print('Hello', name, age)

    
hello("jkhghk", 28)
Hello jkhghk 28
def hello (name, age):
    print('Hello', name,'. Your age is', age)

    
hello("jhdj", 88)
Hello jhdj . Your age is 88

def create_order(name, pn, age, msg):
    print("Order 3333: created.")
    print(f"   Name:{name}")
    print(f"   Your phone:{ph}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    prunt()

    
create_order("Goose", 123)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    create_order("Goose", 123)
TypeError: create_order() missing 2 required positional arguments: 'age' and 'msg'
ef create_order(name, pn, age="", msg=""):
    print("Order 3333: created.")
    print(f"   Name:{name}")
    print(f"   Your phone:{ph}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    prunt()
    
SyntaxError: invalid syntax
def create_order(name, pn, age="", msg=""):
    print("Order 3333: created.")
    print(f"   Name:{name}")
    print(f"   Your phone:{ph}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    prunt()

    
create_order("Goose", 123)
Order 3333: created.
   Name:Goose
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    create_order("Goose", 123)
  File "<pyshell#87>", line 4, in create_order
    print(f"   Your phone:{ph}")
NameError: name 'ph' is not defined. Did you mean: 'pn'?
def create_order(name, pn, age="", msg=""):
    if len(name) < 2:
        return False
    if str(ph).isallnum() != True:
        return False
    print("Order 3333: created.")
    print("Order details:")
    print(f"   Name:{name}")
    print(f"   Your phone:{ph}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    print()
    return True

res = creste_order('a', 123123)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    res = creste_order('a', 123123)
NameError: name 'creste_order' is not defined. Did you mean: 'create_order'?
res = create_order('a', 123123)

res = create_order('Uan', 123123)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    res = create_order('Uan', 123123)
  File "<pyshell#101>", line 4, in create_order
    if str(ph).isallnum() != True:
NameError: name 'ph' is not defined. Did you mean: 'pn'?
def create_order(name, pn, age="", msg=""):
    if len(name) < 2:
        return False
    if str(ph).isallnum() != True:
        return False
    print("Order 3333: created.")
    print("Order details:")
    print(f"   Name:{name}")
    print(f"   Your phone:{pn}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    print()
    return True

res = create_order('a', 123123)

res = create_order('Uan', 123123)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    res = create_order('Uan', 123123)
  File "<pyshell#107>", line 4, in create_order
    if str(ph).isallnum() != True:
NameError: name 'ph' is not defined. Did you mean: 'pn'?
def create_order(name, pn, age="", msg=""):
    if len(name) < 2:
        return False
    if str(pn).isallnum() != True:
        return False
    print("Order 3333: created.")
    print("Order details:")
    print(f"   Name:{name}")
    print(f"   Your phone:{pn}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    print()
    return True

res = create_order('a', 123123)

res = create_order('Uan', 123123)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    res = create_order('Uan', 123123)
  File "<pyshell#112>", line 4, in create_order
    if str(pn).isallnum() != True:
AttributeError: 'str' object has no attribute 'isallnum'. Did you mean: 'isalnum'?
ef create_order(name, pn, age="", msg=""):
    if len(name) < 2:
        return False
    if str(pn).isalnum() != True:
        return False
    print("Order 3333: created.")
    print("Order details:")
    print(f"   Name:{name}")
    print(f"   Your phone:{pn}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    print()
    return True

res = create_order('a', 123123)
SyntaxError: invalid syntax
def create_order(name, pn, age="", msg=""):
    if len(name) < 2:
        return False
    if str(pn).isalnum() != True:
        return False
    print("Order 3333: created.")
    print("Order details:")
    print(f"   Name:{name}")
    print(f"   Your phone:{pn}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    print()
    return True

res = create_order('a', 123123)
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
res = create_order('Uan', 123123)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    res = create_order('Uan', 123123)
  File "<pyshell#112>", line 4, in create_order
    if str(pn).isallnum() != True:
AttributeError: 'str' object has no attribute 'isallnum'. Did you mean: 'isalnum'?
sss()
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    sss()
NameError: name 'sss' is not defined

def numbers(num):
    if num % 2 == 0:
        return True
    return None

numbers(2)
True
numbers()
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    numbers()
TypeError: numbers() missing 1 required positional argument: 'num'
numbers(3)
numbers(3))
SyntaxError: unmatched ')'
numbers(3)
>>> print(numbers(3))
None
>>> def numbers(num):
...     if num % 2 == 0:
...         return True
... 
...     
>>> 
>>> print(numbers(3))
None
>>> check("123456")
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    check("123456")
NameError: name 'check' is not defined
>>> INT
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    INT
NameError: name 'INT' is not defined. Did you mean: 'int'?
>>> def non(number):
...     if number > 20:
...         return True
...     return number + non(number+4)
... 1+5+9+13+17+ True
SyntaxError: invalid syntax
>>> 1 + 5 + 9 + 13 + 17 + True
46
>>> non(1)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    non(1)
NameError: name 'non' is not defined. Did you mean: 'None'?
