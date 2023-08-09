from sys import argv as gv

from myloger import home_loger as lg

'''Напишите однострочный генератор словаря, который принимает 
на вход три списка одинаковой длины: имена str, ставка int, 
премия str с указанием процентов вида «10.25%». В результате 
получаем словарь с именем в качестве ключа и суммой 
премии в качестве значения. Сумма рассчитывается 
как ставка умноженная на процент премии 
'''





# @lg.write_log
# def task_2(names: list[str], bets: list[int], bonus:list[str], consol=gv[1:])->dict[str:int]:
#     if consol:
#         names, bets, bonus = consol
#         bets = map(int,bets)
#         return {name: bet / 100 * float(bon) for name, bet, bon in zip(names, bets, map(lambda x:x.replace('%',''),bonus))}
#     return {name: bet / 100 * print(float(bon)) for name,bet,bon in zip(names,bets,map(lambda x:x.replace('%',''),bonus))}



        
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
    
    
    def __init__(self, length, width=0, consol=gv[1:]) -> None:
        if consol:
            self.length, self.width= list(map(int, consol))
        else:
            self.length = length
            if not width:
                width = length
            self.width = width

    @lg.write_log
    def perimeter_rectangle(self) -> int|float:
        '''Находжение периметра прямоугольника'''
        return  2 * (self.length + self.width)
    
    @lg.write_log
    def area_rectangle(self)-> int|float:
        '''Нахождение площади треугольника прямоугольника'''
        return self.length * self.width 

    @lg.write_log
    def __add__(self, other):
        '''Скадывает периметры двух экземпляров класса Rectangle по средством метода perimeter_rectangle'''
        sum_perim = max(self.perimeter_rectangle() + other.perimeter_rectangle(),0)
        return Rectangle(sum_perim)
    
    @lg.write_log
    def __sub__(self, other):
        'Вычитает периметры двух экземпляров класса Rectangle по средством метода perimeter_rectangle'
        sum_perim = max(self.perimeter_rectangle() - other.perimeter_rectangle(),0)
        return Rectangle(sum_perim)
    
    @lg.write_log
    def __radd__(self, other):
        '''Отрабатывает если __add__ ушёл в ошибку,
        скадывает периметры двух экземпляров класса Rectangle по средством метода perimeter_rectangle'''
        sum_perim = max(other.perimeter_rectangle() + self.perimeter_rectangle(),0)
        return Rectangle(sum_perim)
    
    
    @lg.write_log
    def __rsub__(self, other):
        '''Отрабатывает если __sub__ ушёл в ошибку,
        вычитает периметры двух экземпляров класса Rectangle по средством метода perimeter_rectangle'''
        sum_perim = max(other.perimeter_rectangle() - self.perimeter_rectangle(),0)
        return Rectangle(sum_perim)
    
    
    @lg.write_log
    def __lt__(self, other) -> bool:
        ''' Производит сравнение < экземпляров класса Rectangle по периметру'''
        return self.perimeter_rectangle() < other.perimeter_rectangle()
    
    
    @lg.write_log
    def __le__(self, other) -> bool:
        ''' Производит сравнение <= экземпляров класса Rectangle по периметру'''
        return self.perimeter_rectangle() <= other.perimeter_rectangle()
        
    
    def __eq__(self, other) -> bool:
        ''' Производит сравнение == экземпляров класса Rectangle по периметру'''
        return self.perimeter_rectangle() == other.perimeter_rectangle()
        
    
    @lg.write_log
    def __ne__(self, other) -> bool:
        ''' Производит сравнение != экземпляров класса Rectangle по периметру'''
        return self.perimeter_rectangle() != other.perimeter_rectangle()
        
        
    @lg.write_log
    def __gt__(self, other) -> bool:
        ''' Производит сравнение > экземпляров класса Rectangle по периметру'''               
        return self.perimeter_rectangle() > other.perimeter_rectangle()
        
        
    @lg.write_log
    def __ge__(self, other) -> bool:
        ''' Производит сравнение >= экземпляров класса Rectangle по периметру'''
        return self.perimeter_rectangle() >= other.perimeter_rectangle()
        
        
    def __str__(self) -> str:
        '''Выводит информацию о имени и типе Rectangle'''
        return " <class 'Rectangle'>"
        
    def __repr__(self) -> str:
        """Предстовление класса"""
        return   f'Rectangle(lengt = {self.length}, width = {self.width})'
    
    
match __name__:
    case '__main__':
        test = Rectangle(2,5)
        test.area_rectangle()
