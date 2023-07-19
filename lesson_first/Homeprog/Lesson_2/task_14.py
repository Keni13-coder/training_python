'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
превосходящие числа N
'''

def task14(num):
    return [2 ** x  for x in range(num) if 2 ** x <num]




print(task14(10))