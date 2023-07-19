import json
import pickle
import os


__all__ = ['js_to_pickle']

def js_to_pickle(folder_name: str)-> None:
    for dirs, folders, files in os.walk(folder_name):
        for file in files:
            if file.endswith('json'):
                with (open(f'{dirs}/{file}','r',encoding='utf-8') as f,
                      open(f'{dirs}/{file.rstrip(".json")}.pickle','wb') as rezul):
                    new_file = json.load(f)
                    pickle.dump(new_file,rezul)