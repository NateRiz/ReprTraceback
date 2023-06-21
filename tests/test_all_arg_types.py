"""Do not run this file. This is a test that should be run from tests.py"""
from ReprTraceback import ReprTraceback

def all_args(a, b=2, *args, **kwargs):
    raise Exception()
def main():
    ReprTraceback.init()

    a=1
    b=3
    args= (1,2,3)
    kwargs = {"x":"b"}

    all_args(a, b, *args, **kwargs)

if __name__ == '__main__':
    main()
