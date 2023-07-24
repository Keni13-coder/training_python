from collections import defaultdict
from typing import Any


class Testr:
    def __init__(self, key, value) -> None:
        self.lis = defaultdict(int)
    
    def __call__(self, key, value) -> Any:
        self.lis[key] = value
        return dict(self.lis)

    
    def __str__(self) -> str:
        return f'{dict(self.lis)}'
    
    
    def __repr__(self) -> str:
        return 'Это класс хз зачем'
    
    
    
    
# d = Testr()
# s = d
# print(d('sdf',5))    
# print(d('78',5))
# print(s.lis)
print(Testr(1,2))
print(help(dict))


    