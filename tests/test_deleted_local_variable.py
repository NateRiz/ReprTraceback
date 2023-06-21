"""Do not run this file. This is a test that should be run from tests.py"""
from ReprTraceback import ReprTraceback

def deleted_arg(integer, string, lst):
    del lst
    raise Exception()
def main():
    ReprTraceback.init()

    integer = 5
    string = "abc"
    lst_ = [2, 4, 8]

    deleted_arg(integer, string, lst_)

if __name__ == '__main__':
    main()
