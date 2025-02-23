Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Dog:
    pass

class Lada:
    pass

class Wallet:
    pass

class Dog:
    def __init__(self, name, age):
        self.name = name
        selg.age = age

        
d = Dog()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d = Dog()
TypeError: Dog.__init__() missing 2 required positional arguments: 'name' and 'age'
d = Dog("Bobic", 34)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d = Dog("Bobic", 34)
  File "<pyshell#10>", line 4, in __init__
    selg.age = age
NameError: name 'selg' is not defined. Did you mean: 'self'?
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
d = Dog("Bobic", 34)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        
dima = User("Dima", "dima@fds.com")
type(dima)
<class '__main__.User'>
type(d)
<class '__main__.Dog'>
isinstance(dima, User)
True
isinstance(dima, Dog)
False
dima.name
'Dima'
dima.email
'dima@fds.com'
d.age
34
d.name
'Bobic'
dima = User('Dima', "dima@fds.com")
vova = User('Vova', "jhhhhgkj.com")
SyntaxError: multiple statements found while compiling a single statement
dima = User('Dima', "dima@fds.com")
vova = User('Vova', "jhhhhgkj.com")
class User:
    users couter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
SyntaxError: invalid syntax
class User:
    users counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
SyntaxError: invalid syntax
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email

        
User.users_counter
0
User.users_counter = 666
User.users_counter
666
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.users_counter += 1

        
User.users_counter
0
dima = User("Di", "@")
User.users_counter
1
vika = User("Vi", "@")
User.users_counter
2
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.users_counter += 1

        
d = User("Di", "@")
v = User("Vi", "@")
c = User("Ci", "@")
User.users_counter
3
User.users_counter = 555
User.users_counter
555
d.users_counter
555
v.users_counter
555
class Wallet:
    """Представляет структуру полей для описания кошелька."""
    def __init__(self, owner, currency, amount, address="", color="silver"):
        self.owner = owner
        self.currency = currency
        self.amount = amount
        self.adress = address
        self.color = color
        Wallet.counter += 1
        self.wallet_id = Wallet.counter * 10

        
Wallet.counter
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    Wallet.counter
AttributeError: type object 'Wallet' has no attribute 'counter'
class Wallet:
    """Представляет структуру полей для описания кошелька."""
    def __init__(self, owner, currency, amount, address="", color="silver"):
        self.owner = owner
        self.currency = currency
        self.amount = amount
        self.adress = address
        self.color = color
        Wallet.counter += 1
        self.wallet_id = Wallet.counter * 10

        
class Wallet:
    """Представляет структуру полей для описания кошелька."""
    counter = 0
    def __init__(self, owner, currency, amount, address="", color="silver"):
        self.owner = owner
        self.currency = currency
        self.amount = amount
        self.adress = address
        self.color = color
        Wallet.counter += 1
        self.wallet_id = Wallet.counter * 10

        
Wallet.counter
0
fw = Wallet("s f", "byn", 1000)
Wallet.counter
1
fw.owner
's f'
fw.currency
'byn'
fw.address
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    fw.address
AttributeError: 'Wallet' object has no attribute 'address'. Did you mean: 'adress'?
fw.adress
''
fw.color
'silver'
fw.wallet_id
10
sw = Wallet("d f", "byn", 1000)
sw = Wallet("d f", "rub", 1000)
sw
<__main__.Wallet object at 0x000002B7F884ED20>
Wallet.__doc__
'Представляет структуру полей для описания кошелька.'
Wallet.__name__
'Wallet'
Wallet.__bases__
(<class 'object'>,)
fw.__dict__
{'owner': 's f', 'currency': 'byn', 'amount': 1000, 'adress': '', 'color': 'silver', 'wallet_id': 10}
for k, v in fw.__dict__.items():
    print(k, ":", v)

    
owner : s f
currency : byn
amount : 1000
adress : 
color : silver
wallet_id : 10
for k, v in sw.__dict__.items():
    print(k, ":", v)

    
owner : d f
currency : rub
amount : 1000
adress : 
color : silver
wallet_id : 30

class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f"{self.name} says {message}!")

        
d1 = User("Dima", "@")
d1.name
'Dima'
d1.email
'@'
d1.hello
<bound method User.hello of <__main__.User object at 0x000002B7F884F3E0>>
print
<built-in function print>
d1.hello
<bound method User.hello of <__main__.User object at 0x000002B7F884F3E0>>
d1.hello("hello there")
Dima says hello there!
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f"{self.name} says {message}!")
    def bye(self):
        print(f"{self.name} says bye bye!")

        
d1 = User("Dima", "@")
d1.hello("hhhhh")
Dima says hhhhh!
d1.bye
<bound method User.bye of <__main__.User object at 0x000002B7F884EBD0>>
d1.bye()
Dima says bye bye!
st = "hello"
print(st)
hello
print(d1)
<__main__.User object at 0x000002B7F884EBD0>
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f"{self.name} says {message}!")
    def bye(self):
        print(f"{self.name} says bye bye!")
    def __str__(self):
        return f"User: name-{self.name}, email-{self.email}."

kate = User("Kate", "kate123@gmail.com")
kate.hello("mjhgkj")
Kate says mjhgkj!
kate.bye()
Kate says bye bye!
print(kate)
User: name-Kate, email-kate123@gmail.com.
dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
dir(User)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bye', 'hello', 'users_counter']
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f"{self.name} says {message}!")
    def bye(self):
        print(f"{self.name} says bye bye!")
    def __str__(self):
        return f"User: name-{self.name}, email-{self.email}."

    
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({counter_id:user})
    def show_all(self):
        for user_id, user in self.storage.items():
            print(f"User id:{user_id}")
            print(f"    Name:{user.name}")
            print(f"    Email:{user.email}")
            print(user)
            print(user.bye{})
            
SyntaxError: invalid syntax. Perhaps you forgot a comma?
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({counter_id:user})
    def show_all(self):
        for user_id, user in self.storage.items():
            print(f"User id:{user_id}")
            print(f"    Name:{user.name}")
            print(f"    Email:{user.email}")
            print("__str__")
            print(user)
            print(user.bye{})
            
SyntaxError: invalid syntax. Perhaps you forgot a comma?
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({Storage.counter_id:user})
    def show_all(self):
        for user_id, user in self.storage.items():
            print(f"User id:{user_id}")
            print(f"    Name:{user.name}")
            print(f"    Email:{user.email}")
            print("__str__")
            print(user)
            print(user.bye{})
            
SyntaxError: invalid syntax. Perhaps you forgot a comma?
KeyboardInterrupt
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({Storage.counter_id:user})
    def show_all(self):
        for user_id, user in self.storage.items():
            print(f"User id:{user_id}")
            print(f"    Name:{user.name}")
            print(f"    Email:{user.email}")
            print("__str__")
            print(user)
            print(user, bye{})
            
SyntaxError: invalid syntax. Perhaps you forgot a comma?
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({Storage.counter_id:user})
    def show_all(self):
        for user_id, user in self.storage.items():
            print(f"User id:{user_id}")
            print(f"    Name:{user.name}")
            print(f"    Email:{user.email}")
            print("__str__")
            print(user)
            print(user.bye(""))

            
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({Storage.counter_id:user})
    def show_all(self):
        for user_id, user in self.storage.items():
            print(f"User id:{user_id}")
            print(f"    Name:{user.name}")
            print(f"    Email:{user.email}")
            print("__str__")
            print(user)
            print(user.bye())

            
strg = Storage()
dima = User("Dima", "hgfjh")
kate = User("Vasia", "hfdjh")
strg.add_user(dima)
strg.add_user(kate)
strg.add_user(vasia)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    strg.add_user(vasia)
NameError: name 'vasia' is not defined
vasia = User("Vasia1", "hfdjh")
strg.add_user(vasia)
strg.show_all()
User id:1
    Name:Dima
    Email:hgfjh
__str__
User: name-Dima, email-hgfjh.
Dima says bye bye!
None
User id:2
    Name:Vasia
    Email:hfdjh
__str__
User: name-Vasia, email-hfdjh.
Vasia says bye bye!
None
User id:3
    Name:Vasia1
    Email:hfdjh
__str__
User: name-Vasia1, email-hfdjh.
Vasia1 says bye bye!
None

class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__(self):
        return "привет из родительского класса."

    
class Sedan:
    pass

class Wagon:
    pass
Sedan.__bases__
SyntaxError: invalid syntax
Sedan.__bases__
(<class 'object'>,)
s = Sedan()
s
<__main__.Sedan object at 0x000002B7F884F5F0>
class Sedan(Car):
    pass

class Wagon(Car):
    pass

Sedan.__bases__
(<class '__main__.Car'>,)
Wagon.__bases__
(<class '__main__.Car'>,)
s = Sedan("1255", 1.7, "Megane")
print(s)
привет из родительского класса.
isinstance(s, Sedan)
True
isinstance(s, Car)
True
class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__(self):
        return "привет из родительского класса."
    def drive(self):
        print("VRUM VRUM VRUM")

        
class Sedan(Car):
    pass

class Wagon(Car):
    pass

w = Wagon(125588, 1.9, 21022)
w.__dict__
{'vin': 125588, 'volume': 1.9, 'model_name': 21022}
Sedan.__dict__
mappingproxy({'__module__': '__main__', '__doc__': None})
Car.__dict__
mappingproxy({'__module__': '__main__', '__init__': <function Car.__init__ at 0x000002B7F8871B20>, '__str__': <function Car.__str__ at 0x000002B7F88719E0>, 'drive': <function Car.drive at 0x000002B7F8871940>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
class Sedan(Car):
    def drive(self):
        print("Sedan delaet iiiii")

        
s = Sedan(1111, 3.3, "jgfkj")
s.drive()
Sedan delaet iiiii
class Wagon(Car):
    pass

w = Wagon(1236, 1.9, 21022)
w.drive()
VRUM VRUM VRUM


class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__(self):
        return "привет из родительского класса."
    def drive(self):
        print("VRUM VRUM VRUM")

        
class Wagon(Car):
    pass

class Sedan(Car):
    def drive(self):
        print("Sedan delaet iiiii")

        
class Sedan(Car):
    def drive(self):
        super().drive()
        print("Sedan delaet iiiii")

        
w = Wagon(1236, 1.9, 21022)
s = Sedan(1111, 3.3, "jgfkj")
w.drive()
VRUM VRUM VRUM
s.drive()
VRUM VRUM VRUM
Sedan delaet iiiii


class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__(self):
        return "привет из родительского класса."
    def drive(self):
        print("VRUM VRUM VRUM")
    def show_car(self):
        print(self.vin, self.volume, self.model_name)

        
class Sedan(Car):
    def __init__(self):
        self.body_type = "Sedan"
    def drive(self):
        super().drive()
        print("Sedan delaet iiii")

        

s = Sedan(1111, 3.3, "jgfkj")
Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    s = Sedan(1111, 3.3, "jgfkj")
TypeError: Sedan.__init__() takes 1 positional argument but 4 were given
>>> class Car:
...     def __init__(self, vin, volume, model_name):
...         self.vin = vin
...         self.volume = volume
...         self.model_name = model_name
...     def __str__(self):
...         return "привет из родительского класса."
...     def drive(self):
...         print("VRUM VRUM VRUM")
...     def show_car(self):
...         print(self.vin, self.volume, self.model_name)
... 
...         
>>> class Sedan(Car):
...     def __init__(self):
...         self.body_type = "Sedan"
...     def drive(self):
...         super().drive()
...         print("Sedan delaet iiii")
... 
...         
>>> s = Sedan(1111, 3.3, "jgfkj")
Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    s = Sedan(1111, 3.3, "jgfkj")
TypeError: Sedan.__init__() takes 1 positional argument but 4 were given
>>> s.body_type
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    s.body_type
AttributeError: 'Sedan' object has no attribute 'body_type'
