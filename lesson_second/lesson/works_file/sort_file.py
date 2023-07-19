from pathlib import Path
import os
from works_file import max_files_generators as mfg


__all__ = ['sorted_file'] 

def sorted_file(directory: str)-> None:

    extensions = {
    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 
              'h264', 'flv', 'rm', 'swf', 'vob'],

    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 
             'tar', 'xml'],

    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl',
              'cda'],

    'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 
              'tiff'],
    'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],
    
    'exe': ['exe'],
    }
    if not Path(directory).is_dir():
        directory = Path().cwd() / directory
        Path(directory).mkdir(parents=True)
        mfg.max_gener_file(['txt','mp4', 'mov', 'avi','sqlite', 'sqlite3', 'csv', 'dat','mp3', 'wav', 'ogg','pdf', 'txt', 'doc', 'docx'],15,directory)

    rezul  = [file.split('.') for dirs, folders, files in os.walk(directory) for file in files]

    for (name, expan) in rezul:
        for k, v in extensions.items():
            if expan in v:
                new_dir = Path().cwd() / directory / k 
                if new_dir.is_dir():
                    old_dir = Path(directory) / f'{name}.{expan}'
                    old_dir = old_dir.replace(new_dir / f'{name}.{expan}')
                else:
                    Path(new_dir).mkdir(parents=True)
                    old_dir = Path(directory) / f'{name}.{expan}'
                    old_dir = old_dir.replace(new_dir / f'{name}.{expan}')
                    
                    
if __name__ == '__main__':                   
    sorted_file('Test_folder_file')                    