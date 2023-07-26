'__call__ - позволяет экземпляру класса стать функцией'
'__iter__ - позволяет итерировать объект обычно пишеться  __iter__ и __next__ '
'__iter__ - чаще всего возвращает self,но если нет __next__ будет ошибка'
'__next__ - пишеться реализация нашей итерации по классу, в конце пишеться raise StopIteration'
'''
менеджер контекста with
__enter__ - начало исполняемого класса, если хотим указать явно что будет происходить с началом,  
    пример open : close.
Надо понимать что __enter__ ипользуеться с __exit__ который в свою очерь указывает явно что делат класс при завершении.
возвращает  self
'''
'__exit__ - всегда принемает self, exc_type, exc_val, exc_tb и ничего не возвращает'
'@property - являеться getter - нужен для образование нового свойста из защищённых, пишеться над методом для преобразование в новое свойство'
'@name.setter - имя такое же как у метода - нужен для изменение защищённых свойст и образование нового свойста'
'@name.delete - нужен для изменение поведение при коменде del метод пишиться заново потом к нему применяться декоратор'
'эти декораторы не нужны если  защищённые свойства никак не видоизменяться в методах. Например нет никаких условий и дополнений к __init__'
'__set_name__ - используется для получение имени переменной куда был записан класс, сработает в случае создание экземпляра класса в другом классе '
'__set_name__(self, owner, name) , где owner имя экземпляра класса при присвоении в поле класса <class __main__.owner>'
'__set__(self, instance, value): - instance ссылка на экземпляр класса где был присвоен дексриптор, value его значение'
'''class Test:
    x = дексриптор()
    def __init__(self,num)
        self.x = num
В этом примере instance будет равен ссылке на class Test 
а value будет переопределена 
'''
'__get__(self, instance ,owner) - instance ссылка на экземпляр класса где был присвоин дескриптор, owner  - ссылка на класс где был присвоин дескриптор'
'''
class Test:
    x = дексриптор()
    def __init__(self,num)
        self.x = num
d = Test()
d.y = 3
в этом примере в момент присвоения к 'd' свойство 'y', работает __get__        
'''
'''
class Testr:
    def __init__(self, *args, **kwargs) -> None:
        self.lis = defaultdict(int)
        if isinstance(*args,dict):
            self.lis.update(*args)
            self.lis.update(kwargs)
        else:    
            self.lis.update({z:y for x in args for z,y in x})
            self.lis.update(kwargs)
       
    
    def __call__(self, *args, **kwargs) -> dict:
        if isinstance(*args,dict):
            self.lis.update(*args)
            self.lis.update(kwargs)
        else:    
            self.lis.update({z:y for x in args for z,y in x})
            self.lis.update(kwargs)
        return Testr(self.lis)

    
    def __str__(self) -> str:
        # a = {z:y for x in self.args for z,y in x}
        return f'{dict(self.lis)}'
    
    
    def __repr__(self) -> str:
        return 'Это класс хз зачем'
    
    
    def __iter__(self):
        return iter(self.lis)
    
    
    def __add__(self, other):
        if isinstance(other,dict):
            self.lis.update(other)
        else:
            self.lis.update(other.lis)
        return Testr(self.lis)

    
    
# d = Testr()
# s = d
# print(d('sdf',5))    
# print(d('78',5))
# print(s.lis)
# print(Testr(1,2))

# a = Testr({1:2},sdfs=5)
# b = {1: 2, 'sdfs': 5, 7: 2, 'sfs': 5}




class Enter:
    def __init__(self, number, degree ) -> None:
        self.number =  number
        self.degree = degree
    
    # при старте блока with rezul = 2 * 2
    def __enter__(self):
        self.rezul = self.number * 2
        return self
    
    # когда выходим из блока with rezul = 2 ** 6
    def __exit__(self,exc_type, exc_val, exc_tb):
        self.rezul = self.number ** self.degree
        
        
# a = Enter(2,6)

# with a:
#     print(a.rezul)
    
# print(a.rezul)


class Discript:
    def __init__(self, number: int) -> None:
        self.number = number
        
    def __set_name__(self, owner, name):
        self.param_name = f'_{name}'
        print(self.param_name)  


    def __get__(self, instance ,owner):
        print(f'get {instance,owner}')
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        print(f'set {instance,value}')
        setattr(instance,self.param_name, value)
        
        
class DFSF:
    a = Discript(2)


    def __init__(self,number) -> None:
        self.a = number
        self.d = self.a

    # def __repr__(self) -> str:
    #     return f'a= {self.a}'

d = DFSF(4)
d.f = 6'''


from collections import defaultdict
from typing import Any
from itertools import islice
import json


'''
Задание №1
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
'''

class Factorial:
    
    
    def __init__(self, number) -> None:
        self.number = number
        self._full_info = {}
        
        
    def __call__(self, number) -> Any:
        self.number = number
        self.f = 1
        for x in range(1 ,number + 1 ):
            self.f *=  x
        self._full_info[self.number] = self.f
        return self.f
    
    
    @property    
    def full_info(self):
        max_len  = len(self._full_info) -1 
        return dict(islice(self._full_info.items(), max_len))
    
    
    @full_info.setter
    def full_info(self,value):
        raise ValueError('Данное свойства нельзя изменить')
        
    
    def __str__(self) -> str:
        return f'{self.f}'
    
    
    def __enter__(self): 
        self.file = open('lesson_second\lesson\lesson_12\Factorial.json','w',encoding='utf-8')
        json.dump(self.full_info, self.file, ensure_ascii=False, indent=2)
        return self
    
    
    def __exit__(self,exc_type, exc_val, exc_tb):
        self.file.close()

'''
Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
'''

# d = Factorial(5)
# print(d(4))
# d(5)
# d(6)
# with d:
#     d
# print()

'''
Задание №3
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
'''
class GenerFactorial:
    
    
    def __init__(self, stop:int, start: int=1,  step: int=1) -> None:
        self.stop = stop
        self.start = start
        self.step = step
        
    def __iter__(self):
        return self
    
    
    def __next__(self):
        if self.start < self.stop:
            f = 1
            for i in range(1,self.start + 1):
                f *=i
            self.start +=self.step
            return f    
        else:
            raise StopIteration
    
    
# f = GenerFactorial(15,5)    
# for x in f:
#     print(x)




'''
Задание №4
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
Задание №5
Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__
Задание №6
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
'''
class Positive:
    def __init__(self, num: int = 0) -> None:
        self.num = num

    def __set_name__(self, owner, name):
        self.param_name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance,self.param_name)
    
    def __set__(self, instance, value):
        if self.__validation(value):
            setattr(instance,self.param_name,value)
        else:
            raise ValueError('Число не может быть меньше 0')    
    
    @staticmethod
    def __validation(value) -> bool:
        if value < 0:
            return False
        return True


class Rectangle:
    '''Класс для подсчёта периметра и площади прямоугольника'''
    __slots__ = ['_length', '_width']
    length = Positive()
    width = Positive()
    
    
    def __init__(self, length, width=0) -> None:
        self.length = length
        if not width:
            width = length
        self.width = width

           
    def perimeter_rectangle(self) -> int|float:
        '''Находжение периметра прямоугольника'''
        return  2 * (self.length + self.width)
    
    
    def area_rectangle(self)-> int|float:
        '''Нахождение площади треугольника прямоугольника'''
        return self.length * self.width 


    def __add__(self, other):
        '''Скадывает периметры двух экземпляров класса Rectangle по средством метода perimeter_rectangle'''
        sum_perim = max(self.perimeter_rectangle() + other.perimeter_rectangle(),0)
        return Rectangle(sum_perim)
    
    
    def __sub__(self, other):
        'Вычитает периметры двух экземпляров класса Rectangle по средством метода perimeter_rectangle'
        sum_perim = max(self.perimeter_rectangle() - other.perimeter_rectangle(),0)
        return Rectangle(sum_perim)
    
    
    def __radd__(self, other):
        '''Отрабатывает если __add__ ушёл в ошибку,
        скадывает периметры двух экземпляров класса Rectangle по средством метода perimeter_rectangle'''
        sum_perim = max(other.perimeter_rectangle() + self.perimeter_rectangle(),0)
        return Rectangle(sum_perim)
    
    def __rsub__(self, other):
        '''Отрабатывает если __sub__ ушёл в ошибку,
        вычитает периметры двух экземпляров класса Rectangle по средством метода perimeter_rectangle'''
        sum_perim = max(other.perimeter_rectangle() - self.perimeter_rectangle(),0)
        return Rectangle(sum_perim)
    
    
    def __lt__(self, other) -> bool:
        ''' Производит сравнение < экземпляров класса Rectangle по периметру'''
        return self.perimeter_rectangle() < other.perimeter_rectangle()
        
    def __le__(self, other) -> bool:
        ''' Производит сравнение <= экземпляров класса Rectangle по периметру'''
        return self.perimeter_rectangle() <= other.perimeter_rectangle()
        
    
    def __eq__(self, other) -> bool:
        ''' Производит сравнение == экземпляров класса Rectangle по периметру'''
        return self.perimeter_rectangle() == other.perimeter_rectangle()
        
        
    def __ne__(self, other) -> bool:
        ''' Производит сравнение != экземпляров класса Rectangle по периметру'''
        return self.perimeter_rectangle() != other.perimeter_rectangle()
        
        
    def __gt__(self, other) -> bool:
        ''' Производит сравнение > экземпляров класса Rectangle по периметру'''               
        return self.perimeter_rectangle() > other.perimeter_rectangle()
        
        
    def __ge__(self, other) -> bool:
        ''' Производит сравнение >= экземпляров класса Rectangle по периметру'''
        return self.perimeter_rectangle() >= other.perimeter_rectangle()
        
        
    def __str__(self) -> str:
        '''Выводит информацию о имени и типе Rectangle'''
        return " <class 'Rectangle'>"
        
    def __repr__(self) -> str:
        """Предстовление класса"""
        return   f'Rectangle(lengt = {self.length}, width = {self.width})'
    
    # @property
    # def length(self):
    #     return self.length
    
    
    # @length.setter
    # def length(self,value):
    #     if value < 0:
    #         raise ValueError('Число не может быть меньше 0')
    #     self.length = value
        
      
    # @property
    # def width(self):
    #     return self.width
    
    
    # @width.setter
    # def width(self,value):
    #     if value < 0:
    #         raise ValueError('Число не может быть меньше 0')
    #     self.width = value

    
    

                

    
# class Test:
#     def __new__(cls,num):
#         instance = super().__new__(cls)
#         instance.lis = [x for x in range(num)]
#         return instance.lis
#     def __init__(self,num) -> None:
#         self.num = num
        
        
        
# d = Rectangle(2,2)

# print(d.perimeter_rectangle()) 

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



