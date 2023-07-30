import json
from errors import my_errors as er


'''
Задание №1
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
'''


def task_1():
    number = input('Введите число: ')
    while not isinstance(number, (int, float)):
        try:
            number = int(number)
            return number
        except ValueError:
            try:
                number = float(number)
                return number
            except ValueError:
                number = input('Введите число: ')

# task_1()


'''
Задание №2
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
'''

def get_dict(dict_: dict, key: int, default: int=0):
    try:
        return dict_[key]
    
    except KeyError:
        return default
    
    
    
# d = {1:'asd',2:'чикатило'}
# print(get_dict(d,7,5))  


'''
Задание №3
Создайте класс с базовым исключением и дочерние классы-исключения:
○ ошибка уровня,
○ ошибка доступа.
''' 




'''
Задание №4
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
'''


class User:
    __slots__ = ['name', 'id_' , 'level']
    
    
    def __init__(self, name: str, id: int, level: int) -> None:
        self.name = name
        self.id_ = id
        self.level = level
    
    
    def __str__(self) -> str:
        return f'Пользователь {self.name} с id {self.id_} имеет уровень доступа {self.level}'
    
    
    def __eq__(self, __value: object) -> bool:
        return self.id == __value.id and self.name == __value.name
        
    
    def __ne__(self, __value: object) -> bool:
        return self.id == __value.id and self.name == __value.name






def create_user(path: str):
    with open(f'{path}\\test.json',encoding='utf-8') as f:
        reader = json.load(f)
    users = set()
    for k, v in reader.items():
        value = list(v.items())
        rezul = [(k,)] + value 
        rezul = sum(rezul,())[::-1]
        users.add(str(User(*rezul)))
    return users




'''
Задание №5
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
'''


class FullUser:
    '''Делает проверку соответсвий аккаунтов'''
    def __init__(self) -> None:
        self.__set_users = self.__create_user()
        self.tempuseless = None

    @staticmethod
    def __create_user(path: str='D:\Repository\\training_python\Test_file'):
        with open(f'{path}\\test.json',encoding='utf-8') as f:
            reader = json.load(f)
        users = set()
        for k, v in reader.items():
            value = list(v.items())
            rezul = [(k,)] + value 
            rezul = sum(rezul,())[::-1]
            users.add(str(User(*rezul)))
        return users

    
    
    def __eq__(self, __value: object) -> bool:
        return __value.user in self.__set_users
        
    
    def __ne__(self, __value: object) -> bool:
        return __value.user in self.__set_users
    
    
    def enter_system(self,my_name, my_id):
        '''Вход в систему'''
        new_user = User(my_name, my_id ,0)
        if new_user not in self.__set_users:
            raise er.AccessError(f'Данной учетной записи не существует User({my_name},{my_id})')
        else:
            for user in self.__set_users:
                if new_user == user:
                    self.tempuseless = user
                    return self.tempuseless
            
    def add(self, name, id_, level):
        '''Добавление аккаунта'''
        if self.tempuseless.level > level:
            raise er.LevelError(f'Уровень пользователя {self.tempuseless.name} не может превышать {level}')
        
        else:
            new_user = User( name, id_, level)
            self.__set_users.add(new_user)
            return new_user
        
    def get_info(self):
        '''Получение информации о пользователях'''
        return self.__set_users
    
    
    def __repr__(self) -> str:
        return f'< class FullUser >'
    
    
    def __str__(self):
        return f'< class FullUser >'
        
        
        
        
        
        
        
