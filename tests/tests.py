import subprocess
import unittest


class TestReprTraceback(unittest.TestCase):
    def test_positional_args(self):
        tests = [
            ("test_positional_args.py", "positional_args(integer=5, string=abc, lst=[2, 4, 8])"),
            ("test_variable_args.py", "variable_args(args=(1, 'a', [2], {3}, {4: 5}))"),
            ("test_keyword_args.py", "keyword_args(kwargs={'a': 'b', 't': 2, 'c': [], 'd': {}})"),
            ("test_default_args.py", "default_args(a=2, b=(2, 'abc'))"),
            ("test_all_arg_types.py", "all_args(a=1, b=3, args=(1, 2, 3), kwargs={'x': 'b'})"),
            ("test_deleted_local_variable.py", "deleted_arg(integer=5, string=abc, lst=?)"),
            ("test_nested_function.py", "test(a=2)"),
            ("test_class.py", "fial"),
        ]

        for test in tests:
            file, expected = test
            self._run_and_assert_traceback(file, expected)

    def _run_and_assert_traceback(self, file: str, expected: str):
        try:
            subprocess.check_output(['python', file], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            traceback = e.output.decode()
            self.assertIn(expected, traceback, F"[[Failed at {file}]]\n\n[[EXPECTED SUB-STR]]:\n{expected}\n\n[[ACTUAL]]:\n{traceback}")
            return

        assert False, F"[[Failed at {file}]]\n\n[[EXPECTED SUB-STR]]:\n{expected}"


if __name__ == '__main__':
    unittest.main()