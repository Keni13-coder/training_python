'''
self_.name - защищенный атрибут
def _method - защищенный метод
self.__name - приватный атрибут
def __method - приватный метод
super().__init__(параметры например: *args, **kwargs) - позволяет унаследовать у ближайщего родителя параметры инита
'''

'''
Приватный метод (свойство) (он же private) - такой метод (свойство), доступ к которому можно получить только из того же класса (или объекта того же класса).
Защищенный метод (свойство) (он же protected) - такой метод (свойство), доступ к которому можно получить только из того же класса (или объекта того же класса)
и из его наследников.
'''

'''
Множественное наследование: 
class Hero(Person, Adress, Weapon)- класс Hero наследуеться от классов Person, Adress, Weapon, в зависимсти очерёдности будет идти иницилизация методов
def Hero __init__ будет принемать все параметры классов, а дальше :
    Person.__init__(self, All)
    Address.__init__(self, All)
    Weapon.__init__(self, All)
    Class.mro() - для понимание кто у кого родитель
'''


'''
Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
'''
from math import  pi
import random


class Circle:
    PI = pi
    NUMBER = 2
    
    def __init__(self, radius) -> None:
        self.radius = radius
        
        
    def len_circle(self)->float:
        return  self.NUMBER * self.PI * self.radius
    
       
    def area_circle(self)-> float:
        return self.PI * self.radius ** self.NUMBER
    
    
# test_ = Circle(50)
# print(test_.len_circle())     
# print(test_.area_circle())   


'''
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
'''


class Rectangle:
 
    
    def __init__(self, length, width=0) -> None:
        self.length = length
        if not width:
            width = length
        self.width = width

           
    def perimeter_rectangle(self) -> int|float:
        return  2 * (self.length + self.width)
    
    
    def area_rectangle(self)-> int|float:
        return self.length * self.width 



# test_2 = Rectangle(2)

# print(test_2.area_rectangle())



'''
Задание №3
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
'''



class People:
    
    
    def __init__(self, surname: str, name: str, patronymic: str, age: int) -> None:
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self._age = age
    
        
    def birthday(self)->None:
        self._age += 1
        
    
    def get_age(self) -> int:
        age = self._age
        return age
    
    
    def full_name(self) -> str:
        return f'{self.surname} {self.name} {self.patronymic}'
    
    
# test_3 = People('Узбеков',"Фёдр","Хуевич",34)
# test_3.birthday()  
# test_3.birthday()   
# print(test_3.get_age())    
# print(test_3.full_name())


'''
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
''' 


class worker(People):
    NUM_DEL = 7
    MIN_NUMBER = 100_000
    MAX_NUNBER = 999_999
    
    
    def __init__(self, surname: str, name: str, patronymic: str, age: int, id_: int) -> None:
        if id_ < self.MIN_NUMBER:
            id_ = random.randint(self.MIN_NUMBER,self.MAX_NUNBER)
        self.id_ = id_
        super().__init__(surname, name, patronymic, age)
        
        
    def access_level(self):
        return sum(map(int, str(self.id_).split())) % self.NUM_DEL
    
    
    def get_id(self):
        return self.id_
    
# test_4 = worker('Узбеков',"Фёдр","Хуевич", 34, id_= 86)
# print(test_4.access_level())            
# print(test_4.get_id())            





'''
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
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
    
    
    def __init__(self, name, age, weight, price) -> None:
        self.price = price
        super().__init__(name, age, weight)
    
    
    def get_pig(self)-> float:
        price = self.price / (self.PERCENT * self._age)
        return price



class Fish(Animals):
    
    
    def __init__(self, name: str, weight: int, age: int, isfly: bool = False) -> None:
        self.isfly = isfly
        super().__init__(name, weight, age)

    
    def get_fish(self):
        return f'Рыба и именем {self._name} - {"летающая" if self.isfly else "не летающая"}'
  
  


class Bird(Animals):
    MAX_AGE = 5
    
    
    def __init__(self, name: str, weight: int, age: int) -> None:
        super().__init__(name, weight, age)


    def get_bird(self):
        return 'будет жить' if max(0,self.MAX_AGE - self._age) else f'Птице c именем {self._name} хана'







# test_2 = Pig('котя',7,16,44)
# test_3 = Fish('',13,1)
# test_4 = Bird('Вася',3,5)
# print(test_4.get_bird())
# print(test_3.get_fish())
# print(test_2.get_all())
# print(test_2.get_pig())



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
    
    
    def __init__(self,name_othen: object,*args) -> None:
        self.rezul = name_othen(*args) 
        
        
    def create_class(self):
         return self.rezul
     
     
     
     
test_5 = Factory(Bird,'Вася',3,5)
print(test_5.create_class())
test_6 = test_5.create_class()
print(test_6.get_bird())