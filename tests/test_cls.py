"""Do not run this file. This is a test that should be run from tests.py"""
from ReprTraceback import ReprTraceback

class A:
    def a_throw(self):
        x="3 cls 4"
        B.b_throw(x)

class B:
    @classmethod
    def b_throw(cls, z):
        raise Exception()

    def __repr__(self):
        return "B Instance"

def main():
    ReprTraceback.init()

    A().a_throw()


if __name__ == '__main__':
    main()
