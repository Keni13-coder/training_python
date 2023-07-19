import pickle
import os
import csv


__all__ = ['pickle_to_csv']

def pickle_to_csv(pickle_file: str)-> None:
    with (open(pickle_file,'rb') as pic_file,
          open(f'{os.getcwd()}\\rezul.csv','w',newline='',encoding='utf-8')as rezul):
        reader = pickle.load(pic_file)
        writer = csv.DictWriter(rezul,fieldnames=[*reader.keys()])
        writer.writeheader()
        writer.writerow(reader)