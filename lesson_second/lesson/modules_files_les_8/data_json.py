import json
import os


__all__ = ['create_data_js']

def create_data_js(end_file=os.getcwd())-> None:
    while True:
        end = input('Для выхода введите exit или enter чтобы продолжить: ')
        if 'exit' == end:
            break
        name = input('Введите имя: ')
        id_ = input('Введите id: ')
        level = input('Введите уровень доступа: ')

        with open(f'{end_file}\Test_file\\test.json','r+',encoding='utf-8') as f:
            try:
                read_ : dict = json.load(f)
                vulues = [x for x in read_.values()]
            except json.decoder.JSONDecodeError:
                vulues = []
                read_ = {}
            if level not in read_:
                if not any(map(lambda x: id_ in x , vulues)):
                    read_[level] = {id_:name}
                
            else:
                if not any(map(lambda x: id_ in x , vulues)):        
                    read_.setdefault(level,{}).update({id_:name})
                
            with open(f'{end_file}\Test_file\\test.json','w+',encoding='utf-8') as rezul:
                json.dump(read_,rezul,ensure_ascii=False,indent=2,sort_keys=True)