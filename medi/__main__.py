import sys
from os.path import join, dirname, abspath, isdir

def _complete():
    import medi
    import pdb

    if '-d' in sys.argv:
        sys.argv.remove('-d')
        medi.set_debug_function()

    try:
        completions = medi.Script(sys.argv[2]).complete()
        for c in completions:
            c.docstring()
            c.type
    except Exception as e:
        print(repr(e))
        pdb.post_mortem()
    else:
        print(completions)


if len(sys.argv) > 1 and sys.argv[1] == '_complete':
    _complete()
else:
    print('Command not implemented: %s' % sys.argv[1])
