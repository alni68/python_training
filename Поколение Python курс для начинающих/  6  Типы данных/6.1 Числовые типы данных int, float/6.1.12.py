'''
Наибольшее и наименьшее
Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.

Формат входных данных
На вход программе подается пять целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести наименьшее и наибольшее число с поясняющей надписью.
'''

a=int(input())
b=int(input())
c=int(input())
d=int(input())
f=int(input())

print('Наименьшее число =', min(a, b, c, d, f))
print('Наибольшее число =', max(a, b, c, d, f))