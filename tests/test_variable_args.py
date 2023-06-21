"""Do not run this file. This is a test that should be run from tests.py"""
from ReprTraceback import ReprTraceback

def variable_args(*args):
    raise Exception()
def main():
    ReprTraceback.init()

    args = (1, "a", [2], {3,}, {4:5})

    variable_args(*args)

if __name__ == '__main__':
    main()
