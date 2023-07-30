def is_test(number: int):
    if not isinstance(number,int):
        raise TypeError(f'Значение {number} должно быть int а не {type(number)}')
    if number % 2 == 0:
        return True
    return False


match __name__:
    case '__main__':
        import doctest
        doctest.testmod(verbose=True)
        is_test(3.14)