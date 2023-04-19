'''
7.3.2
Что покажет приведенный ниже фрагмент кода?

num1 = 4
num2 = 6
num1 += num2
num1 *= num1
print(num1)

100
'''

'''
7.3.3
Что покажет приведенный ниже фрагмент кода?

total = 0
for i in range(1, 6):
    total += i
print(total)

15
'''

'''
7.3.4
Что покажет приведенный ниже фрагмент кода?

total = 0
for i in range(1, 6):
    total += i
    print(total, end='')
    
1361015
'''

'''
7.3.5
Количество чисел
На вход программе подаются два целых числа a и b (a≤b). 
Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно, 
куб которых оканчивается на 4 или 9.

Формат входных данных
На вход программе подаются два целых числа a и b (a≤b).

Формат выходных данных
Программа должна вывести одно целое число в соответствии с условием программы.

Примечание. Куб числа a – это его третья степень.
'''

a=int(input())
b=int(input())
counter = 0
for i in range(a, b+1):
    if i**3 % 10 == 4 or i**3 % 10 == 9:
        counter = counter + 1
print(counter)

'''
7.3.6
Сумма чисел
На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел. 

Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести сумму данных чисел.
'''

n=int(input())
total=0
for i in range(n):
    a = int(input())
    total=total+a
print(total)

'''
7.3.7
Асимптотическое приближение
На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения
Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math.
'''

from math import *
n=int(input())
total=0
for i in range(1, n+1):
    total=total+1/i
print(total-log(n))

'''
7.3.8
Сумма чисел 2
На вход программе подается натуральное число n. 
Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно) 
квадрат которых оканчивается на 2,5 или 8.

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести единственное число в соответствии с условием задачи.

Примечание. Если таких чисел нет в указанном диапазоне, то следует вывести 0.
'''

n = int(input())
total = 0
for i in range(n + 1):
    if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
        total = total + i

print(total)

'''
7.3.9
Факториал
На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.

Входные данные
На вход программе подается натуральное число n,(n≤12).

Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.

Примечание. Факториалом натурального числа n, называется произведение всех натуральных чисел от 
1 до n, то есть n!=1⋅2⋅3⋅…⋅n
'''

n = int(input())
total = 1
for i in range(1, n + 1):
    total = total * i

print(total)

'''
7.3.10
Без нулей
Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

Формат входных данных
На вход программе подаются 10 целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести произведение отличных от нуля чисел.

Примечание. Гарантируется, что хотя бы одно из 10 чисел является ненулевым.
'''

total = 1
for i in range(10):
    a = int(input())
    if a != 0:
        total = total * a

print(total)

'''
7.3.11
Сумма делителей
На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.

Входные данные
На вход программе подается натуральное число n.

Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.

Примечание. Функция подсчета суммы всех делителей числа является очень важной в теории чисел.
'''

n = int(input())
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total = total + i

print(total)

'''
7.3.12
Знакочередующаяся сумма
На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы 
1−2+3−4+5−6+…+(−1)**n+1*n.

Входные данные
На вход программе подается натуральное число n.

Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.
'''

n=int(input())
total=0
for i in range(1, n+1):
    if i%2==0:
        total=total-i
    elif i%2==1:
        total=total+i
print(total)

'''
7.3.13
Наибольшие числа 🌶️🌶️
На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

Формат входных данных
На вход программе подаются натуральное число n≥2, а затем n различных натуральных чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести два наибольших числа, каждое на отдельной строке.
'''

n = int(input())
max1 = 0
max2 = 0
for i in range(n):
    a = int(input())
    if a > max1:
        max2 = max1
        max1 = a

    elif a < max1 and a > max2:
        max2 = a
print(max1)

print(max2)

'''
7.3.14
Only even numbers 🌶️
Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.

Формат входных данных
На вход программе подаются 10 целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести строку «YES», если все числа четные и «NO» в ином случае.
'''

total=0
for i in range(10):
    n=int(input())
    if n%2==0:
        total=total+1
if total==10:
    print('YES')
else:
    print('NO')

'''
7.3.15
Последовательность Фибоначчи 🌶️
Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.

Формат входных данных
На вход программе подается одно число  n (n≤100) – количество членов последовательности.

Формат выходных данных
Программа должна вывести члены последовательности Фибоначчи, отделенные символом пробела.

Примечание. Последовательность Фибоначчи – это последовательность натуральных чисел, где каждое последующее число является суммой двух предыдущих:
'''

n=int(input())
max1=0
max2=1
q=0
for i in range(n):
    q=max2+max1
    print(q, end=' ')
    max2=max1
    max1=q