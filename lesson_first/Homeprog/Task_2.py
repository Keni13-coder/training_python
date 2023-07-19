from functools import reduce
''' Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

'''

def task2(num):
    return sum([int(x) for x in str(num)])
    return sum(list(map(int , str(num))))
    return reduce(lambda x,y: int(x) + int(y), str(num))
print(task2(123))
