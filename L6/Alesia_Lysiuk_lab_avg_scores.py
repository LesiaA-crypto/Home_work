Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Home work.
>>> # L6.
>>> school_class = {}
>>> name = input("name:")
name:Alesia Lysiuk
>>> name
'Alesia Lysiuk'
>>> # {name:grades, name: grades}
>>> set tuple list
SyntaxError: invalid syntax
>>> grade = int(input("grade:"))
grade:7
>>> school_class[name] = (grade, )
>>> grade = int(input("grade:"))
grade:5
>>> school_class[name] += (grade, )
>>> school_class
{'Alesia Lysiuk': (7, 5)}
>>> school_class[name]
(7, 5)
>>> sum(school_class[name])/len(school_class[name])
6.0
>>> 
>>> menu = """
... 1 - добавить нового студента
... 2 - добавить оценку
... 3 - посчитать средний балл
... -1 - выход"""
>>> oper = int(input(menu))

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    oper = int(input(menu))
ValueError: invalid literal for int() with base 10: ''
while oper != -1:
    if oper == 1:
        name = input("name")
        if name not in school_class:
            school_class[name] = ()
         else:
             
SyntaxError: unindent does not match any outer indentation level
while oper != -1:
    if oper == 1:
        name = input("name")
        if name not in school_class:
            school_class[name] = ()
            print("Студент успешно создан")
        else:
            print("Уже был создан.")
    elif oper == 2:
        name = input("name:")
        if name in school_class:
            gfade = int(input("grade (1-10):"))
            school_class[name] += (grade, )
            print("Оценка успешно добавлена.")
        else:
            print("Студента ещё не существует.")
    elif oper == 3:
        if len(school_class) < 1:
            print("Оценок не содержится.")
        elif len(school_class) >= 1:
            for name in school_class.keys():
                grades = school_class[name]
                if len (grades) >= 1:
                    print(name)
                    print(school_class[name])
                    print("avg:")
                    print(sum(grades)/len(grades))
                else:
                    print("y", name, нет оценок.")
                          
SyntaxError: unterminated string literal (detected at line 29)
while oper != -1:
    if oper == 1:
        name = input("name")
        if name not in school_class:
            school_class[name] = ()
            print("Студент успешно создан")
        else:
            print("Уже был создан.")
    elif oper == 2:
        name = input("name:")
        if name in school_class:
            gfade = int(input("grade (1-10):"))
            school_class[name] += (grade, )
            print("Оценка успешно добавлена.")
        else:
            print("Студента ещё не существует.")
    elif oper == 3:
        if len(school_class) < 1:
            print("Оценок не содержится.")
        elif len(school_class) >= 1:
            for name in school_class.keys():
                grades = school_class[name]
                if len (grades) >= 1:
                    print(name)
                    print(school_class[name])
                    print("avg:")
                    print(sum(grades)/len(grades))
                else:
                    print("y", name, "нет оценок.")
    oper = int(input(menu))

    
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    while oper != -1:
NameError: name 'oper' is not defined. Did you mean: 'open'?
