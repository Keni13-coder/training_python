import csv
import pickle


__all__ = ['pickle_string']

def pickle_string(csv_file: str)->str:
    with open(csv_file,'r',encoding='utf-8',newline='') as file:
        reader = [*csv.reader(file)]
        dict_reader = {head: row for (head,row) in zip(reader[0],reader[1])}
        rezul = pickle.dumps(dict_reader)
        return rezul
    