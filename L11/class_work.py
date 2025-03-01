Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class User:
    __counter = 0
    def __init__(self, name):
        self.name = name
        User.__counter += 1
    @classmethod
    def get_counter(cls):
        return cls.__counter
    def __str__(self):
        return f"user name: {self.name}."

    
User.get_counter
<bound method User.get_counter of <class '__main__.User'>>
User.get_counter()
0
k = User("Kate")
print(k)
user name: Kate.
k.get_counter()
1
User.get_counter()
1
User_counter
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    User_counter
NameError: name 'User_counter' is not defined
class User:
    __counter = 0
    
    def __init__(self, name):
        self.name = name
        User.__counter += 1
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
    @classmethod
    def set_counter = value
    
    def __str__(self):
        return f"user name: {self.name}."
    
SyntaxError: expected '('
class User:
    __counter = 0
    
    def __init__(self, name):
        self.name = name
        User.__counter += 1
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value
    
    def __str__(self):
        return f"user name: {self.name}."

    
k = User("Kate")
print(k)
user name: Kate.
User.get_counter
<bound method User.get_counter of <class '__main__.User'>>
User.set_counter
<bound method User.set_counter of <class '__main__.User'>>
User.get_counter()
1
User.get_counter(55)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    User.get_counter(55)
TypeError: User.get_counter() takes 1 positional argument but 2 were given


class User:
    __counter = 0
    
    def __init__(self, name):
        self.name = name
        User.__counter += 1
        
    def __str__(self):
        return f"user name: {self.name}."
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
    
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value

        
class User:
    __counter = 0
    
    def __init__(self, name):
        self.name = name
        User.__counter += 1
        
    def __str__(self):
        return f"user name: {self.name}."
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
    
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value

        
class User:
    __counter = 0
    
    def __init__(self, name):
        self.name = name
        User.__counter += 1
        
    def __str__(self):
        return f"user name: {self.name}."
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
    
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value
        
    @staticmethod
    def check_name(name):
        return False if len(name) < 2 else True

    
user1 = "Kate"
if User.check_name(user1):
    inst1 = User(user1)
else:
    print("Имя слишком короткое.")

    
print(inst1)
user name: Kate.
user name: Kate.
SyntaxError: invalid syntax
user2 = "O"
if User.check_name(user1):
    inst1 = User(user1)
else:
    print("Имя слишком короткое.")

    
user2 = "O"
if User.check_name(user2):
    inst1 = User(user2)
else:
    print("Имя слишком короткое.")
    
SyntaxError: multiple statements found while compiling a single statement
user2 = "O"
if User.check_name(user2):
    inst2 = User(user2)
else:
    print("Имя слишком короткое.")
    
SyntaxError: multiple statements found while compiling a single statement
user2 = "O"
if User.check_name(user2):
    inst2 = User(user2)
else:
    print("Имя слишком короткое.")

    
Имя слишком короткое.


class User:
    __counter = 0
    
    def __init__(self, name):
        self.name = name
        User.__counter += 1
        
    def __str__(self):
        return f"user name: {self.name}."
        
    @classmethod
    def init_age_including(cls, name, age):
        print("alt __init__")
        user = cls(name)
        user.age = age
        return user
    def __str__(self):
        return f"user name: {self.name}."
            
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value
        
    @staticmethod
    def check_name(name):
        return False if len(name) < 2 else True

    
u1 = User("Vova")
__init__
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    __init__
NameError: name '__init__' is not defined
u1 = User("Vova")
__init__
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    __init__
NameError: name '__init__' is not defined

# txt csv json xml

# prep export status
class ExportToTXT:
    # Петя делает свою таску.
    def __init__(self, file_name):
        self.file_name = file_name
    def exp(self):
        print("export to txt", self.file_name)

        
class ExportToCSV:
    # Вася делает свою часть кода.
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to csv", self.file_name)
    def preparation(self):
        print("preparation")

        
class ExportToCSV:
    # Коля делает свою часть кода.
    def __init__(self, file_name):
        self.f_n = file_name
    def export333(self):
        print("export to csv", self.file_name)
    def preparation(self):
        print("preparation")
    def gotovka(self):
        print("preparation")
    def check_stts(self):
        
KeyboardInterrupt
class ExportToCSV:
    # Коля делает свою часть кода.
    def __init__(self, file_name):
        self.f_n = file_name
    def export333(self):
        print("export to csv", self.file_name)
    def preparation(self):
        print("preparation")
    def gotovka(self):
        print("preparation")
    def check_stts(self):
        print("status")

        
li = [ExportToTXT("1.txt"),ExportToCSV("1.txt")]
for i in li:
    inst.expotr()

    
Traceback (most recent call last):

  File "<pyshell#90>", line 2, in <module>
    inst.expotr()
NameError: name 'inst' is not defined. Did you mean: 'inst1'?
# txt csv json xml
# prep export status
from abc import ABC, abstractmethod
class Export(ABC):
    @abstractmethod
    def export(self):
        pass
    @abstractmethod
    def prep(self):
        pass
    @abstractmethod
    def status(self):
        pass

    
class ExportToTXT:
    # Петя делает свою таску.
    def __init__(self, file_name):
        self.file_name = file_name
    def exp(self):
        print("export to txt", self.file_name)

        
inst = ExportToTXT("ggfdk")

class ExportToTXT:
    # Петя делает свою таску.
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to txt", self.file_name)
    def prep(self):
        print("prep")
    def status(self):
        print("status")

        
li = [ExportToTXT("1.txt"), ExportToTXT("2.txt"), ExportToJSON("n1.json")]
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    li = [ExportToTXT("1.txt"), ExportToTXT("2.txt"), ExportToJSON("n1.json")]
NameError: name 'ExportToJSON' is not defined. Did you mean: 'ExportToCSV'?
class ExportToJSON:
    # Петя делает свою таску.
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to txt", self.file_name)
    def prep(self):
        print("prep")
    def status(self):
        print("status")

        
li = [ExportToTXT("1.txt"), ExportToJSON("n1.json")]
for inst in li:
    inst.export()

    
export to txt 1.txt
export to txt n1.json

class A
SyntaxError: expected ':'
class A:
    pass

class B(A):
    pass

class C(B):
    pass

KeyboardInterrupt
class A:
    pass

class B(A):
    pass

class C(B):
    pass
SyntaxError: invalid syntax
class A:
    pass

class B(A):
    pass

class C(B):
    pass

C.__mro__
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
C.mro()
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

class A:
    a = 10

    
class B(A):
    b = 100

    
class C(B):
    c = 1000

    
c = C()
c1 = C()
c1.c
1000
c1.b
100
c1.a
10
c1.d
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    c1.d
AttributeError: 'C' object has no attribute 'd'
class A:
    a = 10
    def __init__(self):
        aaa = 11

        
class B(A):
    a = 10
    def __init__(self):
        bbb = 111

        
class C(B):
    c = 10
    def __init__(self):
        ccc = 1111

        

class A:
    a = 10
    def __init__(self):
        aaa = 11

        
class B(A):
    b = 10
    def __init__(self):
        self.bbb = 111

        
class A:
    a = 10
    def __init__(self):
        self.aaa = 11

        
class C(B):
    c = 1000
    def __init__(self):
        self.ccc = 1111
        super().__init__()

        
c1 = C()
c1.c
1000
c1.ccc
1111
c1.b
10
c1.bbb
111

try:
    raise AttributeError
except:
    print("err")
else:
    print("ok")
finally:
    print("fin")

    
err
fin
try:
    1+1
except:
    print("err")
else:
    print("ok")
finally:
    print("fin")

    
2
ok
fin
def a(number):
    try:
        return number
    except:
        return number +1
    else:
        return number +2
    finally number ** 10
    
SyntaxError: expected ':'
def a(number):
    try:
        return number
    except:
        return number +1
    else:
        return number +2
    finally:
        return number ** 10

    
a(10)
10000000000
def a(number):
    try:
        return number
    except:
        return number +1
    else:
        return number +2

    
a(10)
10
class User:
    def __init__(self, name):
        self.name = name
        User.__counter += 1
     def __str__(self):
         
SyntaxError: unindent does not match any outer indentation level
class User:
    def __init__(self, name):
        self.name = name
        User.__counter += 1
     def __str__(self):
         
SyntaxError: unindent does not match any outer indentation level
class User:
    def __init__(self, name):
        self.name = name
        User.__counter += 1
        
    def __str__(self):
        return f"user name: {self.name}."

    
class User:
    def __init__(self, name):
        self.name = name
              
    def __str__(self):
        return f"user name: {self.name}."
    def call(self, number):
        if len(number) < 8:
            pass
        return f"звоню {number}"

    
class NumberError(Exception):
    def __init__(self, number, message):
        self.number = number
        self.message = message

        
raise NumberError(12312, "Короткий номер!")
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    raise NumberError(12312, "Короткий номер!")
NumberError: (12312, 'Короткий номер!')
class NumberError(Exception):
    def __init__(self, number, message):
        self.number = number
        self.message = message

        
class User:
    def __init__(self, name):
        self.name = name
              
    def __str__(self):
        return f"user name: {self.name}."
    def call(self, number):
        if len(number) < 8:
            raise NumberError (number, "Короткий номер")
        return f"звоню {number}"

    
user1 = User("Vasia")
user1.call(123)
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    user1.call(123)
  File "<pyshell#233>", line 8, in call
    if len(number) < 8:
TypeError: object of type 'int' has no len()
user.call("123")
Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    user.call("123")
NameError: name 'user' is not defined. Did you mean: 'User'?
try:
    user1call(""1234)
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
try:
    user1.call("123")
except NumberError as e:
    print(e)
except:
    print("-1")

    
('123', 'Короткий номер')
>>> class NumberError(Exception):
...     def __init__(self, number, message):
...         self.number = number
...         self.message = message
...     def __str__(self):
...         return f"NumberError: number: {self.number}, message: {self.message}"
... 
...     
>>> class User:
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
>>> user1 = User("Vasia")
>>> try:
...     user1.call("123")
... except NumberError as e:
...     print(e)
... except:
...     print("-1")
... 
...     
NumberError: number: 123, message: Короткий номер
