import json
import csv
import os


__all__ = ['json_to_csv']

def json_to_csv(end_file=os.getcwd())-> None:
    try:
        with open(f'{end_file}\Test_file\\test.json','r',encoding='utf-8') as f:
            reader_ : dict= json.load(f)
            print(reader_)
            with open(f'{end_file}Test_file\\testing.csv','w',encoding='utf-8',newline='') as rez:
                writer = csv.DictWriter(rez,fieldnames=[*reader_.keys()])
                writer.writeheader()
                writer.writerow(reader_)
    except FileNotFoundError:
        return 'Файл не найден'