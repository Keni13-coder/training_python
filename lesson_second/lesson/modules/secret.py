__all__ = ['guess_secret','dictionary_secret','rezul_dict']

__dict_rezul = {}


def guess_secret(secr: str, answer: list[str], number=5) -> int:
    print(f'Загадка такова: {secr}')
    guess = input('Введите ответ на загадку: ')
    my_guess_list = []
    while number-1:
        if guess.casefold() in map(lambda x: x.casefold(),my_guess_list):
            print('Ты забыл, такой ответ уже был')
        if guess.casefold() in map(lambda x: x.casefold(),answer):
            return number
        number -= 1
        print(f'осталось: {number} попыток')
        guess = input('Введите ответ на загадку: ')
    else:
        return 0 


def dictionary_secret():
    full_dict = {
        'что-то синее': ['море',"небо"],
        "что то летающие": ["птица","дракон"],
        "что то ездит" : ['машина',"велик"]
    }
    for k,v in full_dict.items():
        __dict_rezul[k] = guess_secret(k,v)


def rezul_dict():
    
    return [f"Загадка {i} была решена за {v} попыток\n" for i,v in __dict_rezul.items()]
  
if __name__ == '__main__':  
    # print(guess_secret('Что то синего цвета',['море'," небо"],5))
    dictionary_secret()
    print(__dict_rezul)