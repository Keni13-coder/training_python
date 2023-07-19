import os
import random as rd
from pathlib import Path
from works_file import gener_files


__all__ = ['max_gener_file']

def max_gener_file(expansions: list[str], count_file: int, directory=Path().cwd()):
    end_file_name = [rd.choice(expansions) for _ in range(count_file)]
    if Path(directory).is_dir():
        os.chdir(directory)
    else:
        directory = Path().cwd()/directory
        Path(directory).mkdir(parents=True)
        os.chdir(directory)
        print(directory)   
    for x in end_file_name:
        try:
            gener_files.gener_file(x,count_file=1)
        except FileExistsError:
            print(f'Данное имя уже зарезервировано')