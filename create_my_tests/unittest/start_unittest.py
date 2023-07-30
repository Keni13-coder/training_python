import sys
sys.path.append('..')
from start_test import is_test
import unittest


class MyTest(unittest.TestCase):
    def test_is_test(self):
        self.assertEqual(is_test(42),True, msg='ты дура')
        self.assertEqual(is_test(41),False, msg='ты дура')
        self.assertTrue(is_test(48))
        self.assertFalse(is_test(39))
    
    def test_type(self):
        self.assertRaises(TypeError, is_test, 1.2)
        
        
match __name__:
    case '__main__':
        unittest.main(verbosity=2)