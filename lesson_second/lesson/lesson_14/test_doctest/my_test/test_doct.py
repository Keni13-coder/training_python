import sys
import doctest
sys.path.append('../..')
from test_lesson import del_full_or_lantin

match __name__:
    case '__main__':
        doctest.testfile('../describ/test_1.md',verbose=True)