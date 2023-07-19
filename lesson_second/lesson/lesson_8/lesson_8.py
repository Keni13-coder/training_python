''' json.load(file) - из json файла получить объект пайтона,читает и преобразовывает
    json.loads(json_text) - преобразовывает текстовое представление json в объект питона
    json.dump(dict,file) - сохранение обекта питона в json file
    json.dumps() - сохранение обекта питона в json строку
    json.dump(ensure_ascii=False) - для отключение аске, чтоб бывол видно другие языки
    json.dump( indent - отвечает за переносы строк,
                separators - 2 параментра: символ между элементами и символ между ключём и значением
                sort_keys = True сортирует ключи, даже вложенные
'''
# import json
# a = 'Hello word'
# b = {key: value for key, value in enumerate(a)}
# c = json.dumps(b,indent=5,separators=(';','= '))
# print(c)

'''
wiht open(newline='')-для правельного чтения csv
csv.reader(file) - построчное чтение файла, строка являеться list 
csv.reader(file, dialect=excel-tab)-  в обычной чтение читаеться через зяпятую, через dialect=excel-tab мы говорим что разделитель TAB
csv.reader(file, quoting = csv.QUOTE_NONNUMERIC) - если число не было в кавчках, то преобразует в число

csv.writer(f) - обычная запись в файл
csv.writer.writerow(line) - сохранение списка в одной строке
csv.writer.writerows(all_data) - сохранение матрицы в нескольких строках
csv.writer(f, delimiter=) как разделять объекты меж собой (разделение столбцов)
csv.writer(f, quotechar=|) - если символы разделители уже есть, то они будут | (символ, использующийся для "склейки" поля, содержащего специальные символы,
такие как delimiter)
csv.DictReader(f,fieldanme=[],restkey=" ", restval =" ")-читает dict 
fieldanme- список загаловков столбцов, ключей словоря
restkey=" " - имя ключа для столбца которых нет в fieldanme
restval =" " - значение ключей fieldanme который нет в csv, если колонка есть а значений нет
csv.writer.writeheader() - сохранение первой строки с заговловками
csv.writer.writerow(line)
csv.writer.writerows(all_data)
'''


'''
Piclke
сериалезуем только то в чём уверены, может быть код консольный, будут проблемы
pickle.dump(my_dict,f)  - сохранение в бинарном файле
pickle.dumps(my_dict) - сохранение в бинарную строку
pickle.dumps(, protocol) - сериализация и десериализация может быть только с одинаковыми протоколами
                   Десериализация
pickle.load(f) - загрузка из бинарного файла в объект
pickle.loads(data) - получение объекта из бинарной строки
при сериализация и десериализация объектов на уровне модуля , объекты должны быть и там и там, иначе Pickle не поймет откуда взят файл
по факту он передёт имена функции или класса и если в файле будет такое же имя, Pickle подумает что это она и есть
'''

import json
import csv
import random as rd
from collections import defaultdict
import os
import pickle
'''
Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
'''

def task_1(file_name: str, end_file=os.getcwd())-> None:
    with (open(file_name,'r',encoding='utf-8') as f,
          open(f'{end_file}\Test_file\\test_js.json','w+',encoding='utf-8') as js):
        d = dict(x.replace('\n', '').capitalize().split(':')  for x in f)
        json.dump(d,js,indent=2,separators=(', ',':'))

        
    
    
'''
Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.

'''

def task_2(end_file=os.getcwd())-> None:
    while True:
        end = input('Для выхода введите exit или enter чтобы продолжить: ')
        if 'exit' == end:
            break
        name = input('Введите имя: ')
        id_ = input('Введите id: ')
        level = input('Введите уровень доступа: ')

        with open(f'{end_file}\Test_file\\test.json','r+',encoding='utf-8') as f:
            try:
                read_ : dict = json.load(f)
                vulues = [x for x in read_.values()]
            except json.decoder.JSONDecodeError:
                vulues = []
                read_ = {}
            if level not in read_:
                if not any(map(lambda x: id_ in x , vulues)):
                    read_[level] = {id_:name}
                
            else:
                if not any(map(lambda x: id_ in x , vulues)):        
                    read_.setdefault(level,{}).update({id_:name})
                
            with open(f'{end_file}\Test_file\\test.json','w+',encoding='utf-8') as rezul:
                json.dump(read_,rezul,ensure_ascii=False,indent=2,sort_keys=True)
                
                
                
                
'''
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
'''
def task_3(end_file=os.getcwd())-> None:
    try:
        with open(f'{end_file}\Test_file\\test.json','r',encoding='utf-8') as f:
            reader_ : dict= json.load(f)
            print(reader_)
            with open(f'{end_file}Test_file\\testing.csv','w',encoding='utf-8',newline='') as rez:
                writer = csv.DictWriter(rez,fieldnames=[*reader_.keys()])
                writer.writeheader()
                writer.writerow(reader_)
    except FileNotFoundError:
        return 'Файл не найден'



'''
Задание №4
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
'''


def task_4(star_file_csv: str, end_file_json: str)->None | str:
    try:
        with (open(star_file_csv,'r',newline='',encoding='utf-8') as file,
              open(end_file_json,'w',encoding='utf-8') as rezul_file):
            
            reader = [*csv.reader(file)]
            dict_reader = {head: row for (head,row) in zip(reader[0],reader[1])}
            dict_ = defaultdict(dict)
        
            for k,v in dict_reader.items():
                v: dict = json.loads(v.replace("'",'"'))
                for id_,name in v.items():
                    id_ = ''.join(str(rd.randint(1,9)) if i =='0' else i for i in id_.zfill(10))
                    dict_[k].update({id_ : name.capitalize()})
                    dict_['hash'].update({id_ : hash(id_ + name.capitalize())})
            json.dump(dict_, rezul_file, indent=2, ensure_ascii=False, sort_keys=True) 
                  
    except FileNotFoundError:
        return 'Файл не найден'
      
      
'''
Задание №5
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
'''    


def task_5(folder_name: str)-> None:
    for dirs, folders, files in os.walk(folder_name):
        for file in files:
            if file.endswith('json'):
                with (open(f'{dirs}/{file}','r',encoding='utf-8') as f,
                      open(f'{dirs}/{file.rstrip(".json")}.pickle','wb') as rezul):
                    new_file = json.load(f)
                    pickle.dump(new_file,rezul)
  
  
'''
Задание №6
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
'''  


def task_6(pickle_file: str)-> None:
    with (open(pickle_file,'rb') as pic_file,
          open(f'{os.getcwd()}\\rezul.csv','w',newline='',encoding='utf-8')as rezul):
        reader = pickle.load(pic_file)
        writer = csv.DictWriter(rezul,fieldnames=[*reader.keys()])
        writer.writeheader()
        writer.writerow(reader)





'''
Задание №7
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.
'''

def task_7(csv_file: str)->str:
    with open(csv_file,'r',encoding='utf-8',newline='') as file:
        reader = [*csv.reader(file)]
        dict_reader = {head: row for (head,row) in zip(reader[0],reader[1])}
        rezul = pickle.dumps(dict_reader)
        return rezul
    
    
'''
Задание
Решить задачи, которые не успели решить на семинаре.
Напишите функцию, которая получает на вход директорию и рекурсивно 
обходит её и все вложенные директории. Результаты обхода сохраните в 
файлы json, csv и pickle. 
○ Для дочерних объектов указывайте родительскую директорию. 
○ Для каждого объекта укажите файл это или директория. +
○ Для файлов сохраните его размер в байтах, а для директорий размер 
файлов в ней с учётом всех вложенных файлов и директорий.+
Соберите из созданных на уроке и в рамках домашнего задания функций 
пакет для работы с файлами разных форматов.
'''    


def task_home(directory_: str,end_directory:str)-> None:
    d = defaultdict(dict)
    for dir_, folders, files in os.walk(directory_):
        size = 0
        for path, dirs_2, fils in os.walk(dir_):
            for file in fils:
                way = f"{path}/{file}" 
                d['Size'].update({file : os.path.getsize(way)})
                d['file'].update({file:os.path.isfile(way)})
                d['dir'].update({file: os.path.isdir(way)})   
                size += os.path.getsize(way)
            for _dir in dirs_2:
                d['parent'].update({path:_dir})    

        d['Size'].update({dir_ : size})
        d['file'].update({dir_:os.path.isfile(dir_)}) 
        d['dir'].update({dir_: os.path.isdir(dir_)})  
        with (open(f'{end_directory}\home_task.json','w',encoding='utf-8') as json_file,
              open(f'{end_directory}\home_task.csv','w',encoding='utf-8',newline='') as csv_file,
              open(f'{end_directory}\home_task.pickle','wb') as pickle_file):
            json.dump(d,json_file,ensure_ascii=False,indent=2)
            writer = csv.DictWriter(csv_file,fieldnames=[*d.keys()])
            writer.writeheader()
            writer.writerow(d)
            pickle.dump(d,pickle_file)


if __name__ == '__main__':
    # task_1('rezul.txt')
    # task_2()        
    # task_3()
    # print(task_4('Lesson_python\lesson_second\lesson\\testing.csv','Lesson_python\lesson_second\lesson\\rezul.json'))
    # task_5('Lesson_python\lesson_second\lesson')
    # task_6('Lesson_python\lesson_second\lesson\\rezul.pickle')
    # print(task_7('rezul.csv'))
    # task_home('Lesson_python\lesson_second\lesson','Lesson_python\lesson_second\lesson\Test_file')
    pass
