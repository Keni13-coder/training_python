from typing import Callable
from functools import wraps

__all__= ['count']

def count(count_num : int = 1):
    def main(funk: Callable):
        @wraps(funk)
        def wrapper(num: int,*args,**kwargs):
            rez = []
            for _ in range(count_num):
                lis = funk(num,*args,**kwargs)
                rez.append(lis)
                # num = num + sum(args)
            return rez
        
        return wrapper
    
    return main



if __name__ == '__main__':
    @count(5)
    def test(num: int,*args):
        f = 1
        for i in range(2,num+1):
            f *= i
        return f 
    print(test(10,5))