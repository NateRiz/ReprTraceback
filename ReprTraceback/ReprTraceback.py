import collections
import itertools
import linecache
import sys
import traceback as tb
import inspect


def repr_exception_handler(type_, value, exc_tb):
    tb_gen = tb._walk_tb_with_full_positions(exc_tb)
    traceback = ReprTraceback.extract_from_extended_frame_gen(tb_gen)

    for item in ReprTraceback.from_list(traceback).format():
        print(item, file=sys.stderr, end="")
    print(F"{type_.__name__}: {value}", file=sys.stderr)
class ReprFrameSummary(tb.FrameSummary):
    def __init__(self, f_back, f_code, filename, lineno, name, lookup_line=True, locals=None,
                 line=None, end_lineno=None, colno=None, end_colno=None):
        super().__init__(filename, lineno, name, lookup_line=lookup_line, locals=locals, line=line,
                         end_lineno=end_lineno, colno=colno, end_colno=end_colno)
        self.f_back = f_back
        self.f_code = f_code


class ReprTraceback(tb.StackSummary):
    @classmethod
    def extract_from_extended_frame_gen(klass, frame_gen, *, limit=None,
                                        lookup_lines=True):
        if limit is None:
            limit = getattr(sys, 'tracebacklimit', None)
            if limit is not None and limit < 0:
                limit = 0
        if limit is not None:
            if limit >= 0:
                frame_gen = itertools.islice(frame_gen, limit)
            else:
                frame_gen = collections.deque(frame_gen, maxlen=-limit)

        result = klass()
        fnames = set()
        for f, (lineno, end_lineno, colno, end_colno) in frame_gen:
            co = f.f_code
            filename = co.co_filename
            name = co.co_name

            fnames.add(filename)
            linecache.lazycache(filename, f.f_globals)
            # Must defer line lookups until we have called checkcache.
            f_locals = f.f_locals
            f_back = f.f_back
            f_code = f.f_code
            result.append(
                ReprFrameSummary(f_back, f_code, filename, lineno, name, lookup_line=False,
                                 locals=f_locals, end_lineno=end_lineno, colno=colno, end_colno=end_colno))
        for filename in fnames:
            linecache.checkcache(filename)
        # If immediate lookup was desired, trigger lookups now.
        if lookup_lines:
            for f in result:
                formatted_line = ReprTraceback.get_formatted_function_exception(f)
                if formatted_line:
                    f._line = formatted_line
                f.line
                f.locals = {}
        return result

    @staticmethod
    def get_formatted_function_exception(current_frame: ReprFrameSummary):
        if current_frame.f_back is None:
            return ""
        args, varargs, kwargs = inspect.getargs(current_frame.f_code)
        argument_names = list(args)
        if varargs:
            argument_names.append(varargs)
        if kwargs:
            argument_names.append(kwargs)

        arg_pairs = []
        for name in argument_names:
            value = current_frame.locals.get(name, "?")
            arg_pairs.append((name, value))

        return F"{current_frame.f_code.co_name}(" + ", ".join(
            [F"{arg_name}={arg_value}" for arg_name, arg_value in arg_pairs]) + ")"


def init():
    sys.excepthook = repr_exception_handler
