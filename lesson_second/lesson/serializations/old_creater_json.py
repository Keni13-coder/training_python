import json
import os


__all__ = ['task_1']

def task_1(file_name: str, end_file=os.getcwd())-> None:
    with (open(file_name,'r',encoding='utf-8') as f,
          open(f'{end_file}\Test_file\\test_js.json','w+',encoding='utf-8') as js):
        d = dict(x.replace('\n', '').capitalize().split(':')  for x in f)
        json.dump(d,js,indent=2,separators=(', ',':'))