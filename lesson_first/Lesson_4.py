import timeit
'''
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
'''
# def task25(st):
#     stroka = st.split()
#     result = {}
#     for i in stroka:
#         if i in result:
#             print(f'{i}_{result[i]}', end=' ')
#         else:
#             print(i, end=' ')
#         result[i] = result.get(i, 0) + 1
#     return




def my_task25(st):
    d = {}
    array = []
    for x in st.split():
        if x in array:
            array.append(f'{x}_{d[x]}')
        else:
            array.append(x)    
        d[x] = d.get(x,0) + 1
        print(d[x])
    return ' '.join(array)



dd = {1: 44, 2: 33}
dd['asd'] = dd.get('asd',0)
print(f'Пример {dd}')


print(my_task25('a a a b c a a d c d d'))
# print(task25('a a a b c a a d c d d'))
'''
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13



'''


'''
Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: +7, +6, +2, +4 и т.д. Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., а значения - список номеров (следующих в том же порядке, что и во входной строке) с соответствующими кодами. Полученный словарь вывести командой:

print(*sorted(d.items()))

Sample Input:
+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
Sample Output:
('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])

'''

# def task112(strs):
#     d = {}
#     for x in strs.split():
#         # добавление множеста значение по 1 ключю
#         d.setdefault(x[:2],[]).append(x)
#     return d



'''
str = input().split(" ")
d = {}
for x in str:
    key = x[0:2]
    if key not in d.keys():
        d[key] = [x]
    else:
        d[key] += [x]
print(*sorted(d.items()))
'''

'''
d = {}
for i in s:
    d[i[:2]] = [x for x in s if x[:2] == i[:2]]
print(*sorted(d.items()))
'''

from itertools import groupby
def task111(st): 
    return ', '.join([f'{x , list(y)}' for x,y in groupby(sorted(st.split(), key=lambda x : x[:2]),lambda x : x[:2])])


s = '+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890'
print(task111(s))

print(f'Затрачено {timeit.timeit(setup=task111(s)): .2f} секунд')


