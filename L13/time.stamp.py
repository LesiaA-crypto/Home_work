Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import datetime
datetime.datetime.now()
datetime.datetime(2025, 3, 9, 19, 42, 41, 48782)
datetime.datetime.now()
datetime.datetime(2025, 3, 9, 19, 42, 56, 639424)
say.__name__
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    say.__name__
NameError: name 'say' is not defined
print(datetime.datetime.now())
2025-03-09 19:45:10.838036
def decorator(func):
    def inner(dname):
        print('Привет из декоратора')
        print('Время запуска', datetime.datetime.now()))
        
SyntaxError: unmatched ')'
def decorator(func):
    def inner(dname):
        print('Привет из декоратора')
        print('Время запуска', datetime.datetime.now())
        print('Имя функции которая запускается:', func.__name__)
        func(dname)
        return inner

    
@decorator
def say(f'{name}, Как дела')
SyntaxError: invalid syntax
def say():
    print("Как дела")

    
>>> @decorator
... def say(f'{name}, Как дела')
SyntaxError: invalid syntax
>>> @decorator
... def say():
...     print("Как дела")
... 
...     
>>> def say(f'{name}, Как дела')
SyntaxError: invalid syntax
>>> @decorator
... def say(name):
...     print((f'{name}, Как дела'))
... 
...     
>>> @decorator
... def bye(name):
...     print(f'{name}, Пока')
... 
...     
>>> say('Petya')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    say('Petya')
TypeError: 'NoneType' object is not callable
>>> @decorator
... def bye(name):
...     print(f'{name}, Пока')
... 
...     
>>> bye('Petya')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    bye('Petya')
TypeError: 'NoneType' object is not callable
