import random
from typing import Callable
from functools import wraps


__all__ =['decor_range_namber']

def decor_range_namber(funk:Callable)->Callable[[int,int],bool]:
    NUM_MIN = 1
    NUM_MAX = 100
    COUNT_NUM = 10
    @wraps(funk)
    def wrapper(num: int, num_count: int)->bool:
        # if NUM_MIN < num < NUM_MAX and NUM_MIN < num_count < COUNT_NUM
        if num in range(NUM_MIN,NUM_MAX) and num_count in range(NUM_MIN,COUNT_NUM):
            print('Всё Ок')
            rez = funk(num,num_count)
        else:
            print('Dont Ок')
            num = random.randrange(NUM_MIN,NUM_MAX)
            num_count = random.randrange(NUM_MIN,COUNT_NUM) 
            rez = funk(num,num_count)
        return rez    
    return wrapper  