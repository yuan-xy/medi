"""
To use Medi completion in Python interpreter, add the following in your shell
setup (e.g., ``.bashrc``). This works only on Linux/Mac, because readline is
not available on Windows. If you still want Medi autocompletion in your REPL,
just use IPython instead::

    export PYTHONSTARTUP="$(python -m medi repl)"

Then you will be able to use Medi completer in your Python interpreter::

    $ python
    Python 2.7.2+ (default, Jul 20 2012, 22:15:08)
    [GCC 4.6.1] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import os
    >>> os.path.join('a', 'b').split().in<TAB>            # doctest: +SKIP
    ..dex   ..sert

"""
import medi.utils
from medi import __version__ as __medi_version__

print('REPL completion using Medi %s' % __medi_version__)
medi.utils.setup_readline(fuzzy=False)

del medi

# Note: try not to do many things here, as it will contaminate global
# namespace of the interpreter.
