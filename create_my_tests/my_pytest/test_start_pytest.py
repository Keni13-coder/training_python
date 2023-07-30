import pytest
import sys
sys.path.append('..')
from start_test import is_test

@pytest.fixture
def data():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_is_test():
    assert is_test(40), 'Даное число являеться не четным'
    assert not is_test(41), 'Даное число являеться четным'


def test_type():
    with pytest.raises(TypeError):
        is_test(1.2)


match __name__:
    case '__main__':
        pytest.main(['-v'])
