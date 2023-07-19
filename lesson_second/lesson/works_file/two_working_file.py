from itertools import cycle


__all__ = ['duo']

# слишком ситуативная функция, не знаю что с ней делать
def duo(first_file_name: str, second_file_name: str)-> None:
    with (
        open(f'{first_file_name}','r',encoding='utf-8') as first_file,
        open(f'{second_file_name}', 'r',encoding='utf-8') as second_file,
        open(f'rezul.txt','a',encoding='utf-8') as rezul 
        ):
        name_list = list(map(lambda x: x.replace('\n',''),first_file.readlines()))
        number_list = list(map(lambda x: x.split('|'),second_file.readlines()))
        rezul_num = [int(y) * float(x.replace('\n','')) for (y,x) in number_list]
        if len(number_list) >= len(name_list): 
            rezul_ = list(zip(rezul_num,cycle(name_list)))
            for (y,x) in rezul_:
                if y > 0:
                    rezul.write(f'{x.upper()}:{int(y)}\n')
                else:
                    rezul.write(f'{x.lower()}:{abs(y)}\n')   
        else:
            rezul_ = list(zip(name_list,cycle(rezul_num)))
            for (y,x) in rezul_:
                if x > 0:
                    rezul.write(f'{y.upper()}:{int(x)}\n')
                else:
                    rezul.write(f'{y.lower()}:{abs(x)}\n')
                    
if __name__ == '__main__':
    duo('TESTING_name','TESTING')                  