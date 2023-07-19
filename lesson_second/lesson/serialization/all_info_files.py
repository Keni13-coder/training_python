from collections import defaultdict
import os
import pickle
import json
import csv


__all__ = ['full_info_all_files']

def full_info_all_files(directory_: str,end_directory:str)-> None:
    d = defaultdict(dict)
    for dir_, folders, files in os.walk(directory_):
        size = 0
        for path, dirs_2, fils in os.walk(dir_):
            for file in fils:
                way = f"{path}/{file}" 
                d['Size'].update({file : os.path.getsize(way)})
                d['file'].update({file:os.path.isfile(way)})
                d['dir'].update({file: os.path.isdir(way)})   
                size += os.path.getsize(way)
            for _dir in dirs_2:
                d['parent'].update({path:_dir})    

        d['Size'].update({dir_ : size})
        d['file'].update({dir_:os.path.isfile(dir_)}) 
        d['dir'].update({dir_: os.path.isdir(dir_)})  
        with (open(f'{end_directory}\home_task.json','w',encoding='utf-8') as json_file,
              open(f'{end_directory}\home_task.csv','w',encoding='utf-8',newline='') as csv_file,
              open(f'{end_directory}\home_task.pickle','wb') as pickle_file):
            json.dump(d,json_file,ensure_ascii=False,indent=2)
            writer = csv.DictWriter(csv_file,fieldnames=[*d.keys()])
            writer.writeheader()
            writer.writerow(d)
            pickle.dump(d,pickle_file)