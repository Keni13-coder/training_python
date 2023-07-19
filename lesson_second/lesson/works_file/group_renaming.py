from pathlib import Path
import os


__all__ = ['rename_group_max']

def rename_group_max(end_name: str, count_sequence_number: int , start_expansions: str, end_expansions: str, slice_name:list[int,int], directory=Path().cwd()):
    start_number = 1
    start_slice, end_slace = slice_name
    for dirs, folders, files in os.walk(directory):
        for i,file in enumerate(files):
            if file.endswith(start_expansions):
                old_name = Path(dirs) / file
                old_name.rename(f'{dirs}\{file[start_slice:end_slace]}{end_name}{str(start_number).zfill(count_sequence_number)}.{end_expansions}')
                start_number += 1