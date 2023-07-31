import sys
import pytest
sys.path.append('..')
from files_py import student


@pytest.fixture
def data():
    data : student.Student = student.Student('Бочкин Cергей Бритьевич')
    return data

def test_raise_name():
    with pytest.raises(ValueError):
        student.Student('бочкин Cергей Бритьевич')

    
def test_param(data):
    assert data.results_dict =='Студент - Бочкин Cергей Бритьевич:\n[]\n{}'
    data('астрономия', 80, 5)
    assert data.results_dict == "Студент - Бочкин Cергей Бритьевич:\n['exam : астрономия = 80.0', 'grade : астрономия = 5.0']\n{'exam': 80.0, 'grade': 5.0}"
    data('этикет', 90, 4)
    assert data.results_dict == \
                    "Студент - Бочкин Cергей Бритьевич:\n['exam : астрономия = 80.0', 'exam : этикет = 90.0', 'grade : астрономия = 5.0', 'grade : этикет = 4.0']\n{'exam': 85.0, 'grade': 4.5}"


def test_raise_param(data):
    with pytest.raises(ValueError):
        data('физика', 50, 5)
        data('астрономия', 101, 5)
        data('астрономия', 99, 7)
        data('астрономия', 99, 7)
        data('астрономия', 20, 1)


       

match __name__:
    case '__main__':
        pytest.main(['-v'])