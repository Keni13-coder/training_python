from itertools import combinations
'''
Дан список повторяющихся элементов. Вернуть список 
с дублирующимися элементами. В результирующем списке 
не должно быть дубликатов.

'''
array = [1,2,3,4,5,2,3,4,1,5,7]
def task_1(array:list)-> list:
    '''эта функция возвращает список дубликатов '''
    return sorted(set(x for x in array if array.count(x)>1))

print(task_1(array))

'''

В большой текстовой строке подсчитать количество встречаемых 
слов и вернуть 10 самых частых. Не учитывать знаки препинания 
и регистр символов. За основу возьмите любую статью 
из википедии или из документации к языку.

'''
st = '''
Python - это простой в освоении и мощный язык программирования. Он обладает эффективными высокоуровневыми структурами данных и простым, но эффективным подходом к объектно-ориентированному программированию. Элегантный синтаксис Python и динамическая типизация вместе с его интерпретируемым характером делают его идеальным языком для написания сценариев и быстрой разработки приложений во многих областях на большинстве платформ.

Интерпретатор Python и обширная стандартная библиотека свободно доступны в исходном виде или в двоичном виде для всех основных платформ с веб-сайта Python, https://www.python.org/ и могут свободно распространяться. На этом же сайте также содержатся дистрибутивы и указатели на множество бесплатных модулей, программ и инструментов Python сторонних производителей, а также дополнительная документация.

Интерпретатор Python легко расширяется за счет новых функций и типов данных, реализованных на C или C ++ (или других языках, вызываемых из C). Python также подходит в качестве языка расширения для настраиваемых приложений.

Это руководство неофициально знакомит читателя с основными концепциями и функциями языка и системы Python. Для практического использования полезно иметь под рукой интерпретатор Python, но все примеры являются автономными, поэтому руководство также можно прочитать в автономном режиме.
'''
def task_2(st:str)->list[str]:
    st = st.split()
    st = {x:st.count(x) for x in st if x not in [' ',',']}
    st = sorted(st,key=st.get)[::-1]
    return st[0:10]

print(task_2(st))



'''

Создайте словарь со списком вещей для похода в качестве 
ключа и их массой в качестве значения. Определите какие 
вещи влезут в рюкзак передав его максимальную 
грузоподъёмность. Достаточно вернуть один допустимый вариант.

'''

dit = {'гири': 25,
       'палатка': 12,
       'вода':6,
       'еда':7,}




def task_3(d:dict,num:int)->list[tuple]:
    # lis =[]
    # for k,v in d.items():
    #     for j,i in d.items():
    #         if num - v - i >=0:
    #             lis.append((k,j))
    # last_list = []
    # for i,v in enumerate(lis):
    #     if v[::-1] in lis and v[::-1] not in last_list:
    #         last_list.append(v)
    # return  last_list
    lis = []           
    for i,v in enumerate(list(d.values())):
        lis.extend([x for x in combinations(d.values(),len(d.values())-i)])    
    lis = [x for x in lis if sum(x)<=num]
    last = [list(map(lambda z:tuple(k for k,v in d.items() if d[k]==z) ,x)) for x in lis]    
    last = [sum(x,()) for x in last]
    return last



print(task_3(dit,56))  



'''
Три друга взяли вещи в поход. Сформируйте 
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного 
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции 
с множествами. Код должен расширяться 
на любое большее количество друзей

'''


dit = {'миша':('веревка',"еда","вода"),
       'паша':("еда","вода","палатка"),
       'саша':("еда","вода","текила"),
       'маша':("еда","вода","веревка"),}

def question_1(d:dict)-> None:
    lis = list(map(set,d.values()))
    print(f'Есть у всех : {set.intersection(*lis)}')
    print(f'{set.difference(*lis) if set.difference(*lis) else set.difference(*lis[::-1])}')
    '''
    Не получаеться понять как сделать с помощью методов set,при измене вещей всё идёт крахом и выводы не верные
    '''
print(question_1(dit))   

