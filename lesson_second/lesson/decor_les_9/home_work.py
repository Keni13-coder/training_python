from pathlib import Path
import csv
import numpy as np
import random
from typing import Callable
import decor_seved_json


__all__ = ['write_number_csv','writer_json_q']

def write_number_csv(number_row: int, pach: str=Path().cwd())-> None:
    MAX_NUMBER = 1000
    MIN_LEN_LIST = 3
    RANGE_LIST = random.randrange(MAX_NUMBER,number_row)
    with open(f'{pach}\\home_les_9.csv','w',newline='',encoding='utf-8') as rez_file:
        rez = np.random.randint(MAX_NUMBER,size=(RANGE_LIST, MIN_LEN_LIST))
        print(rez)
        writer = csv.writer(rez_file)
        writer.writerows(rez)

def __main(funk: Callable)-> Callable[[str],list]:
    def wrapper(*args,**kwargs)->list:
        rez = []
        with open('Test_les_9\home_test\home_les_9.csv','r',newline='',encoding='utf-8') as reader_file:
            reader_ = csv.reader(reader_file, quoting = csv.QUOTE_NONNUMERIC)
            for row in reader_:
                root = funk(*row)
                rez.append(root)
        return rez
    return wrapper

@__main
@decor_seved_json.write_json('Test_les_9\home_test')
def __quadratic(a: int|float ,b: int|float ,c: int|float)-> float|complex:
    d = b**2 - 4 * a * c
    if d < 0:
        d = complex(d,0)
    x_1 = (-b + d ** .5) / (a * 2)
    x_2 = (-b - d ** .5) / (a * 2)
    if d == 0:
        return f'x = {-b / (2 * a)}'
    return f'первый корень {x_1=} второй корень {x_2=}'







@__main
def writer_json_q(path: str)->None:
    return
    
if __name__ == '__main__':
    # writer_json_q('home_les_9.csv')
    print(__quadratic(1,2,3))