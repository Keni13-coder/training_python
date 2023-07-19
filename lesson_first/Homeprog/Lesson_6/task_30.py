'''
Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''
def task30(number, difference, count):
    ls = [number]
    suma = number
    for x in range(count - 1):
        suma += difference
        ls.append(suma)
    return ls



print(task30(7,2,5))

def task30(number, difference, count):
    return [number] if count == 1 else  [number] + task30(number + difference,difference,count-1)


print(task30(7,2,5))


def task30(number, difference, count):
    return [number + x * difference for x in range(count)]


print(task30(7,2,5))
