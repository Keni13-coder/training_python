'''Задание №7
Функция получает на вход словарь с названием компании в качестве ключа 
и списком с доходами и расходами (3-10 чисел) в качестве значения. 
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании 
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
'''
dit = {"пидор":[100,-100,10],
       "Молодец":[100,-100,10],
       "чулбус":[200,-200,10],}
def task_7(di:dict)->bool:
    return all(sum(v)>0 for k,v in di.items())


# print(task_7(dit))





'''
Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
✔ Напишите функцию, которая при запуске заменяет содержимое переменных 
оканчивающихся на s (кроме переменной из одной буквы s) на None. 
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

'''





Skits = 2
Passbk = 0
Tribons = 4
srwar = 0
rezul = []
def task_8()->None:
    global rezul
    for x in globals():
        if x in ['Skits', 'Passbk', 'Tribons', 'srwar']: # Так как в 1 файле присутсвуют разные задачи, чтоб не было пересичений, иначе  not x.startswith('__') 
            if x.startswith(('s','S')):
                rezul.append(globals()[x])
                globals()[x] = None
            

print(task_8())
print(Skits,Passbk,Tribons,srwar)







'Напишите функцию для транспонирования матрицы'

matr = [[1,2,3],
        [3,4,5],
        [6,7,8]]
'''
[1,3,6]
[2,4,7]
[3,5,8]
'''

def transpose_matrix(matrix:list[list])->list[list]:
    return  list(map(list, zip(*matrix)))

# print(transpose_matrix(matr))






'''
✔ Напишите функцию принимающую на вход только ключевые 
параметры и возвращающую словарь, где ключ — значение 
переданного аргумента, а значение — имя аргумента. Если 
ключ не хешируем, используйте его строковое представление.
'''
def dz_2(**kwargs:dict)->dict:
    return {x:v for v, x in kwargs.items()}


# print(dz_2(кактам=32,может=50, нухз=100))






'''
Возьмите задачу о банкомате из семинара 2. Разбейте её 
на отдельные операции — функции. Дополнительно сохраняйте 
все операции поступления и снятия средств в список.
'''



summa = 0
LIST = ('50','100','150','500','1000','5000','Другое','Выход')
percent = 1.5
count = 0
TAX = 10
operation = {}
def task_choice()->str:
    print('Выберите следующие действия\n'
              '1: Пополнить\n'
              '2: Снять\n'
              '3: Выйти\n')
    choice = input('Введите номер дейстия: ').strip()
    while  not choice.isdigit() or choice >'3':
        print('Выберите следующие действия\n'
              '1: Пополнить\n'
              '2: Снять\n'
              '3: Выйти\n')
        choice = input('Введите номер дейстия: ').strip()
    return choice
           
def account_replenishment()->None|object:# Пополнение счета
    
    global summa,LIST,percent,count,TAX,operation
    print(f'Вашь баланс на данный момент состовляет {summa}')
    if summa > 5_000_000:
        percent = TAX 
    if count % 3 ==0:
        percent += 3
    print('Доступные варианты')
    [print(f'{v}',end='   ') if i != 2 and i != len(LIST)-1 else print(f'{v}')  for i,v in enumerate(LIST)]
    replenish = input('Введите число для пополнение: ').strip()
    while replenish not in LIST:
        print('Доступные варианты')
        [print(f'{v}',end='   ') if i != 2 and i != len(LIST)-1 else print(f'{v}')  for i,v in enumerate(LIST)]
        replenish = input('Введите число для пополнение: ').strip()
    if replenish.isdigit():
        if replenish in LIST:
            summa += int(replenish)
            print(f'Вашь баланс на данный момент состовляет {summa}')
            count += 1
            operation.setdefault('Пополнение',[]).append(replenish)
        else:
            print('Данное число не найдено')     
    elif replenish == 'Другое':
        try:
            replenish = int(input("Введите другое число для пополнение: ").strip())
            summa += int(replenish)
            operation.setdefault('Пополнение',[]).append(replenish)
            count += 1
            print(f'Вашь баланс на данный момент состовляет {summa}')
        except  ValueError:
            print('Был введён не коректый символ\nЗавершение программы...')
    elif replenish == 'Выход':
        return task_choice()
                
                
                
def account_withdrawal()->None|object: # Снятие денег
    global summa,LIST,percent,count,TAX,operation
    print(f'Вашь баланс на данный момент состовляет {summa}')
    if summa > 5_000_000:
        percent = TAX 
    if count % 3 ==0:
        percent += 3
    print('Доступные варианты')
    [print(f'{v}',end='   ') if i != 2 and i != len(LIST)-1 else print(f'{v}')  for i,v in enumerate(LIST)]
    replenish = input('Введите число для снятие наличных: ').strip()
    while replenish not in LIST:
        print('Доступные варианты')
        [print(f'{v}',end='   ') if i != 2 and i != len(LIST)-1 else print(f'{v}')  for i,v in enumerate(LIST)]
        replenish = input('Введите число снятие наличных: ').strip()
    if replenish.isdigit():
        if replenish in LIST:
            if summa - int(replenish) < 0:
                print("Не достаточно средств")
            else:
                replenish = int(replenish)
                summa -= replenish + (30 if (s := ((replenish / 100) * percent)) < 30 else 600 if s >600 else s)
                summa = f'{summa:.2f}'
                summa = float(summa)
                operation.setdefault('Снятие',[]).append(replenish)
                print(f'Вашь баланс на данный момент состовляет {summa}')
                count += 1
        else:
            print('Данное число не найдено')     
    elif replenish == 'Другое':
        try:
            replenish = int(input("Введите другое число снятие наличных: ").strip())
            if summa - int(replenish) < 0:
                print("Не достаточно средств")
            else:
                replenish = int(replenish)
                summa -= replenish + (30 if (s := ((replenish / 100) * percent)) < 30 else 600 if s >600 else s)
                summa = f'{summa:.2f}'
                summa = float(summa)
                operation.setdefault('Снятие',[]).append(replenish)
                count += 1
                print(f'Вашь баланс на данный момент состовляет {summa}')
        except  ValueError:
            print('Был введён не коректый символ\nЗавершение программы...')
    elif replenish == 'Выход':
        return task_choice()
                        


def action(num:str)->object|str:
    if num == '1':
        return account_replenishment()
    elif num == '2':
        return account_withdrawal()
    else:
        return 'Завершение программы'


    
def main()->object|str:
    flag = task_choice()
    while flag < '3':
        check = action(flag)
        if check is not None:
            flag = check
        else:
            flag = task_choice()

    else:
        print("Завершение програмыы")    
          
main()
print(operation)    
     
     
