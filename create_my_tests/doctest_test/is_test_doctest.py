import doctest
import os
import sys
# sys.path.append(os.path.join(os.getcwd(), '..'))
sys.path.append('..')
from start_test import is_test


match __name__:
    case '__main__':
        doctest.testfile('test/is_test_test.md',verbose=True)