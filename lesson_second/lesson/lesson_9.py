'множественные дикораторы работают по принципу стека - снизу вверх запоминает и также сначала происходит возвращение основной функции, с вверху вниз закрывает'
import random
from typing import Callable
import json
from decor_les_9 import *
from pathlib import Path
import csv
import numpy as np
'''def cache(func: Callable):
    _cache_dict = {}
    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
            print(_cache_dict)
        return _cache_dict[args]
    print('Конец') # сначала возвращает конец потом wrapper
    return wrapper #  в ствою очередь wrapper возвращает  словарь с ключём (1,10)
@cache
def rnd(a: int, b: int) -> int:
    print('Запуск')
    return random.randint(a, b)
'''

# print(f'{rnd(1, 10) = }')
# print(f'{rnd(1, 10) = }')
# print(f'{rnd(1, 9) = }')





"Декаратор с параметрами"
'''def count(num: int = 1):
    def deco(func: Callable):
        counter = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter
        return wrapper
    return deco
@count(10) # -> параметр 10, каждый раз при вызове функции будет добовляеться 10 значений
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)


print(f'{rnd(1, 10) = }')
print(f'{rnd(1, 100) = }')
print(f'{rnd(1, 1000) = }')
'''
' decorater wraps(funk) -  из fanctools  позволяет получть информацию о функции а не о wrappers'
'decorater cache - из fanctools  позволяет получть данный которые были уже использованы не вызывая функцию, пример работы 1 задача'



'''
Задание №1
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток. 
'''

# def task_1(num: int = int(input('Введите число от 1 до 100: ')), num_count: int = int(input('Введите чсило попыток от 1 до 10: ')))->Callable[[str], bool]:
#     def loc()-> bool:
#         nonlocal num, num_count
#         rez = random.randint(1,99)
#         while num_count:
#             if num == rez:
#                 return True
#             elif num > rez:
#                 print(f'Введённое число {num} > загадонного')
#             else:
#                 print(f'Введённое число  {num} < загадонного')  
#             num = int(input('Введите число от 1 до 100: '))
#             num_count -= 1
#         else:
#             return False
#     return loc

# print(task_1()())

'''
Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функци - угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
'''


# def decor_task_2(funk:Callable)->Callable[[int,int],bool]:
#     NUM_MIN = 1
#     NUM_MAX = 100
#     COUNT_NUM = 10
#     def wrapper(num: int, num_count: int)->bool:
#         # if NUM_MIN < num < NUM_MAX and NUM_MIN < num_count < COUNT_NUM
#         if num in range(NUM_MIN,NUM_MAX) and num_count in range(NUM_MIN,COUNT_NUM):
#             print('Всё Ок')
#             rez = funk(num,num_count)
#         else:
#             print('Dont Ок')
#             rez = funk(random.randrange(NUM_MIN,NUM_MAX),random.randrange(NUM_MIN,COUNT_NUM))

#         return rez    
#     return wrapper    



# @decor_task_2
# def task_2(num: int , num_count: int ):
#     START_RANGE = 1
#     END_RANGE = 100
#     rez = random.randrange(START_RANGE,END_RANGE)
#     while num_count:
#         if num == rez:
#             return True
#         elif num > rez:
#             print(f'Введённое число {num} > загадонного')
#         else:
#             print(f'Введённое число  {num} < загадонного')  
#         num = int(input('Введите число от 1 до 100: '))
#         num_count -= 1
#         print(f'Осталось {num_count} попыток')
#     else:
#         return False
    
# print(task_2(100,20))    



'''
Задание №3
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
'''

# def write_json(path: str = 'Lesson_python\lesson_second\lesson\Test_les_9'):
#     def main(funk: Callable)->Callable[[int],None]:
#         def wrapper(*args,**kwargs)-> None:
#             rez = {str(*args):funk(*args,**kwargs)}
#             try:
#                 with open(f'{path}\\rez.json','r+',encoding='utf-8') as rez_file:
#                     reader_dict: dict = json.load(rez_file)
#                     reader_dict.update(rez)
#                     print(reader_dict)
#                     with open(f'{path}\\rez.json','w',encoding='utf-8') as rez_file:
#                         json.dump(reader_dict,rez_file, indent= 2, ensure_ascii= False, skipkeys=True)
#             except (FileNotFoundError, json.decoder.JSONDecodeError):  
#                 with open(f'{path}\\rez.json','w',encoding='utf-8') as rez_file:
#                     json.dump(rez,rez_file, indent= 2, ensure_ascii= False, skipkeys=True)         
#         return wrapper
    
#     return main

# @ write_json('Lesson_python\lesson_second\lesson\Test_les_9')
# def task_3(num: int, *args, **kwargs):
#     return [(x,x**i)  for i,x in enumerate(range(random.randrange(1,num))) ]


# print(task_3(10,i=10))

'''
Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции
'''



# def count(count_num : int = 1):
#     def main(funk: Callable):
#         def wrapper(num: int):
#             rez = []
#             for _ in range(count_num):
#                 lis = funk(num)
#                 rez.append(lis)
#                 num += 1
#             return rez
        
#         return wrapper
    
#     return main



# @count(10)
def task_4(num: int):
    f = 1
    for i in range(2,num+1):
        f *= i
    return f    
# print(task_4(5))   


'''
Задание №5
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
'''

@decor_seved_json.write_json('Test_les_9')   
@decor_count.count(2)
@decor_range.decor_range_namber
def task_5(num: int , num_count: int ):
    START_RANGE = 1
    END_RANGE = 100
    rez = random.randrange(START_RANGE,END_RANGE)
    while num_count:
        if num == rez:
            return True
        elif num > rez:
            print(f'Введённое число {num} > загадонного')
        else:
            print(f'Введённое число  {num} < загадонного')  
        num = int(input('Введите число от 1 до 100: '))
        num_count -= 1
        print(f'Осталось {num_count} попыток')
    else:
        return False
    
# print(task_5(100,9))



'''
Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке. 
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного 
уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы 
функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
'''

     


@decor_seved_json.write_json('Test_les_9')
def quadratic(a: int|float ,b: int|float ,c: int|float)-> float|complex:
    d = b**2 - 4 * a * c
    if d < 0:
        d = complex(d,0)
    x_1 = (-b + d ** .5) / (a * 2)
    x_2 = (-b - d ** .5) / (a * 2)
    if d == 0:
        return f'x = {-b / (2 * a)}'
    return f'первый корень {x_1=} второй корень {x_2=}'
       

def main(funk):
    def wrapper(path):
        rez = []
        with open(path,'r',newline='',encoding='utf-8') as reader_file:
            reader_ = csv.reader(reader_file, quoting = csv.QUOTE_NONNUMERIC)
            for row in reader_:
                root = quadratic(*row)
                rez.append(root)
        return rez
    return wrapper



def write_number_csv(number_row: int, pach: str=Path().cwd()):
    MAX_NUMBER = 1000
    MIN_LEN_LIST = 3
    RANGE_LIST = random.randrange(MAX_NUMBER,number_row)
    with open(f'{pach}\\home_les_9.csv','w',newline='',encoding='utf-8') as rez_file:
        rez = np.random.randint(MAX_NUMBER,size=(RANGE_LIST, MIN_LEN_LIST))
        print(rez)
        writer = csv.writer(rez_file)
        writer.writerows(rez)


@main
def writer_json_q(path: str)->None:
    return
    

# writer_json_q('home_les_9.csv')