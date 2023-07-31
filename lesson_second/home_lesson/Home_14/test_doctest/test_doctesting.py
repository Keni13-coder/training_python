import doctest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
import files_py.student as st



match __name__:
    case '__main__':
        doctest.testfile('describ/class_student.md',verbose=True)