#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        ret = fct(*args)
    except BaseException as exc:
        ret = None
        print("Exception: {}".format(exc), file=sys.stderr)
    return ret
