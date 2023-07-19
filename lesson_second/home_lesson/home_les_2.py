from fractions import Fraction
from functools import reduce
'''
Задание №6
Напишите программу банкомат. 
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой 
операцией, даже ошибочной
✔ Любое действие выводит сумму дене

'''
def task_6():
    summa = 0
    LIST = ('50','100','150','500','1000','5000','Другое','Выход')
    percent = 1.5
    count = 0
    TAX = 10
    def action():
        nonlocal summa
        nonlocal count
        nonlocal percent
        nonlocal TAX
        print('Выберите следующие действия\n'
              '1: Пополнить\n'
              '2: Снять\n'
              '3: Выйти\n')
        choice = input('Введите номер дейстия: ').strip()
        while  not choice.isdigit():
            print('Выберите следующие действия\n'
              '1: Пополнить\n'
              '2: Снять\n'
              '3: Выйти\n')
            choice = input('Введите номер дейстия: ').strip()
        else:
            while choice != '3':
                if choice == '1': # Пополнение счета
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
                        else:
                            print('Данное число не найдено')     
                    elif replenish == 'Другое':
                        try:
                            replenish = int(input("Введите другое число для пополнение: ").strip())
                            summa += int(replenish)
                            count += 1
                            print(f'Вашь баланс на данный момент состовляет {summa}')
                        except  ValueError:
                            print('Был введён не коректый символ\nЗавершение программы...')
                    elif replenish == 'Выход':
                        print('Выберите следующие действия\n'
                        '1: Пополнить\n'
                        '2: Снять\n'
                        '3: Выйти\n')
                        choice = input('Введите номер дейстия: ').strip()
                        while  not choice.isdigit():
                            print('Выберите следующие действия\n'
                            '1: Пополнить\n'
                            '2: Снять\n'
                            '3: Выйти\n')
                            choice = input('Введите номер дейстия: ').strip()
                    else:
                        print('Данный вариант не найден')
                elif choice == '2': # Снятие денег
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
                                count += 1
                                print(f'Вашь баланс на данный момент состовляет {summa}')
                        except  ValueError:
                            print('Был введён не коректый символ\nЗавершение программы...')
                    elif replenish == 'Выход':
                        print('Выберите следующие действия\n'
                        '1: Пополнить\n'
                        '2: Снять\n'
                        '3: Выйти\n')
                        choice = input('Введите номер дейстия: ').strip()
                        while  not choice.isdigit():
                            print('Выберите следующие действия\n'
                            '1: Пополнить\n'
                            '2: Снять\n'
                            '3: Выйти\n')
                            choice = input('Введите номер дейстия: ').strip()


    return action()
task_6()







'''
Напишите программу, которая получает целое 
число и возвращает его шестнадцатеричное 
строковое представление. Функцию hex 
используйте для проверки своего результата.

'''

def number_translation(m:int, n=2) -> str:
    suma = ''
    d = {10:'A', 11:'B',12:'C',13:'D',14:'E',15:'F'}
    while m >= 1:
        if m % n == 0:
            suma += str(m % n)
            m = m // n
        elif (m % n) >9:
            suma += d[(m % n)]
            m = m // n
        else:
            suma += str(m % n)
            m = m // n 
    return f'{suma[::-1]}'
print(number_translation(934,16))




'''
Напишите программу, которая принимает две строки 
вида “a/b” — дробь с числителем и знаменателем. 
Программа должна возвращать сумму 
и *произведение дробей. Для проверки своего 
кода используйте модуль fractions.
'''

"Вариант 1"
def test(st_1:str,st_2:str)-> float:
    return f'сумма: {(eval(st_1)+eval(st_2))}\nпроизведение: {eval(st_1)*eval(st_2)}'

# print(test('3/4','5/7'))
# first = Fraction(3, 4)
# second = Fraction(5, 7)
# rez_1 = first + second
# rez_2 = first * second
# print(rez_1,rez_2) 


"Вариант 2"

def test(st_1:str,st_2:str)->str:
    st_1 = list(map(int,st_1.split('/')))
    st_2 = list(map(int,st_2.split('/')))
    last_st_1= [i*st_2[1] for i in st_1]
    last_st_2 =[i*st_1[1] for i in st_2]
    final_list = list(zip(last_st_1,last_st_2))
    first_number_sum =sum(final_list[0])
    second_number_sum = list(set(final_list[1]))[0] 
    for x in range(10,1,-1):
        if first_number_sum % x == 0 and second_number_sum % x == 0:
            first_number_sum //=x
            second_number_sum //=x
    summa = f"{first_number_sum}/{second_number_sum}"
    s = list(map(lambda x: reduce(lambda i,z:i*z,x),zip(st_1,st_2)))
    for i in range(10,1,-1):
        if s[0] % i ==0 and s[1] % i==0:
            s[0] //= i
            s[1] //= i
    multiplication = "/".join(map(str,s))
    return f'сумма = {summa}\nпроизведение = {multiplication}'

# f'сумма = {summa}\nпроизведение = {multiplication}'
# '/'.join(map(str,map(lambda x: reduce(lambda i,z:i*z,x),zip(st_1,st_2))))

print(test('4/6','3/7'))

first = Fraction(4, 6)
second = Fraction(3, 7)
rez_1 = first + second
rez_2 = first * second
print(rez_1,rez_2)


