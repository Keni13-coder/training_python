import json
import csv
import random as rd
from collections import defaultdict


__all__ = ['csv_to_js']

def csv_to_js(star_file_csv: str, end_file_json: str)->None | str:
    try:
        with (open(star_file_csv,'r',newline='',encoding='utf-8') as file,
              open(end_file_json,'w',encoding='utf-8') as rezul_file):
            
            reader = [*csv.reader(file)]
            dict_reader = {head: row for (head,row) in zip(reader[0],reader[1])}
            dict_ = defaultdict(dict)
        
            for k,v in dict_reader.items():
                v: dict = json.loads(v.replace("'",'"'))
                for id_,name in v.items():
                    id_ = ''.join(str(rd.randint(1,9)) if i =='0' else i for i in id_.zfill(10))
                    dict_[k].update({id_ : name.capitalize()})
                    dict_['hash'].update({id_ : hash(id_ + name.capitalize())})
            json.dump(dict_, rezul_file, indent=2, ensure_ascii=False, sort_keys=True) 
                  
    except FileNotFoundError:
        return 'Файл не найден'
      