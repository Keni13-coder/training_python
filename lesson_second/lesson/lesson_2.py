import sys
import decimal
from math import pi
# data: list = [10,10.0,True,[2],('ssrs','sdfsdf'),{1:'_'},{1},'fkhglk/']
# for i,v in enumerate(data,1):
#     print(f'{i}:{v} - id:{id(v)} - {sys.getsizeof(v)} байт - хеш= {hash(v) if isinstance(v,(float,str,int,tuple)) else "изменяемый тип объекта"}')
#     if isinstance(v,int):
#         if v > 0:
#             print(f'{i}:{v}: Это целое число')
#     elif isinstance(v,str):
#             print(f'{i}:{v}: Это строчный объект')



'''
Напишите программу, которая получает целое число и возвращает 
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего 
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода 
в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможно
'''            



# def number_translation(m:int, n=2) -> str:
#     suma = ''
#     d = {10:'A', 11:'B',12:'C',13:'D',14:'E',15:'F'}
#     while m >= 1:
#         if m % n == 0:
#             suma += str(m % n)
#             m = m // n
#         elif (m % n) >9:
#             suma += d[(m % n)]
#             m = m // n
#         else:
#             suma += str(m % n)
#             m = m // n 
#     return f'{suma[::-1]}'
# print(number_translation(934,16))

'''
Напишите программу, которая вычисляет площадь 
круга и длину окружности по введённому диаметру. 
✔ Диаметр не превышает 1000 у.е. 
✔ Точность вычислений должна составлять 
не менее 42 знаков после запятой.
'''

# def task_4(d:int) -> decimal.Decimal:
#     MAX = 1000
#     ACCURACY = decimal.getcontext().prec = 42
#     PI = decimal.Decimal(pi)
#     if d < MAX:
#         diameter = decimal.Decimal(str(d))
#         len_circle = PI * diameter
#         square = PI * diameter ** 2 /4
#         return f'Длина окружности {len_circle=}\n: Площадь окружности {square=}'
#     else:
#         return 'Превышен лимит в 1000'

# print(task_4(10))

'''
Напишите программу, которая решает 
квадратные уравнения даже если 
дискриминант отрицательный. 
✔ Используйте комплексные числа 
для извлечения квадратного корня.

'''

def task_5(a:int|float,b:int|float,c:int|float)-> float|complex:
    d = b**2 - 4 * a * c
    if d < 0:
        d = complex(d,0)
    x_1 = (-b + d ** .5) / (a * 2)
    x_2 = (-b - d ** .5) / (a * 2)
    if d == 0:
        return f'x = {-b / (2 * a)}'
    return f'первый корень {x_1=} второй корень {x_2=}'
       

print(task_5(1,2,1)) 