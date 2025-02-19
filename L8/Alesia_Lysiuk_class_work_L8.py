Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
s = "jfhjdf"
s.capitalize()
'Jfhjdf'
s.casefold()
'jfhjdf'
s.decapitalize()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s.decapitalize()
AttributeError: 'str' object has no attribute 'decapitalize'. Did you mean: 'capitalize'?
li = [1,2,3]
li[0.5]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    li[0.5]
TypeError: list indices must be integers or slices, not float
1/0
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
try:
    1/0
except:
    print("Privet")

    
Privet
try:
    li = [1,2,3]
    li[0.5]
except:
    print("Privet")

    
Privet

try:
    int("-2222/*1/0"
except:
    print("Privet")
    
SyntaxError: '(' was never closed

try:
    int("-2222/*1/0")
except:
    print("Privet")

    
Privet
try:
    1/0
except ValueError:
    print("ValueError")
except:
    print(-1)

    
-1
try:
    1/0
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")

    
ZeroDivisionError

try:
    
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
except:
    
SyntaxError: expected an indented block after 'try' statement on line 1
try:
    li[0.5]
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
except:
    print("hhhhh")

    
hhhhh
try:
    13/0
except ZeroDivisionError as zde:
    print("ZeroDivisionError x/0", zde.args)
except ValueError as ve:
    print("ValueError", ve.args)
except:
    print(-1)

    
ZeroDivisionError x/0 ('division by zero',)
try:
    raise ValueError
except ZeroDivisionError as zde:
    print("ZeroDivisionError x/0", zde.args)
except ValueError as ve:
    print("ValueError", ve.args)
except:
    print(-1)

    
ValueError ()
try:
    raise ZeroDivisionError
except ZeroDivisionError as zde:
    print("ZeroDivisionError x/0", zde.args)
except ValueError as ve:
    print("ValueError", ve.args)
except:
    print(-1)

    
ZeroDivisionError x/0 ()
raise IndexError
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    raise IndexError
IndexError
try:
    123/0
except (ZeroDivisionError, ValueError):
    print("ZeroDivisionError or ValueError")
except:
    print(-1)

    
ZeroDivisionError or ValueError
a = 8
if a == 8:
    try:
        import time
    except:
        pass
else:
    print("делай без тайм")

    

try:
    raise ZeroDivisionError # 1/0
except("defoult")
SyntaxError: expected ':'

try:
    raise ZeroDivisionError # 1/0
except:
    print("defoult")

    
defoult
try:
    raise ZeroDivisionError # 1/0
except ArithmeticError:
    print("ArithmeticError")
except ZeroDivisionError:
    print ("ZeroDivisionError")
except:
    print("defoult")

    
ArithmeticError

try:
    raise IndexError # 1/0
except IndexError as i :
    print("i.arg")
except:
    print("defoult")

    
i.arg
def a(x):
    try:
        res = int(x)
    except:
        print("123")

        
a(123)
a("jfh@kj")
123

def a(x):
    try:
        res = int(x)
    except:
        print("123")
        raise

    
a(123)
a("jgfgf")
123
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a("jgfgf")
  File "<pyshell#82>", line 3, in a
    res = int(x)
ValueError: invalid literal for int() with base 10: 'jgfgf'
+
SyntaxError: invalid syntax

assert 1
assert 0
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    assert 0
AssertionError
>>> assert []
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    assert []
AssertionError
>>> assert "fhf"
>>> assert [1,2,3]
>>> assert None
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    assert None
AssertionError
>>> res = 10
>>> assert res == 10
>>> 
>>> res = 10
... assert res == 10
SyntaxError: multiple statements found while compiling a single statement
>>> res = 10
>>> assert res == 10
>>> res = 11
>>> assert res == 10
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    assert res == 10
AssertionError
>>> [DEBUG ON]
>>> [DEBUG OFF]
