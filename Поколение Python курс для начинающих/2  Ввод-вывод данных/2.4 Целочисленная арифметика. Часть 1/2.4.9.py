'''
Следующее и предыдущее
Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.

Формат входных данных
На вход программе подаётся целое число.

Формат выходных данных
Программа должна вывести текст согласно условию задачи.
'''

x=int(input())
y=x+1
z=y+1
print('Следующее за числом', x, 'число:', x+1)
print('Для числа', x, 'предыдущее число:', x-1)