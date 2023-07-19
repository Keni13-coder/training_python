import random
import decor_les_9


__all__ = ['guess']




@decor_les_9.decor_seved_json.write_json('Test_les_9')   
@decor_les_9.decor_count.count(2)
@decor_les_9.decor_range.decor_range_namber
def guess(num: int , num_count: int )-> bool:
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