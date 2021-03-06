"""
Speed tests of Medi. To prove that certain things don't take longer than they
should.
"""

import time
import functools

from .helpers import get_example_dir
import medi


def _check_speed(time_per_run, number=4, run_warm=True):
    """ Speed checks should typically be very tolerant. Some machines are
    faster than others, but the tests should still pass. These tests are
    here to assure that certain effects that kill medi performance are not
    reintroduced to Medi."""
    def decorated(func):
        @functools.wraps(func)
        def wrapper(Script, **kwargs):
            if run_warm:
                func(Script=Script, **kwargs)
            first = time.time()
            for i in range(number):
                func(Script=Script, **kwargs)
            single_time = (time.time() - first) / number
            message = 'speed issue %s, %s' % (func, single_time)
            assert single_time < time_per_run, message
        return wrapper
    return decorated


@_check_speed(0.15)
def test_scipy_speed(Script):
    s = 'import scipy.weave; scipy.weave.inline('
    script = Script(s, path='')
    script.get_signatures(1, len(s))


@_check_speed(0.8)
def test_precedence_slowdown(Script):
    """
    Precedence calculation can slow down things significantly in edge
    cases. Having strange recursion structures increases the problem.
    """
    path = get_example_dir('speed', 'precedence.py')
    with open(path) as f:
        line = len(f.read().splitlines())
    assert Script(path=path).infer(line=line)
