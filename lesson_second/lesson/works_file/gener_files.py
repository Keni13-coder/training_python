import os
import random as rd
from works_file import gener_name 


__all__ = ['gener_file']

def gener_file(expansion='txt', min_name=6, max_name=30, min_byte=256, max_byte=4096, count_file=42)->None:
    byte = rd.randint(min_byte,max_byte)
    for _ in range(count_file):
        name = gener_name.generator_names(0,min_name,max_name)
        with open(f'{name}.{expansion}','xb') as f:
            f.write(os.urandom(byte))