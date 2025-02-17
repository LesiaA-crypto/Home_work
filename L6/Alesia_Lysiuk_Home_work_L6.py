
menu = """
1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход"""
oper = int(input(menu))

# 1 - добавить нового студента
# 2 - добавить оценку
# 3 - посчитать средний балл
# -1 - выход

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
