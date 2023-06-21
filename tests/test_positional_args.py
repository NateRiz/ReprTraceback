"""Do not run this file. This is a test that should be run from tests.py"""
from ReprTraceback import ReprTraceback

def positional_args(integer, string, lst):
    raise Exception()
def main():
    ReprTraceback.init()

    integer = 5
    string = "abc"
    lst = [2, 4, 8]

    positional_args(integer, string, lst)

if __name__ == '__main__':
    main()
