'''
Создайте класс студента. 
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и 
наличие только букв. 
○ Названия предметов должны загружаться из файла CSV при создании 
экземпляра. Другие предметы в экземпляре недопустимы. 
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты 
тестов (от 0 до 100). 
○ Также экземпляр должен сообщать средний балл по тестам для каждого 
предмета и по оценкам всех предметов вместе взятых.
'''
import csv
from collections import defaultdict
from typing import Any





class Student:
    
    
    def __init__(self, full_name: str) -> None:
        self.__create_csv()
    
    
    @staticmethod
    def __create_csv(path: str='lesson_second\home_lesson\Home_12'):
        start_subject = ['астрономия',
            'художественная литература',
            'этикет',
            'дизайн',
            'политология',
            'риторика',
            'психология']
        with open(f'{path}\subject.csv','w',encoding='utf-8',newline='') as file:

            writer = csv.writer(file,delimiter='\n')
            writer.writerows([start_subject])
    
    def __call__(self, subject, exam,grade ) -> Any:
         pass
    
# d = Student('asd')
rez = {'exam': {'астрономия': 5,'художественная литература': 3,},
      'grade': {'вастрономия': 4,'дизайн': 2}}

rez_exam = defaultdict(list)
for k,v in rez.items():
    for key,value in v.items():
            if k == 'exam':
                print(f"{key}: {value}")
                rez_exam[key].append(value)
print(rez_exam)
# продумать реализацию нахождения среднего значения всех тестов для каждого предмета и всех оценок 
