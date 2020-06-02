import medi
from medi import debug

def test_simple():
    medi.set_debug_function()
    debug.speed('foo')
    debug.dbg('bar')
    debug.warning('baz')
    medi.set_debug_function(None, False, False, False)
