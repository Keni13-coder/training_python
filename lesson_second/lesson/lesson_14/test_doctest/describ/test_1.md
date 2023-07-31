Проверяем doctest
===

Юзаем функцию del_full_or_lantin
---

    >>> from test_lesson import del_full_or_lantin

Делаем возврат строки без изменений

    >>> text = 'almost any person'
    >>> del_full_or_lantin(text)
    'almost any person'

Возврат строки с преобразованием регистра без потери
символов 

    >>> text = 'For Almost ANy peRsOn'
    >>> del_full_or_lantin(text)
    'for almost any person'

Возврат строки с удалением знаков пунктуации

    >>> text = 'for almost any person,'
    >>> del_full_or_lantin(text)
    'for almost any person'

Возврат строки с удалением слов из букв других алфавитов

    >>> text = 'and she is the oldest one Возможно текст останется'
    >>> del_full_or_lantin(text)
    'and she is the oldest one   '

Возврат строки с удалением букв других алфавитов

    >>> text = 'and she is the olКest Иne'
    >>> del_full_or_lantin(text)
    'and she is the olest ne'

Полный смак функции 

    >>> text = 'For almost any person, there is nothiВозможноng more important in the world than their family. I love my family too. TПриветday I would like to tell you abЯтутout them. Ты мог что-то замететь.'
    >>> del_full_or_lantin(text)
    'for almost any person there is nothing more important in the world than their family i love my family too tday i would like to tell you about them    '