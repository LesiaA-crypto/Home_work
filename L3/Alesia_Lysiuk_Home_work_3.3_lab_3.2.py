
# Lysiuk_Alesia_hw3.1_L3.

list = [1, 2, 3, 4, 5]
list
[1, 2, 3, 4, 5]
len(list)
5
int(input("Введите любое число: "))
Введите любое число: 5
5
list.insert(2, 7)
list
[1, 2, 7, 3, 4, 5]

list.pop()
5
list
[1, 2, 7, 3, 4]
print(len (list))
5


# Home_work_Lab_3.2.

list = ["Ivan Ivanov", "Petr Petrov", "Sergei Sergeev"]
list
['Ivan Ivanov', 'Petr Petrov', 'Sergei Sergeev']

list.append("Sidr Sidorov")
list
['Ivan Ivanov', 'Petr Petrov', 'Sergei Sergeev', 'Sidr Sidorov']

for i in list:
    print(i)

    
Ivan Ivanov
Petr Petrov
Sergei Sergeev
Sidr Sidorov


lists = []
                       
lists
                       
[]

for i in range(6):
     lists.append(input("-->"))

                       
-->"Ghgy HHHHH"
-->"Uggg Kkkk"
-->"Ihhh Pjjj"
-->"Thhh Ojjjj"
-->"Yggg Phhhh"
-->"Ihhhh Tnnnn"

lists
                       
['"Ghgy HHHHH"', '"Uggg Kkkk"', '"Ihhh Pjjj"', '"Thhh Ojjjj"', '"Yggg Phhhh"', '"Ihhhh Tnnnn"']

lists += list
                       


print(list + lists)
                       
['Ivan Ivanov', 'Petr Petrov', 'Sergei Sergeev', 'Sidr Sidorov', '"Ghgy HHHHH"', '"Uggg Kkkk"', '"Ihhh Pjjj"', '"Thhh Ojjjj"', '"Yggg Phhhh"', '"Ihhhh Tnnnn"', 'Ivan Ivanov', 'Petr Petrov', 'Sergei Sergeev', 'Sidr Sidorov']

listss = list + lists
                       
listss.append("Iiiii Ppppp")
                       
listss
                       
['Ivan Ivanov', 'Petr Petrov', 'Sergei Sergeev', 'Sidr Sidorov', '"Ghgy HHHHH"', '"Uggg Kkkk"', '"Ihhh Pjjj"', '"Thhh Ojjjj"', '"Yggg Phhhh"', '"Ihhhh Tnnnn"', 'Ivan Ivanov', 'Petr Petrov', 'Sergei Sergeev', 'Sidr Sidorov', 'Iiiii Ppppp']

listss.pop
                       
<built-in method pop of list object at 0x000001E4E157FE40>

listss.pop()
                       
'Iiiii Ppppp'
lists.insert(0, "Tgggg Ttttt")
                       
lists
                       
['Tgggg Ttttt', '"Ghgy HHHHH"', '"Uggg Kkkk"', '"Ihhh Pjjj"', '"Thhh Ojjjj"', '"Yggg Phhhh"', '"Ihhhh Tnnnn"', 'Ivan Ivanov', 'Petr Petrov', 'Sergei Sergeev', 'Sidr Sidorov']

print(len(listss))
                       
14
