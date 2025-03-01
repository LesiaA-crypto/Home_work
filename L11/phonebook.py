Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
try:
...     user1.call("123")
... except NumberError as e:
...     print(e)
... except:
...     print("-1")
... 
...     
... ('123', 'Короткий номер')
... class NumberError(Exception):
...     def __init__(self, number, message):
...         self.number = number
...         self.message = message
...     def __str__(self):
...         return f"NumberError: number: {self.number}, message: {self.message}"
... 
...     
... class User:
...     def __init__(self, name):
...         self.name = name
...               
...     def __str__(self):
...         return f"user name: {self.name}."
...     def call(self, number):
...         if len(number) < 8:
...             raise NumberError (number, "Короткий номер")
...         return f"звоню {number}"
... 
...     
... user1 = User("Vasia")
... try:
...     user1.call("123")
... except NumberError as e:
...     print(e)
... except:
...     print("-1")
... 
...     
... NumberError: number: 123, message: Короткий номер
