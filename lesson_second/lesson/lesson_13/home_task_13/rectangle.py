from errors import my_errors as er


class Rectangle:
    '''Класс для подсчёта периметра и площади прямоугольника'''
    def __init__(self, length, width=0) -> None:
        if length < 0 or width < 0:
            raise er.LessThanZero()
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