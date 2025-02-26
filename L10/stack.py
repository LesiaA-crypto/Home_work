Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
stack = []
def push(value):
   stack.append(value)

   
def pop():
    stack.pop()

    
push(1)
push(2)
push(3)
stack
[1, 2, 3]
pop()
stack
[1, 2]
pop()
stack
[1]

class Stack:
    pass

SyntaxError: multiple statements found while compiling a single statement
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, volue):
        self.stack.append(value)
    def pop(self):
        self.stack.pop()

        
s1 = Stack ()
s1.push(1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s1.push(1)
  File "<pyshell#2>", line 5, in push
    self.stack.append(value)
NameError: name 'value' is not defined. Did you mean: 'volue'?
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        self.stack.pop()

        
s1 = Stack ()
s1.push(1)
s1.push(2)
s1.push(3)
s1.Stack
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s1.Stack
AttributeError: 'Stack' object has no attribute 'Stack'. Did you mean: 'stack'?
s1.stack
[1, 2, 3]
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        try:
            self.stack.pop()
        except:
            return "NE OK"
        return "ok"
    def show(self):
        return self.__stack

    
s1 = Stack ()
s1.pop(1)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s1.pop(1)
TypeError: Stack.pop() takes 1 positional argument but 2 were given
s1.pop()
'NE OK'
s1.push(123)
s1.push(1)
s1.push(2)
s1.push(3)
s1.show()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s1.show()
  File "<pyshell#19>", line 13, in show
    return self.__stack
AttributeError: 'Stack' object has no attribute '_Stack__stack'
class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        try:
            self.stack.pop()
        except:
            return "NE OK"
        return "ok"
    def show(self):
        return self.__stack

...     
>>> s1.show()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s1.show()
  File "<pyshell#19>", line 13, in show
    return self.__stack
AttributeError: 'Stack' object has no attribute '_Stack__stack'
>>> class Stack:
...     def __init__(self):
...         self.__stack = []
...     def push(self, value):
...         self.__stack.append(value)
...     def pop(self):
...         try:
...             self.__stack.pop()
...         except:
...             return "NE OK"
...         return "ok"
...     def show(self):
...         return self.__stack
... 
...     
>>> s1.show()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s1.show()
  File "<pyshell#19>", line 13, in show
    return self.__stack
AttributeError: 'Stack' object has no attribute '_Stack__stack'
>>> s1.pop()
'ok'
