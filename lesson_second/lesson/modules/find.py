from random import randint


__all__ = ['find_number']


def find_number(low: int, high: int, count: int)->bool:
    num = randint(low, high)
    n=input(f"Угадайте число от {low} до {high}: ")
    try:
        n = int(n)
        while count != low:
            if n > num:
                count -=1
                print(f'Введённое число {n} больше загадонного\n'
                      f'У вас осталось {count} попыток\n') 
                n= int(input(f"Угадайте число от {low} до {high}: "))
                
            elif n < num:
                count -=1
                print(f'Введённое число {n} меньше загадонного\n'
                      f'У вас осталось {count} попыток\n') 
                n= int(input(f"Угадайте число от {low} до {high}: "))
                
            else:
                return True
        else:
           return False        
    except ValueError:
        print('Не верный символ\n'
              'Завершение программы\n')

if __name__ == '__main__':
    print(find_number(1,100,20)) 