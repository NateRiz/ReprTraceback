"""Do not run this file. This is a test that should be run from tests.py"""
from ReprTraceback import ReprTraceback


def main():
    def test(a):
        raise Exception()
    ReprTraceback.init()

    b=2

    test(b)

if __name__ == '__main__':
    main()
