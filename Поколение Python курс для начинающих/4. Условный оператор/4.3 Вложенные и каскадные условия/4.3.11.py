'''
Пересечение отрезков 🌶️🌶️
На числовой прямой даны два отрезка:
[1;1]
[a 1 ;  b 1 ] и [2;2]
[a 2 ; b 2 ]. Напишите программу, которая находит их пересечение.

Пересечением двух отрезков может быть:

отрезок;
точка;
пустое множество.
Формат входных данных
На вход программе подаются 4 целых числа 1,1,2,2
a 1 ,b 1 ,a 2 ,b 2, каждое на отдельной строке. Гарантируется, что a1 <b1 и a2 <b2.

Формат выходных данных
Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое множество».
'''

a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if a2 == b1:
    print(a2)
elif a1 == b2:
    print(a1)
elif (a2 < b1):
    print("пустое множество")
elif (a1 > b2):
    print("пустое множество")

elif (b1 <= a1):
    if a2 <= b2:
        print(a1, a2)
    elif a2 > b2:
        print(a1, b2)

elif (a1 < b1):
    if a2 <= b2:
        print(b1, a2)
    elif a2 > b2:
        print(b1, b2)