import sys
import unittest
sys.path.append('..')
from files_py import student


class TestStudent(unittest.TestCase):
    
    def setUp(self) -> None:
        self.data = student.Student('Бочкин Cергей Бритьевич')
        
    
    def test_raise_name(self):
        self.assertRaises(ValueError, student.Student,'бочкин Cергей Бритьевич' )

    
    def test_param(self):
        self.assertEqual(self.data.results_dict, 'Студент - Бочкин Cергей Бритьевич:\n[]\n{}')
        self.data('астрономия', 80, 5)
        self.assertEqual(self.data.results_dict, "Студент - Бочкин Cергей Бритьевич:\n['exam : астрономия = 80.0', 'grade : астрономия = 5.0']\n{'exam': 80.0, 'grade': 5.0}")
        self.data('этикет', 90, 4)
        self.assertEqual(self.data.results_dict,
                         "Студент - Бочкин Cергей Бритьевич:\n['exam : астрономия = 80.0', 'exam : этикет = 90.0', 'grade : астрономия = 5.0', 'grade : этикет = 4.0']\n{'exam': 85.0, 'grade': 4.5}")


    def test_raise_param(self):
        self.assertRaises(ValueError, self.data, 'физика', 50, 5)
        self.assertRaises(ValueError, self.data, 'астрономия', 101, 5)
        self.assertRaises(ValueError, self.data, 'астрономия', 99, 7)
        self.assertRaises(ValueError, self.data, 'астрономия', 99, 7)
        self.assertRaises(ValueError, self.data, 'астрономия', 20, 1)










match __name__:
    case '__main__':
        unittest.main(verbosity=2)