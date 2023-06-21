"""Do not run this file. This is a test that should be run from tests.py"""
from ReprTraceback import ReprTraceback

class A:
    def __init__(self):
        self.b = B()

    def a_throw(self):
        x="1 test 2 class 3"
        self.b.b_throw(x)

class B:
    def __init__(self):
        pass

    def b_throw(self, z):
        raise Exception()

def main():
    ReprTraceback.init()

    a=A()

    a.a_throw()


if __name__ == '__main__':
    main()
