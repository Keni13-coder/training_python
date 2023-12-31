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