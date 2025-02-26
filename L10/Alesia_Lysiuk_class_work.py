Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Car:
    def __init__(self, brand, vol):
        self.brand = brand
        self.volume = vol
    def __str__(self):
        return f"{self.brand}: {self.volume}"

    
my_car = Car("VAZ", 1.8)
prunt(my_car)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    prunt(my_car)
NameError: name 'prunt' is not defined. Did you mean: 'print'?
print(my_car)
VAZ: 1.8
class Car:
    def __init__(, brand, vol):
        
SyntaxError: invalid syntax
class Car:
    def __init__(kitty, brand, vol):
        kitty.brand = brand
        kitty.volume = vol
    def __str__(kitty):
        return f"{kitty.brand}: {kitty.volume}"

    
my_car = Car("VAZ", 1.8)
print(my_car)
VAZ: 1.8
class Car:
    def __init__(kitty, brand, vol):
        self.brand = brand
        self.volume = vol
    def __str__(kitty):
        return f"{kitty.brand}: {kitty.volume}"

    
class Car:
    def __init__(self, brand, vol):
        self.brand = brand
        self.volume = vol
    def __str__(self):
        return f"{self.brand}: {self.volume}"
    def __rept__(self):
        return f"rept - {self.brand}: {self.volume}"

    
my_car = Car("VAZ", 1.8)
my_new_car = Car("VAZ", 1.8)
print(my_new_car)
VAZ: 1.8


class Car:
    counter = 0
    def __init__(self, brand, vol):
        self.brand = brand
        self.volume = vol
    def __str__(self):
        return f"{self.brand}: {self.volume}"
    def __rept__(self):
        return f"Inst of Car:\n\tBrand:{self.brand}. \n\tVolume:{self.volume}"

    
Car.counter
0
class Car:
    counter = 0
    def __init__(self, brand, vol):
        self.brand = brand
        self.volume = vol
        Car.counter +=1
    def __str__(self):
        return f"{self.brand}: {self.volume}"
    def __rept__(self):
        return f"Inst of Car:\n\tBrand:{self.brand}. \n\tVolume:{self.volume}"

    
Car.counter
0
my_new_car = Car("ZAZ", 0.9)
Car.counter
1
my_new_car = Car("ZAZ", 0.9)
Car.counter
2
my_new_car = Car("ZAZ", 0.9)
Car.counter
3
my_new_car.counter
3


class Animal:
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def eat(self):
        print(f'Животное {self.color} цвета кушает...')
    def go(self):
        print("Животное двигается")
    def sleep(self):
        print("ZZZZZZ")

        
Car.__doc__
Car.__bases
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    Car.__bases
AttributeError: type object 'Car' has no attribute '__bases'
Car.__bases__
(<class 'object'>,)
class Empty():
    pass

e = Empty()
Empty.__bases__
(<class 'object'>,)
e
<__main__.Empty object at 0x000002ABF58A29F0>
my_new_car.__dict__
{'brand': 'ZAZ', 'volume': 0.9}


class Animal:
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def eat(self):
        print(f'Животное {self.color} цвета кушает...')
    def go(self):
        print("Животное двигается")
    def sleep(self):
        print("ZZZZZZ")

        
class DomesticCat(Animal):
    def __init__(self, name, color, age):
        self.name = name
        super().__init__(color, age)

        
cat = DomesticCat("Dima", "black", 0)
cat.color
SyntaxError: multiple statements found while compiling a single statement
cat = DomesticCat("Dima", "black", 0)
cat.color
'black'
cat.name
'Dima'
cat.age
0
cat.eat
<bound method Animal.eat of <__main__.DomesticCat object at 0x000002ABF5ECF800>>
cat.go
<bound method Animal.go of <__main__.DomesticCat object at 0x000002ABF5ECF800>>


class Animal:
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def eat(self):
        print(f'Животное {self.color} цвета кушает...')
    def go(self):
        print("Животное двигается")
    def sleep(self):
        print("ZZZZZZ")

        
class DomesticCat(Animal):
    def __init__(self, name, color, age):
        self.name = name
        super().__init__(color, age)
    def __repr__(self):
        return "f'Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

    
cat = DomesticCat("Dima", "black", 0)
cat
f'Cat Name:{self.name}
	Age:{self.age}
	Color:{self.color}


class DomesticCat(Animal):
    counter = 123
    def __init__(self, name, color, age):
        self.name = name
        self.id = DomesticCat.counter
        DomesticCat.counter += 1
        super().__init__(color, age)
    def get_id(self):
        print("cat id")
    def __repr__(self):
        return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

  
cat = DomesticCat("Dima", "black", 0)
cat.__dict__
{'name': 'Dima', 'id': 123, 'color': 'black', 'age': 0}
cat.id = 12345
cat.__dict__
{'name': 'Dima', 'id': 12345, 'color': 'black', 'age': 0}

a = 10
b = 11
a + b
21
a.__add__(b)
21
a - b
-1
a.__sub__(b)
-1
a/b
0.9090909090909091
a.__moddir__(b)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.__moddir__(b)
AttributeError: 'int' object has no attribute '__moddir__'. Did you mean: '__dir__'?
help(int)

а как хелп вызвать?
SyntaxError: invalid syntax

a
10
b
11
a.__truediv__(b)
0.9090909090909091
help(str)

"s" in s
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    "s" in s
NameError: name 's' is not defined. Did you mean: 's1'?
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __add__(self, nextcat):
        return self.age + nextcat.age
    def __contains__(self, key):
        return key in self.name
    def __len__(self):
        return self.age
    def __lt__(self, nextcat):
        return self.age < nextcat.age

    
c = Cat("Cat", 5)
c2 = Cat("Hggg", 6)
c2 + c
11
len(c)
5
len(c2)
6
c < c2
True
c2 < c
False
"a" in c
True
"d" in c
False
c
<__main__.Cat object at 0x0000018D2A8DFB00>


class Wallet:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, int_value):
        self.amount += int_value
        return self.amount
    def __sub__(self, int_value):
        self.amount -= int_value
        return self.amount
    def __len__(self):
        return self.amount

    
my_wallet = Wallet(1000)
my_wallet + 100
1100
len(my_wallet)
1100
my_wallet - 50
1050
len(my_wallet)
1050
 help(int)
 
SyntaxError: unexpected indent
help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getitem__(self, key, /)
 |      Return self[key].
 |
 |  __getnewargs__(...)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |
 |      Padding is done using the specified fill character (default is a space).
 |
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |
 |      Return -1 on failure.
 |
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |
 |      Raises ValueError when the substring is not found.
 |
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |
 |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
 |      such as "def" or "class".
 |
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |
 |      Padding is done using the specified fill character (default is a space).
 |
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |
 |  removeprefix(self, prefix, /)
 |      Return a str with the given prefix string removed if present.
 |
 |      If the string starts with the prefix string, return string[len(prefix):].
 |      Otherwise, return a copy of the original string.
 |
 |  removesuffix(self, suffix, /)
 |      Return a str with the given suffix string removed if present.
 |
 |      If the string ends with the suffix string and that suffix is not empty,
 |      return string[:-len(suffix)]. Otherwise, return a copy of the original
 |      string.
 |
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |
 |      Return -1 on failure.
 |
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |
 |      Raises ValueError when the substring is not found.
 |
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |
 |      Padding is done using the specified fill character (default is a space).
 |
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |
 |        sep
 |          The separator used to split the string.
 |
 |          When set to None (the default value), will split on any whitespace
 |          character (including \n \r \t \f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits.
 |          -1 (the default value) means no limit.
 |
 |      Splitting starts at the end of the string and works to the front.
 |
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |
 |        sep
 |          The separator used to split the string.
 |
 |          When set to None (the default value), will split on any whitespace
 |          character (including \n \r \t \f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits.
 |          -1 (the default value) means no limit.
 |
 |      Splitting starts at the front of the string and works to the end.
 |
 |      Note, str.split() is mainly useful for data that has been intentionally
 |      delimited.  With natural text that includes punctuation, consider using
 |      the regular expression module.
 |
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace removed.
 |
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |
 |      The string is never truncated.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  maketrans(...)
 |      Return a translation table usable for str.translate().
 |
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

help(int)
Help on class int in module builtins:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating-point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |
 |  Built-in subclasses:
 |      bool
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __float__(self, /)
 |      float(self)
 |
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |
 |  __format__(self, format_spec, /)
 |      Convert to a string according to format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |
 |  __int__(self, /)
 |      int(self)
 |
 |  __invert__(self, /)
 |      ~self
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __neg__(self, /)
 |      -self
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __pos__(self, /)
 |      +self
 |
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |
 |  __radd__(self, value, /)
 |      Return value+self.
 |
 |  __rand__(self, value, /)
 |      Return value&self.
 |
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |
 |      Rounding with an ndigits argument also returns an integer.
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |
 |  __rxor__(self, value, /)
 |      Return value^self.
 |
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __truediv__(self, value, /)
 |      Return self/value.
 |
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |
 |  __xor__(self, value, /)
 |      Return self^value.
 |
 |  as_integer_ratio(self, /)
 |      Return a pair of integers, whose ratio is equal to the original int.
 |
 |      The ratio is in lowest terms and has a positive denominator.
 |
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |
 |  bit_count(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |
 |      Also known as the population count.
 |
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |
 |  is_integer(self, /)
 |      Returns True. Exists for duck type compatibility with float.is_integer.
 |
 |  to_bytes(self, /, length=1, byteorder='big', *, signed=False)
 |      Return an array of bytes representing an integer.
 |
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.  Default
 |        is length 1.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.  Default is to use 'big'.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  from_bytes(bytes, byteorder='big', *, signed=False)
 |      Return the integer represented by the given array of bytes.
 |
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
...  |        `sys.byteorder' as the byte order value.  Default is to use 'big'.
...  |      signed
...  |        Indicates whether two's complement is used to represent the integer.
...  |
...  |  ----------------------------------------------------------------------
...  |  Static methods defined here:
...  |
...  |  __new__(*args, **kwargs)
...  |      Create and return a new object.  See help(type) for accurate signature.
...  |
...  |  ----------------------------------------------------------------------
...  |  Data descriptors defined here:
...  |
...  |  denominator
...  |      the denominator of a rational number in lowest terms
...  |
...  |  imag
...  |      the imaginary part of a complex number
...  |
...  |  numerator
...  |      the numerator of a rational number in lowest terms
...  |
...  |  real
...  |      the real part of a complex number
... 
