Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a, b = 1, 2
a <= b
True
a != b
True

res = a != B
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    res = a != B
NameError: name 'B' is not defined. Did you mean: 'b'?
res = a != b
res
True
type (res)
<class 'bool'>
a
1
b
2
password = input("/login:")
/login:12345
if password == "12345":
    print("ok")

    
ok
password = input("/login:")
/login:123
secret = "123"
if password == secret:
    print("ok")

    
ok
if password == secret:
    print("ok")
else:
    print("wrong pass")

    
ok

================== RESTART: Shell =================
secret = "123"
secret1 = "bond"
if password == secret
SyntaxError: expected ':'

password = input("/login:")
/login:

a = 123
if a == 123:
    res = True
else:
    res = False

    
res
True
a
123
res = True if a ==123 else False
res
True
res == a ==123
False


password = "123"
secret
'123'
secret1
'bond'
match password:
    case '123':
        print("ok")
    case 'bond*':
        print("jj")
    case _:
        print(-1)

        
ok
counter = 1
while counter < 10:
    print(counter)
    counter += 2

    
1
3
5
7
9
counter = 1
while counter < 10:
    
SyntaxError: multiple statements found while compiling a single statement
counter = 1
while counter < 10:
    print(counter)
    if counter == 5:
        print("exit")
        break
    counter += 2

    
1
3
5
exit
counter = 1
while counter < 10:
    counter += 2
    if counter == 5:
        print("go")
        continue
    print(counter)

    
3
go
7
9
11

for
SyntaxError: invalid syntax
for i in range (5):
    print(i)

    
0
1
2
3
4
for i in range (1, 6, 2):



import time
SyntaxError: expected an indented block after 'for' statement on line 1
import time
time.sleep (3)
for i in range (6):
    print("sleep")

    
sleep
sleep
sleep
sleep
sleep
sleep
st = "hello 1234"
to_find = "2"
to_find in st
True
to_find = "0"
to_find in st
False
if to_find in st:
    else:
        
SyntaxError: invalid syntax
noPrint = "праонкалла"
word = (input("дай мне слово")
word
        
SyntaxError: '(' was never closed
noPrint = "праонкалла"
        
noPrint = "праонкалла"
        
noPrint = "праонкалла"
        

================== RESTART: Shell =================
noPrint = "hgjdjjfjf"
        
for char in word:
        if char in noPrint:
        continue
    
SyntaxError: expected an indented block after 'if' statement on line 2
SyntaxError: expected an indented block after 'if' statement on line 2
SyntaxError: invalid syntax
for char in word:
    if char not in no Print:
        
SyntaxError: invalid syntax
for char in word:
    if char not in noPrint:
        continue
    print (char)

    
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    for char in word:
NameError: name 'word' is not defined. Did you mean: 'ord'?
age = 21
money = 1000
if age > 18 and money > 900:
    print("Grind")

    
Grind
age = 16
if age > 18 and money > 900:
 print("Grind")

 

age
16
16
16

or char in word:
    
SyntaxError: invalid syntax
for char in word
SyntaxError: expected ':'
for char in word:
    if char in noPrint:
        continue
    print(char)

    
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    for char in word:
NameError: name 'word' is not defined. Did you mean: 'ord'?
age = 21
money = 1000
if age > 18 and money > 900:
    print("Grind")
    
SyntaxError: multiple statements found while compiling a single statement

age = 21
money = 1000
if age > 18 and money > 900:
    print("Grint")

    
Grint
age = 16
if age > 18 and money > 900:
    print("Grint")

    
age = 17
if age > 18 or money > 900:
    print("Grint")

    
Grint
money = -1
if age > 18 or money >900:
    print("Grint")

    
False or False or False
False
False or True or False
True
True
True
not True
False
age
17
age > 10
True
not age > 10
        
False
True
        
True
not True
        
False
not not True
        
True
False
        
False
not False
        
True
True
        
True

if to find in st:
        
SyntaxError: invalid syntax
st = "hello 1234"
to_find = "2"
to_find in st
True
to_find = "0"
to_find in st
False
        
SyntaxError: multiple statements found while compiling a single statement
st = "hello 1234"
        
to_find = "2"
        
if to_find in st:
    print("0 in st")
else:
    print("hope")

    
0 in st
if to find not in st:
    
SyntaxError: invalid syntax
if to_find not in st:
    print("0 in st")

    
if to_find not in st:
    print("0 in st")
else:
    print("nope")

    
nope
noPrint = "лорпдлпдлр"
word = input("дай мне слова")
дай мне словалор15броплопло15р
word
'лор15броплопло15р'
for char in word:
    print(char)

    
л
о
р
1
5
б
р
о
п
л
о
п
л
о
1
5
р
>>> for char in word:
...     if char in word:
...         continue
...     print(char)
... 
...     
>>> 
>>> for char in word:
...     if char not in noPrint:
...         break
...     print(char)
... else:
...     print("успешно")
... 
...     
л
о
р
