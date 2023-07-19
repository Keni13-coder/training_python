'''
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''

def task17(array):
    return len(set(array))


print(task17([1, 1, 2, 0, -1, 3, 4, 4]))

def task17(array):
    new_array=[]
    for x in array:
        if x not in new_array:
            new_array.append(x)
    return len(new_array)
     

print("другая часть",task17([1, 1, 2, 0, -1, 3, 4, 4]))


'''
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 2
Output: [4, 5, 1, 2, 3]
'''


def task19(array, k):
    x = 0
    if k <= len(array)-1:
        while x < k:
            array.insert(0,array[-1])
            array.pop(-1)
            x += 1
    return array
print(task19([1, 2, 3, 4, 5],2))

'''
Задача №21. Решение в группах
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально.
Пользователь его не вводит
'''

def task21(array):
    return set([ x[i] for x in array for i in x])



print(task21([{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]))





'''
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
'''
from itertools import groupby
def tts(array):
    print([list(y) for x,y in groupby([array[x] > array[x-1] if x != len(array) else array[x-1]> array[x-2] for x,y in enumerate(array,1)])])
    return(max(map(len, [list(y) for x, y in groupby([array[x] > array[x-1] if x != len(array) else array[x-1]> array[x-2] for x,y in enumerate(array,1)])])))



print(tts([0, -1, 5, 2, 3]))

