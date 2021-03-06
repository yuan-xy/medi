.. include:: ../global.rst

API Overview
============

.. note:: This documentation is mostly for Plugin developers, who want to
   improve their editors/IDE with Medi.

.. _api:

The API consists of a few different parts:

- The main starting points for complete/goto: :class:`.Script`.
- :ref:`API Result Classes <api-classes>`
- :ref:`Python Versions/Virtualenv Support <environments>` with functions like
  :func:`.find_system_environments` and :func:`.find_virtualenvs`
- A way to work with different :ref:`Folders / Projects <projects>`
- Helpful functions: :func:`.preload_module` and :func:`.set_debug_function`

The methods that you are most likely going to use to work with Medi are the
following ones:

.. currentmodule:: medi

.. autosummary::
   :nosignatures:

    Script.complete
    Script.goto
    Script.infer
    Script.help
    Script.get_signatures
    Script.get_references
    Script.get_context
    Script.get_names
    Script.get_syntax_errors
    Script.rename
    Script.inline
    Script.extract_variable
    Script.extract_function
    Script.search
    Script.complete_search
    Project.search
    Project.complete_search

Script
------

.. autoclass:: medi.Script
    :members:


.. _projects:

Projects
--------

.. automodule:: medi.api.project

.. autofunction:: medi.get_default_project
.. autoclass:: medi.Project
    :members:

.. _environments:

Environments
------------

.. automodule:: medi.api.environment

.. autofunction:: medi.find_system_environments
.. autofunction:: medi.find_virtualenvs
.. autofunction:: medi.get_system_environment
.. autofunction:: medi.create_environment
.. autofunction:: medi.get_default_environment
.. autoexception:: medi.InvalidPythonEnvironment
.. autoclass:: medi.api.environment.Environment
    :members:

Helper Functions
----------------

.. autofunction:: medi.preload_module
.. autofunction:: medi.set_debug_function

Errors
------

.. autoexception:: medi.InternalError
.. autoexception:: medi.RefactoringError

Examples
--------

Completions
~~~~~~~~~~~

.. sourcecode:: python

   >>> import medi
   >>> code = '''import json; json.l'''
   >>> script = medi.Script(code, path='example.py')
   >>> script
   <Script: 'example.py' <SameEnvironment: 3.5.2 in /usr>>
   >>> completions = script.complete(1, 19)
   >>> completions
   [<Completion: load>, <Completion: loads>]
   >>> completions[1]
   <Completion: loads>
   >>> completions[1].complete
   'oads'
   >>> completions[1].name
   'loads'

Type Inference / Goto
~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: python

    >>> import medi
    >>> code = '''\
    ... def my_func():
    ...     print 'called'
    ... 
    ... alias = my_func
    ... my_list = [1, None, alias]
    ... inception = my_list[2]
    ... 
    ... inception()'''
    >>> script = medi.Script(code)
    >>>
    >>> script.goto(8, 1)
    [<Name full_name='__main__.inception', description='inception = my_list[2]'>]
    >>>
    >>> script.infer(8, 1)
    [<Name full_name='__main__.my_func', description='def my_func'>]

References
~~~~~~~~~~

.. sourcecode:: python

    >>> import medi
    >>> code = '''\
    ... x = 3
    ... if 1 == 2:
    ...     x = 4
    ... else:
    ...     del x'''
    >>> script = medi.Script(code)
    >>> rns = script.get_references(5, 8)
    >>> rns
    [<Name full_name='__main__.x', description='x = 3'>,
     <Name full_name='__main__.x', description='x = 4'>,
     <Name full_name='__main__.x', description='del x'>]
    >>> rns[1].line
    3
    >>> rns[1].column
    4

Deprecations
------------

The deprecation process is as follows:

1. A deprecation is announced in the next major/minor release.
2. We wait either at least a year and at least two minor releases until we
   remove the deprecated functionality.
