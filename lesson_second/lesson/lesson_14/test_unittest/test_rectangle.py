import sys
import unittest
sys.path.append('../..')
from lesson_13.home_task_13.rectangle import Rectangle
from lesson_13.errors.my_errors import LessThanZero


class TestRectangle(unittest.TestCase):
    
    def setUp(self) -> None:
        self.data = Rectangle(4)
    
    
    def test_arguments(self):

        self.assertEqual(self.data.width, 4)


    def test_perimeter_rectangle(self):
        self.data.width = 5
        self.assertEqual(self.data.perimeter_rectangle(), 18)
        

    def test_area_rectangle(self):
        self.data.width = 13
        self.assertEqual(self.data.area_rectangle(), 52)
        
    
    def test_equality(self):
        r = Rectangle(4)
        self.assertTrue((self.data == r))
        
    
    def test_not_equality(self):
        r = Rectangle(4,6)
        self.assertFalse((self.data == r))
        
        
    def test_raise(self):
        self.assertRaises(LessThanZero, Rectangle, -1)
        
        
match __name__:
    case '__main__':
        unittest.main(verbosity=2)