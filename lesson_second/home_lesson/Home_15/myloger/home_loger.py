import logging
from typing import Callable
from functools import wraps

__all__ = ['write_log']

def write_log(funk: Callable)->Callable[[any],None]:
    @wraps(funk)
    def wrapper(*args,**kwargs)-> None:
        
        FORMAT = '{levelname:<8} - {asctime}. В файле "{name}", записала сообщение: {msg}'
        logger = logging.getLogger(__name__)
        logging.basicConfig(filename=f'log\{funk.__name__}.log.', filemode='w', encoding='utf-8', format=FORMAT, style='{', level=logging.INFO)
        
        try:
            rez = {f'{args}':funk(*args,**kwargs)}
            logger.info(f'Функция с именем {funk.__name__}, имея аргументы {[*args, *kwargs]} выдает результат {rez}')
        except Exception as ex:
            logger.error(f'Функция с именем {funk.__name__}, имея аргументы {[*args, *kwargs]} выдает результат {ex}')                
    
    return wrapper