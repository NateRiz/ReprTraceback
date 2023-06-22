"""Do not run this file. This is a test that should be run from tests.py"""
from ReprTraceback import ReprTraceback

class A:
    def a_throw(self):
        x="2 test static 3"
        B.b_throw(x)

class B:
    def __init__(self):
        pass

    @staticmethod
    def b_throw(z):
        raise Exception()

    def __repr__(self):
        return "B Instance"

def main():
    ReprTraceback.init()

    A().a_throw()


if __name__ == '__main__':
    main()
