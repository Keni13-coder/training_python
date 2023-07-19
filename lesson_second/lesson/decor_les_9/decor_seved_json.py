from typing import Callable
import json
from functools import wraps


__all__ = ['write_json']

def write_json(path: str = 'Lesson_python\lesson_second\lesson\Test_les_9'):
    def main(funk: Callable)->Callable[[any],None]:
        @wraps(funk)
        def wrapper(*args,**kwargs)-> None:
            rez = {f'{args}':funk(*args,**kwargs)}
            
            try:
                with open(f'{path}\\{funk.__name__}.json','r+',encoding='utf-8') as rez_file:
                    reader_dict: dict = json.load(rez_file)
                    reader_dict.update(rez)
                    
                    with open(f'{path}\\{funk.__name__}.json','w',encoding='utf-8') as rez_file:
                        json.dump(reader_dict,rez_file, indent= 2, ensure_ascii= False, skipkeys=True)
                        
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                  
                with open(f'{path}\\{funk.__name__}.json','w',encoding='utf-8') as rez_file:
                    json.dump(rez,rez_file, indent= 2, ensure_ascii= False, skipkeys=True) 
                            
        return wrapper
    
    return main



if __name__ == '__main__':
    @write_json('Test_les_9\home_test')
    def test(num_first: int, num_second: int):
        return num_first + num_second
    
    print(test(1,5))    