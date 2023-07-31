

'''
Задание №1
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
'''

def del_full_or_lantin(text: str) -> str:
    form = text.translate({ord(x): x if x.upper() in 'QWERTYUIOPLKJHGFDSAZXCVBNM ' else None for x in text})
    return form.lower()


text = '''For almost any person, there is nothing more important in the world than their family. I love my family too. Today I would like to tell you about them.
My family is quite big. It consists of my mother, father, my three siblings and our cat Bob. Well, most people would say that a pet is not a family member but no one in our family would agree with that. We all love Bob and consider him a family member.
My mother’s name is Anna, she is a teacher. She has been working in our local school for a long time. My mom teaches History and Social Studies, the subjects that I really love. She loves reading very much, and her favorite book is “A Street Cat Named Bob” by James Bowen. If you are familiar with the book, you can guess why she named our ginger cat Bob.
My father’s name is Igor. He is a little older than mom and he used to be a police officer. He retired at a quite young age and has been running his own business ever since. He has a small coffee shop and a candy store. To be honest, I don’t know much about his business, but he says it is doing well.
As for my siblings, I have a sister, her name is Maria, and she is the oldest one, and two brothers – Viktor and Boris. By the way, I am the youngest child in the family but I am totally happy with that role. My sister Maria is an engineer, she lives in another town but visits us at least once a month. My brothers are still students. Viktor studies history, following in our mother’s footsteps, Boris is going to be a software developer. He is a big fan of videogames, and his dream is to develop his own game.
'''



# print(del_full_or_lantin(text))


'''
Задание №2
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
'''



'''
Задание №3
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
'''


'''
Задание №4
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
'''


'''
Задание №5
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
'''


'''
Задание №6
На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры.
'''