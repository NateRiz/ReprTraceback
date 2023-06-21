"""Do not run this file. This is a test that should be run from tests.py"""
from ReprTraceback import ReprTraceback

def default_args(a=1, b=(2,"abc")):
    raise Exception()
def main():
    ReprTraceback.init()

    a=2

    default_args(a)

if __name__ == '__main__':
    main()
