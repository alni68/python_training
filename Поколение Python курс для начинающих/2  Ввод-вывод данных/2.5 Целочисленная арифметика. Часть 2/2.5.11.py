'''
Пересчет временного интервала
Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в часах и минутах.

Формат входных данных
На вход программе подаётся целое число – количество минут.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''

n=int(input())
print(n, 'мин - это', (n+60)//60-1, 'час', n%60, 'минут.')