import sys
import unittest
sys.path.append('..')
from test_lesson import del_full_or_lantin


class TestTask1(unittest.TestCase):
    
    
    def test_unchanged(self):
        text = 'almost any person'
        self.assertEqual(del_full_or_lantin(text), 'almost any person')
        
        
    def test_register_conversion(self):
        text = 'For Almost ANy peRsOn'
        self.assertEqual(del_full_or_lantin(text), 'for almost any person')
    
    
    def test_removing_signs(self):
        text = 'for almost any person,'
        self.assertEqual(del_full_or_lantin(text), 'for almost any person')
    
    
    def test_deleting_letters(self):
        text = 'and she is the olКest Иne'
        self.assertEqual(del_full_or_lantin(text), 'and she is the olest ne')
        
    
    def test_deleting_words(self):
        text = 'and she is the oldest one Возможно текст останется'
        self.assertEqual(del_full_or_lantin(text), 'and she is the oldest one   ')
    
    
    def test_full_functionality(self):
        text = 'For almost any person, there is nothiВозможноng more important in the world than their family.\
            I love my family too. TПриветday I would like to tell you abЯтутout them. Ты мог что-то замететь.'
            
        self.assertEqual(del_full_or_lantin(text), 'for almost any person there is nothing more important in the world than their family\
            i love my family too tday i would like to tell you about them    ')



match __name__:
    case '__main__':
        unittest.main(verbosity=2)