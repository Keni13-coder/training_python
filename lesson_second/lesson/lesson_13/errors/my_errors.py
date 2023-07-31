__all__ = ['LevelError','AccessError','RangeError','NameError','LessThanZero']



class MainError(Exception):
    def __init__(self, text: str='') -> None:
        self.text = ''.join(text)
        
        
    def __str__(self) -> str:
        return f'{self.text}'

class LevelError(MainError):
    def __init__(self, text: str='') -> None:
        super().__init__(text)
        
        

class AccessError(MainError):
    def __init__(self, text: str='') -> None:
        super().__init__(text)


class NameError(MainError):
    def __init__(self, text: str='') -> None:
        super().__init__(text)


class RangeError(MainError):
    def __init__(self, text: str='Не соответсвие заданного диапазона') -> None:
        super().__init__(text)


class LessThanZero(MainError):
    def __init__(self, text: str = 'Переданные переменные не могут быть меньше 0') -> None:
        super().__init__(text)
        


match __name__:
    case '__main__':
        raise LevelError()