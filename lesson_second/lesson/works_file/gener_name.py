import random as rd


__all__ = ['generator_names']

def generator_names(file_name=0, min_number_name=6, max_number_name=7)-> None|str:
    VOWELS = 'AEIOU'.lower()
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    if file_name:
        with open(f'{file_name}','a',encoding='utf-8') as file:
            new_name_file = f'{rd.choice(VOWELS)}'
            for _ in range(1,rd.randint(min_number_name,max_number_name)):
                new_name_file += rd.choice(ALPHABET)
            file.write(f'{new_name_file.capitalize()}\n')
    else:
        new_name_file = f'{rd.choice(VOWELS)}'
        for _ in range(1,rd.randint(min_number_name,max_number_name)):
            new_name_file += rd.choice(ALPHABET)
        return new_name_file 
    
    
    
if __name__ == '__main__':
   generator_names('TESTING_name')    