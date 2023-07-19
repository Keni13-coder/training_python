from collections.abc import Generator
'''
Напишите функцию, которая принимает на вход строку — 
абсолютный путь до файла. Функция возвращает кортеж из трёх 
элементов: путь, имя файла, расширение файла.
'''

def task_1(file_path:str):
    a,b,c = '\\'.join(file_path.split('\\')[:-1]),file_path.split('\\')[-1].split('.')[0],file_path.split('\\')[-1].split('.')[1]
    return (a,b,c) 
    'Второй вариант мне нравиться больше '
    # file_path = file_path.split('\\')
    # return (f"Путь файла: {'/'.join(file_path[:-1])}",f"Имя файла: {file_path[-1].split('.')[0]}",f"Расширение файла: {file_path[-1].split('.')[1]}")



# print(task_1('D:\Codewars\it is prank\Lesson_python\lesson_second\home_lesson\home_les_4.py'))


'''
✔ Напишите однострочный генератор словаря, который принимает 
на вход три списка одинаковой длины: имена str, ставка int, 
премия str с указанием процентов вида «10.25%». В результате 
получаем словарь с именем в качестве ключа и суммой 
премии в качестве значения. Сумма рассчитывается 
как ставка умноженная на процент премии 


'''


def task_2(names: list[str],bets: list[int],bonus:list[str])->dict[str:int]:
    return {name: bet / 100 * float(bon) for name,bet,bon in zip(names,bets,map(lambda x:x.replace('%',''),bonus))}



# print(task_2(["миша","паша","саша"],[35000,45000,40000],['10.25%','15.25%','8.25%']))

'''
 Создайте функцию генератор чисел Фибоначчи (см. Википедию).

'''


def task_3(n:int)->Generator[int]:
    fib_1,fib_2 = 0,1
    for x in range(n):
        yield fib_2
        fib_1,fib_2 = fib_2,fib_1 + fib_2


for x in task_3(7):
    print(x)