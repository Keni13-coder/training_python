import csv
from collections import defaultdict
from typing import Any


class TestFullName:
    def __init__(self, name : str='name') -> None:
        self.name = name
        
    
    def __set_name__(self, owner, name):
        self.paran_name = f'_{name}'    


    def __get__(self, istance ,owner):
        getattr(istance, self.paran_name)
        
        
    def __set__(self, instance, value):
        if self.__validation(value):
            setattr(instance,self.paran_name,value)
        else:
            raise ValueError('Ошибка переданного ФИО')
        
        
    def __validation(self,name:str):
        name = name.split()
        return all(map(lambda x: x.istitle() and x.isalpha(),name))    
        
        
        
class Grade:
    def __init__(self, start : int=2, end : int=5) -> None:
        self.start = start
        self.end = end
    
    def __set_name__(self, owner, name):
        self.paran_name = f'_{name}'    


    def __get__(self, istance ,owner):
        getattr(istance, self.paran_name)
        
        
    def __set__(self, instance, value):
        if self.__validation(value):
            setattr(instance,self.paran_name,value)
        else:
            raise ValueError('Ошибка переданного значения: от 2 до 5')
        
    def __validation(self,value) -> bool:
        if self.start <= value <= self.end:
            return True
        return False
    
    
class Exam:
    def __init__(self, start : int=0, end : int=100) -> None:
        self.start = start
        self.end = end
    
    def __set_name__(self, owner, name):
        self.paran_name = f'_{name}'    


    def __get__(self, istance ,owner):
        getattr(istance, self.paran_name)
        
        
    def __set__(self, instance, value):
        if self.__validation(value):
            setattr(instance,self.paran_name,value)
        else:
            raise ValueError('Ошибка переданного значения: от 0 до 100')
        
    def __validation(self,value) -> bool:
        if self.start <= value <= self.end:
            return True
        return False
        








class Student:
    '''Высчитывает средние балы студента'''
    full_name = TestFullName()
    grade = Grade()
    exam = Exam()
    
    def __init__(self, full_name: str) -> None:
        # self.__create_csv()
        self.__results_dict = defaultdict(dict)
        self.full_name = full_name
    
    # @staticmethod
    # def __create_csv(path: str='lesson_second\home_lesson\Home_12'):
    #     '''Создание csv файла с предметами '''
    #     start_subject = ['астрономия',
    #         'художественная литература',
    #         'этикет',
    #         'дизайн',
    #         'политология',
    #         'риторика',
    #         'психология']
    #     with open(f'{path}\subject.csv','w',encoding='utf-8',newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerows([start_subject])
    
    def __call__(self, subject: str, exam: int, grade: int ) -> Any:
        '''Вызываеться у эксезпляра класса и позволят добовлять exam, grade в итог'''
        self.grade = grade
        self.exam = exam
        with open('D:\Repository\\training_python\lesson_second\home_lesson\Home_14\\files_py\subject.csv','r',encoding='utf-8',newline='') as file:
            if subject in file.read():
                try:
                    self.__results_dict['exam'][subject].append(exam)
                    self.__results_dict['grade'][subject].append(grade)
                except KeyError:
                    self.__results_dict['exam'][subject] = [exam]
                    self.__results_dict['grade'][subject] = [grade]
            else:
                raise ValueError('Данного предмета не существует')
    @property  
    def results_dict(self):
        '''Результаты выполнения работ, среднее значение'''
        resul  = {f'{k} : {key} = {sum(value) / len(value)}' for k,v in self.__results_dict.items() for key,value in v.items()}
        full_resul = {k: sum(lis := sum(v.values(), [])) / len(lis)  for k,v in self.__results_dict.items() }
        return f'Студент - {self._full_name}:\n{sorted(resul)}\n{full_resul}'
    
    
    def __repr__(self) -> str:
        return f'Student({self._full_name})'
    

    def __str__(self) -> str:
        return "< class 'Student' >"





if __name__ == '__main__':
    data = Student('Бочкин Cергей Бритьевич')
    print(data == "< class 'Student' >")