"""Do not run this file. This is a test that should be run from tests.py"""
from ReprTraceback import ReprTraceback

def keyword_args(**kwargs):
    raise Exception()
def main():
    ReprTraceback.init()

    kwargs = {"a":"b","t":2, "c":[],"d":{}}

    keyword_args(**kwargs)

if __name__ == '__main__':
    main()
