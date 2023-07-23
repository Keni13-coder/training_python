'__str__ - для пользователя при принте или str'
'__repr__ - строка для создание экземпляра при копировании её кода, например вывод:  User(*args,**kwargs)'
'если есть __str__ и __repr__ чтобы получить 2 надо repr(), f"{user= }", или списком классов [user]'
'__add__ - сложенИе self + value'
'__radd__ - сложение value + self'
"сложение классов __add__(self othen) - self.(*args) + othen(*args)"

import time
'''Задание №1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)'''



class MyStr(str):
    ''' Класс наследуеться от str и хз зачем нужен'''
    def __new__(cls, value, name):
        '''создание класса с аргументами и установкой вермени '''
        instance = super().__new__(cls,value)
        instance.name = name
        instance.time = time.time()
        return instance

    
    def __repr__(self) -> str:
        """Предстовление класса"""
        return f' MyStr(vulue, name)'


    def __str__(self) -> str:
        """Выведет информацию по свойставам"""
        return f'Имя = {self.name}, Время = {self.time=}'

# d = MyStr('sdfsdf','vlad')
# print(f'{d}')   



'''
Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-архивов
list-архивы также являются свойствами экземпляра
'''

class Archive:
    # list_number = []
    # list_text = []
    # def __new__(cls, number: int, text: str):
    #     cls.instance = super().__new__(cls)
    #     cls.instance.list_number.append(number)
    #     cls.instance.list_text.append(text)
    #     return cls.instance
    '''Класс архив сохраняет переданные в него значения с каждым запуском'''
    _instance = None
    def __new__(cls, number: int, text: str):
        ''' создание и добовление списков с аргументами класса'''
        if cls._instance:
            cls._instance.list_number.append(number)
            cls._instance.list_text.append(text)
        else:
            cls._instance = super().__new__(cls)
            cls._instance.list_number = []
            cls._instance.list_text = []
            cls._instance.list_number.append(number)
            cls._instance.list_text.append(text)
        return cls._instance
    
    def __repr__(self) -> str:
        """Предстовление класса"""
        return f'Archive(number= {self.number}, text= {self.text})' 
    
    
    def __str__(self) -> str:
        '''Выводит информацию о свойствах класса для пользователя'''
        return f'Числа: {self.list_number} Запись: {self.list_text}'    

# b = Archive(15,'asdsad')
# c = Archive(15,'123')
# u = Archive(15,'123')
# print(u)    



'''
Задание №3
Добавьте к задачам 1 и 2 строки документации для классов.
'''
'''
Задание №4
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
'''

'''
Задание №5
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
'''



class Rectangle:
    '''Класс для подсчёта периметра и площади прямоугольника'''
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
    
          
# a = Rectangle(20,13)
# b = Rectangle(34,15)
# c = a + b
# print(b)







'''Создайте класс Матрица. Добавьте методы для:
○ вывода на печать, 
○ сравнения, 
○ сложения, 
○ *умножения матриц
'''

class Matrix:
    '''Класс созданный для сравнения, сложения и умножения матриц'''
    
    def __init__(self,matrix: list[list]) -> None:
        if len(set(map(len,matrix))) == 1:
            self._matrix = matrix
        else:
            
            self._matrix = []  
            

    def __repr__(self) -> str:
        """Предстовление класса Matrix """
        return f'Matrix(matrix= {self._matrix})'
    
    
    def __str__(self) -> str:
        return " <class 'Matrix'>"
    
    
    def __len__(self):
        ''' Позволяет получить длину classa Matrix'''
        return len(self._matrix)
    
    
    def __compare(self, matrix, __other: object) -> bool:
        ''' Проверяет схожесть эксемпляров класса Matrix, и наличие в них равных по длине элементов '''
        if str(self)  == str(__other):

            if any(map(bool, matrix) and map(bool,__other)):
                
                if len(matrix) == len(__other):

                    if len(matrix[0]) == len(__other[0]):
                        return True
            return False   

        else:
            if len(set(map(len, __other))) == 1:
                if matrix and __other[0]:
                    if len(matrix) == len(__other):
                        if len(matrix[0]) == len(__other[0]):
                            return True
            return False
        
                
    def __add__(self, __other: object):
        '''сложение эксемпляров класса Matrix с матрицой'''
        if self.__compare(self._matrix,__other):
            return self._matrix + __other
        else:
            return []

    
    def __radd__(self, __other: object):
        '''сложение матрицы с  эксемпляром класса Matrix'''
        if self.__compare(self._matrix,__other):
            return self._matrix + __other
        else:
            return []
    
    
    def __eq__(self, __other: object) -> bool:
        '''Проверка равенства матриц'''
        if self.__compare(self._matrix,__other):
            return self._matrix == __other
        else:
            return False
    
    
    def __ne__(self, __other: object) -> bool:
        '''Проверка  не равенства матриц '''
        if self.__compare(self._matrix,__other):
            return self._matrix != __other
        else:
            return False



    def __getitem__(self, key):
        '''Возможность обратиться по индеску к классу Matrix '''
        if self._matrix == []:
            raise IndexError('Из-за некоректной передачи данных, матрица равна []')
        return self._matrix[key]


    def __mul__(self, __other: object):
        '''Даёт возможность умножать экземпляры классов и матрицы'''
        if self.__compare(self._matrix, __other):
            if str(self) == str(__other):
                start = [[x[i] * y[i] for i,v in enumerate(x) ] for (x,y) in zip(self._matrix, __other) ]
            return start
        return [] 



    def __rmul__(self, __other):
        'Отрабатывает когда матрица слева, а экземпляр с права'
        if self.__compare(self._matrix, __other):
            if str(self) == str(__other):
                start = [[x[i] * y[i] for i,v in enumerate(x) ] for (x,y) in zip(self._matrix, __other) ]
            return start
        return [] 
    
    

  


