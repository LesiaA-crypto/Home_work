Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Dog:
...     pass
... 
>>> d1 = Dog()
>>> d2 = Dog()
>>> d3 = Dog()
>>> 
>>> class Dog:
...     inst_cont = False
...     def __init__(self, name):
...         if Dog.inst_cont == False:
...             self.name = name
...             Dog.inst_cont = True
...         else:
...             raise Exception("собака это синглтон.")
... 
...         
>>> Dog.inst_cont
False
>>> d1 = Dog("Bobik")
>>> Dog.inst_cont
True
>>> d1.name
'Bobik'
