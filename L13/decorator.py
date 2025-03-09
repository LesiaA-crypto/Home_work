Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def decorator(func):
    print("Привет из декоратора")
    func()

    
def say():
    print("Как дела")

    
say()
Как дела
@decorator
def say():
    print("Как дела")

    
Привет из декоратора
Как дела
say()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    say()
TypeError: 'NoneType' object is not callable
def decorator(func):
    def inner():
        print("Привет из декоратора")
        func()
    return inner

decorator
<function decorator at 0x000002112CA87060>
@decorator
def say():
    print("Как дела")

    
say()
Привет из декоратора
Как дела
say()
Привет из декоратора
Как дела
say()
Привет из декоратора
Как дела
def decorator(func):
    print("Привет из декоратора")
    return func

@decorator
def say():
    print("Как дела")

    
Привет из декоратора
say()
Как дела
say()
Как дела
Привет из декоратора
SyntaxError: invalid syntax
def decorator(func):
    def inner():
        print("Привет из декоратора")
        func()
    return inner

@decorator
def say():
    print("Как дела")

...     
>>> say()
Привет из декоратора
Как дела
>>> say()
Привет из декоратора
Как дела
>>> @decorator
... def bye():
...     print("Пока")
... 
...     
>>> bye()
Привет из декоратора
Пока
>>> say()
Привет из декоратора
Как дела
>>> def say(name):
...     print(f'{name}, Как дела')
... 
...     
>>> def decorator(func):
...     def inner(dname):
...         print("Привет из декоратора")
...         func(dname)
...     return inner
... 
>>> @decorator
... def say(name):
...     print(f'{name}, Как дела')
... 
...     
>>> say('Petya')
Привет из декоратора
Petya, Как дела
