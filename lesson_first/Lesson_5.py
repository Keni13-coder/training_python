'''Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию'''

def fib(k):
    if k <= 1:
        return k
    else:
        return fib(k-1) + fib(k-2)


print(fib(7))


' факториал рекурсией'

def Fff(n):
    
    return n if n == 1 else n * Fff(n-1)


print(Fff(5))



'Палиндром'


def pal(st):
    if len(st) <= 1:
        return 'Слово палиндромно'
    if st[0] == st[-1]:
        return pal(st[1:-1]) 
    return 'Слово  не палиндромно'


print(pal('манекенам'))

'''
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes

'''
# def task35(n):
#     if n in [0,1]:
#         return 'No'
#     return 'Yes' if  n % 1 == 0 and n % n == 0  else 'No'


# print(task35(0))
'''
Решение в группах
15 минут
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3

'''
def task(array):
    return array if len(array) <= 1 else task(array[1:]) + task(array[:1]) 

print(task([3, 4, 5, 6]))

""" 
[3 4 5 6]
Левая рекурсия
1 шаг [4 5 6]
      /     \
    5 6       5
2 шаг
    6        5
6 + 5 = [6 , 5] левая рекурсия от 4 5 6
Правая рекурсия от  4 5 6
1 шаг [4] 
    4
Полностью левая чать будет [6, 5] + [4] = [6, 5, 4]
Правая чать
[3]
[6, 5, 4] + [3] = [6, 5, 4, 3]
"""

# def f(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return f(n - 1) + f' {k}'


# n = int(input())
# print(f(n))