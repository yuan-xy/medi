"""
Medi is a static analysis tool for Python that is typically used in
IDEs/editors plugins. Medi has a focus on autocompletion and goto
functionality. Other features include refactoring, code search and finding
references.

Medi has a simple API to work with. There is a reference implementation as a
`VIM-Plugin <https://github.com/davidhalter/medi-vim>`_. 

Here's a simple example of the autocompletion feature:

>>> import medi
>>> source = '''
... import json
... json.lo'''
>>> script = medi.Script(source, path='example.py')
>>> script
<Script: 'example.py' ...>
>>> completions = script.complete(3, len('json.lo'))
>>> completions
[<Completion: load>, <Completion: loads>]
>>> print(completions[0].complete)
ad
>>> print(completions[0].name)
load
"""

__version__ = '0.17.1'

from medi.api import Script, set_debug_function, preload_module, names
from medi import settings
from medi.api.environment import find_virtualenvs, find_system_environments, \
    get_default_environment, InvalidPythonEnvironment, create_environment, \
    get_system_environment, InterpreterEnvironment
from medi.api.project import Project, get_default_project
from medi.api.exceptions import InternalError, RefactoringError

# Finally load the internal plugins. This is only internal.
from medi.plugins import registry
del registry
