from collections import defaultdict
import os
import pickle
import json
import csv
import random as rd


'''
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
'''
'''
Задание №6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
'''

class Animals:

    
    def __init__(self, name: str, weight: int, age: int) -> None:
        self._name = name
        self._age = age
        self._weight = weight
        
        
        
    def get_all(self) -> str:
        return f'Имя = {self._name}, Вес = {self._weight}, Возраст = {self._age}'
    
    
    
  

class Pig(Animals):
    PERCENT = 100
    
    
    def __init__(self, name: str, age: int, weight: int, price: int) -> None:
        self.price = price
        super().__init__(name, age, weight)
    
    
    def get_pig(self)-> float:
        price = self.price / (self.PERCENT * self._age)
        return price



class Fish(Animals):
    
    
    def __init__(self, name: str, weight: int, age: int, isfly: bool = False) -> None:
        self.isfly = isfly
        super().__init__(name, weight, age)

    
    def get_fish(self) -> str:
        return f'Рыба и именем {self._name} - {"летающая" if self.isfly else "не летающая"}'
  
  


class Bird(Animals):
    MAX_AGE = 5
    
    
    def __init__(self, name: str, weight: int, age: int) -> None:
        super().__init__(name, weight, age)


    def get_bird(self) -> str:
        return 'будет жить' if max(0,self.MAX_AGE - self._age) else f'Птице c именем {self._name} хана'



'''
Доработаем задачи 5-6. Создайте класс-фабрику. 
○ Класс принимает тип животного (название одного из созданных классов) 
и параметры для этого типа. 
○ Внутри класса создайте экземпляр на основе переданного типа и 
верните его из класса-фабрики.
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация 
данных), которые вы уже решали. Превратите функции в методы класса, а 
параметры в свойства. Задачи должны решаться через вызов методов 
экземпляра. 
'''


class Factory:
    
    
    def __init__(self, name_othen: object, *args, **kwargs) -> None:
        self.rezul = name_othen(*args, **kwargs) 
        
        
    def create_class(self) -> object:
        return self.rezul
     
     
     
# test_3 = Bird('Петя',3,5) 
# test_5 = Factory(Bird,'Вася',3,5)
# print(test_5.create_class())
# test_6 = test_5.create_class()
# print(test_6.get_bird())



class File_work:
    
    
    def __init__(self, start_file: str=os.getcwd(), end_file: str=os.getcwd()) -> None:
        self.start_file = start_file
        self.end_file = end_file

    
    
    def full_info_all_files(self)-> None:
        d = defaultdict(dict)
        for dir_, folders, files in os.walk(self.start_file):
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
            with (open(f'{self.end_file}\home_task.json','w',encoding='utf-8') as json_file,
                open(f'{self.end_file}\home_task.csv','w',encoding='utf-8',newline='') as csv_file,
                open(f'{self.end_file}\home_task.pickle','wb') as pickle_file):
                json.dump(d,json_file,ensure_ascii=False,indent=2)
                writer = csv.DictWriter(csv_file,fieldnames=[*d.keys()])
                writer.writeheader()
                writer.writerow(d)
                pickle.dump(d,pickle_file)
                
                
    def csv_to_js(self)->None | str:
        try:
            with (open(self.start_file,'r',newline='',encoding='utf-8') as file,
                open(self.end_file,'w',encoding='utf-8') as rezul_file):
                
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
        
        
             
    def js_to_pickle(self)-> None:
        for dirs, folders, files in os.walk(self.start_file):
            for file in files:
                if file.endswith('json'):
                    with (open(f'{dirs}/{file}','r',encoding='utf-8') as f,
                        open(f'{dirs}/{file.rstrip(".json")}.pickle','wb') as rezul):
                        new_file = json.load(f)
                        pickle.dump(new_file,rezul) 
                        
                        
    def pickle_to_csv(self)-> None|str:
        try:
            with (open(self.start_file,'rb') as pic_file,
                open(f'{os.getcwd()}\\rezul.csv','w',newline='',encoding='utf-8')as rezul):
                reader = pickle.load(pic_file)
                writer = csv.DictWriter(rezul,fieldnames=[*reader.keys()])
                writer.writeheader()
                writer.writerow(reader)                               
        except FileNotFoundError:
            return 'Файл не найден'
        
        
        
# task  = File_work('keni13\Lesson_python\lesson_second\lesson')
# task.full_info_all_files()