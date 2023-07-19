import random as rd


__all__ = ['numeric']


def numeric(number_row:int, file_name:str)->None:
    RANGE_NUMBER = 1000
    with open(f'{file_name}','a',encoding='utf-8') as file:
        for _ in range(number_row):
            file.write(f'{rd.randint(-RANGE_NUMBER,RANGE_NUMBER)} | {rd.uniform(float(-RANGE_NUMBER),float(RANGE_NUMBER)):.2f}\n')
            
            
if __name__ == '__main__':
    numeric(5,'TESTING')