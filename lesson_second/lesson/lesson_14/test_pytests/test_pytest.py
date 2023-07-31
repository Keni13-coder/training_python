import pytest
import sys
sys.path.append('..')
from test_lesson import del_full_or_lantin


def test_unchanged():
    text = 'almost any person'
    assert del_full_or_lantin(text) == 'almost any person'
        
        
def test_register_conversion():
    text = 'For Almost ANy peRsOn'
    assert del_full_or_lantin(text) == 'for almost any person'

    
def test_removing_signs():
    text = 'for almost any person,'
    assert del_full_or_lantin(text) == 'for almost any person'
    
    
def test_deleting_letters():
    text = 'and she is the olКest Иne'
    assert del_full_or_lantin(text) == 'and she is the olest ne'
        
    
def test_deleting_words():
    text = 'and she is the oldest one Возможно текст останется'
    assert del_full_or_lantin(text) == 'and she is the oldest one   '
    
    
def test_full_functionality():
    text = 'For almost any person, there is nothiВозможноng more important in the world than their family.\
        I love my family too. TПриветday I would like to tell you abЯтутout them. Ты мог что-то замететь.'
            
    assert del_full_or_lantin(text) == 'for almost any person there is nothing more important in the world than their family\
        i love my family too tday i would like to tell you about them    '
        
        
match __name__:
    case '__main__':
        pytest.main(['-v'])