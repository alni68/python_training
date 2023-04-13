'''
Ход ферзя
Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли ферзь попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом ферзя можно попасть во вторую или «NO» в противном случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный ферзь ходит по диагонали, горизонтали или вертикали.
'''

a1=int(input())
a2=int(input())
b1=int(input())
b2=int(input())
if (b1-a1)==(b2-a2) or (a1-b1)==(b2-a2)  or (a1==b1) or (a2==b2):
    print('YES')
else:
    print('NO')