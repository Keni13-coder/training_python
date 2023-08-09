import logging
from typing import Callable
from functools import wraps
import dateparser as dt
'''
Задание №1
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.
'''
# logging.basicConfig(filename='rezul_task_1.log.', filemode='w', encoding='utf-8', level=logging.ERROR)

def task_1(x: int, y: int):
    
    try:
        result: float = x / y
    except ZeroDivisionError as zero:
        logging.error('Деление на 0')
        return
    
    return result




'''
Задание №2
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.
'''
'''
Задание №3
Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.
'''





def write_log(path: str = 'Lesson_python\lesson_second\lesson\Test_les_9'):
    def main(funk: Callable)->Callable[[any],None]:
        
        @wraps(funk)
        def wrapper(*args,**kwargs)-> None:
           
            FORMAT = '{levelname:<8} - {asctime}. В файле "{name}", записала сообщение: {msg}'
            logger = logging.getLogger(__name__)
            logging.basicConfig(filename='resul_task_2.log.', filemode='w', encoding='utf-8', format=FORMAT, style='{', level=logging.INFO)
            
            try:
                rez = {f'{args}':funk(*args,**kwargs)}
                logger.info(f'Функция с именем {funk.__name__}, имея аргументы {[*args, *kwargs]} выдает результат {rez}')
            except Exception as ex:
                logger.error(f'Функция с именем {funk.__name__}, имея аргументы {[*args, *kwargs]} выдает результат {ex}')                
        
        return wrapper
    
    return main

@write_log()
def task_1(x: int, y: int):
    
    result: float = x / y

    return result


'''
Задание №4
Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.
'''

def task_4(date_: str):
    # date_ = date_.split()
    # count = int(''.join(date_[0])[0])
    # weekday = date_[1]
    # month = date_[2]
    date = dt.parse(date_)
    return date





match __name__:
    case '__main__':
        # task_1(2,0)
        print(task_4('12 пятница декабрь'))
        ...