'если производить импорт со звездочкой делаем __all__ = [название наших объектов]'

'создание пакетов производиться с помощью файла __init__ можно и пустого, пакет может быть вложенным'
'пакет состоит из папки и файлом __init__ в нутри, так же там есть модули и возможно другие пакеты'
'sys argv - для получение списка элементов при вводе в командной строке через консоль'

from modules.find import find_number as find
import modules.secret as secr
from sys import argv as ar
import modules.calendar as cal
from modules.queen_of_chess import  *

# def main():
#     arguments = ar[1:]
#     funk = find(*map(int,arguments))
#     if funk:
#         return "все класс"
#     return "не класс"
# # secr.dictionary_secret()
# # print(secr.rezul_dict())
# print(cal.date('29.02.2001'))

print(main())