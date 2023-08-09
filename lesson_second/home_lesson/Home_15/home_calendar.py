from sys import argv as gv
from myloger import home_loger as lg





class Calendar():
    def __init__(self, date_str: str, bracket=gv[1:]) -> None:
        self.date_str = date_str
        self.bracket=bracket
        
    @lg.write_log
    def date(self)->bool:
        rezzul = []
        if self.bracket:
            d,m,y = [x for x in map(int,self.bracket)]
        else:    
            d,m,y = [x for x in map(int,self.date_str.split('.'))]
        if all((0 <d< 32, 0 <m< 13, 0 <y< 10000)):
            if m in [1,3,5,7,8,10,12]:
                rezzul.append(d <=31) 
            elif m in [4,6,9,11]:
                rezzul.append(d <=30) 
            else:
                if self.__year(y):               
                    rezzul.append(d ==29) 
                else:
                    rezzul.append(d ==28)             
        return all(rezzul)
    
    
    def __year(self, number: int)->bool:
        if (number % 4 == 0 or number % 400 == 0) and number % 100 != 0:
            return True
        return False

    
    def __repr__(self) -> str:
        return f'{self.bracket if self.bracket else self.date_str}'


match __name__:
    case '__main__':
        date = Calendar('29.02.2001')
        print(date.date())

        