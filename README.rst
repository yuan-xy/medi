####################################################################################
Medi - an awesome autocompletion, static analysis and refactoring library for Python
####################################################################################

.. image:: http://isitmaintained.com/badge/open/davidhalter/medi.svg
    :target: https://github.com/davidhalter/medi/issues
    :alt: The percentage of open issues and pull requests

.. image:: http://isitmaintained.com/badge/resolution/davidhalter/medi.svg
    :target: https://github.com/davidhalter/medi/issues
    :alt: The resolution time is the median time an issue or pull request stays open.

.. image:: https://travis-ci.org/davidhalter/medi.svg?branch=master
    :target: https://travis-ci.org/davidhalter/medi
    :alt: Linux Tests

.. image:: https://ci.appveyor.com/api/projects/status/mgva3bbawyma1new/branch/master?svg=true
    :target: https://ci.appveyor.com/project/davidhalter/medi/branch/master
    :alt: Windows Tests

.. image:: https://coveralls.io/repos/davidhalter/medi/badge.svg?branch=master
    :target: https://coveralls.io/r/davidhalter/medi
    :alt: Coverage status


Medi is a static analysis tool for Python that is typically used in
IDEs/editors plugins. Medi has a focus on autocompletion and goto
functionality. Other features include refactoring, code search and finding
references.

Medi has a simple API to work with. There is a reference implementation as a
`VIM-Plugin <https://github.com/davidhalter/medi-vim>`_. Autocompletion in your
REPL is also possible, IPython uses it natively and for the CPython REPL you
can install it. Medi is well tested and bugs should be rare.

Medi can currently be used with the following editors/projects:

- Vim (medi-vim_, YouCompleteMe_, deoplete-medi_, completor.vim_)
- `Visual Studio Code`_ (via `Python Extension <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_)
- Emacs (Medi.el_, company-mode_, elpy_, anaconda-mode_, ycmd_)
- Sublime Text (SublimeJEDI_ [ST2 + ST3], anaconda_ [only ST3])
- TextMate_ (Not sure if it's actually working)
- Kate_ version 4.13+ supports it natively, you have to enable it, though.  [`see
  <https://projects.kde.org/projects/kde/applications/kate/repository/show?rev=KDE%2F4.13>`_]
- Atom_ (autocomplete-python-medi_)
- `GNOME Builder`_ (with support for GObject Introspection)
- Gedit (gedi_)
- wdb_ - Web Debugger
- `Eric IDE`_ (Available as a plugin)
- `IPython 6.0.0+ <https://ipython.readthedocs.io/en/stable/whatsnew/version6.html>`_

and many more!

Here are some pictures taken from medi-vim_:

.. image:: https://github.com/davidhalter/medi/raw/master/docs/_screenshots/screenshot_complete.png

Completion for almost anything:

.. image:: https://github.com/davidhalter/medi/raw/master/docs/_screenshots/screenshot_function.png

Documentation:

.. image:: https://github.com/davidhalter/medi/raw/master/docs/_screenshots/screenshot_pydoc.png


Get the latest version from `github <https://github.com/davidhalter/medi>`_
(master branch should always be kind of stable/working).

Docs are available at `https://medi.readthedocs.org/en/latest/
<https://medi.readthedocs.org/en/latest/>`_. Pull requests with enhancements
and/or fixes are awesome and most welcome. Medi uses `semantic versioning
<https://semver.org/>`_.

If you want to stay up-to-date (News / RFCs), please subscribe to this `github
thread <https://github.com/davidhalter/medi/issues/1063>`_.:

Issues & Questions
==================

You can file issues and questions in the `issue tracker
<https://github.com/davidhalter/medi/>`. Alternatively you can also ask on
`Stack Overflow <https://stackoverflow.com/questions/tagged/python-medi>`_ with
the label ``python-medi``.

Installation
============

`Check out the docs <https://medi.readthedocs.org/en/latest/docs/installation.html>`_.

Features and Limitations
========================

Medi's features are listed here:
`Features <https://medi.readthedocs.org/en/latest/docs/features.html>`_.

You can run Medi on CPython 2.7 or 3.5+ but it should also
understand code that is older than those versions. Additionally you should be
able to use `Virtualenvs <https://medi.readthedocs.org/en/latest/docs/api.html#environments>`_
very well.

Tips on how to use Medi efficiently can be found `here
<https://medi.readthedocs.org/en/latest/docs/features.html#recipes>`_.

API
---

You can find a comprehensive documentation for the
`API here <https://medi.readthedocs.org/en/latest/docs/api.html>`_.

Autocompletion / Goto / Documentation
-------------------------------------

There are the following commands:

- ``medi.Script.goto``
- ``medi.Script.infer``
- ``medi.Script.help``
- ``medi.Script.complete``
- ``medi.Script.get_references``
- ``medi.Script.get_signatures``
- ``medi.Script.get_context``

The returned objects are very powerful and are really all you might need.

Autocompletion in your REPL (IPython, etc.)
-------------------------------------------

Medi is a dependency of IPython. Autocompletion in IPython with Medi is
therefore possible without additional configuration.

Here is an `example video <https://vimeo.com/122332037>`_ how REPL completion
can look like.
For the ``python`` shell you can enable tab completion in a `REPL
<https://medi.readthedocs.org/en/latest/docs/usage.html#tab-completion-in-the-python-shell>`_.

Static Analysis
---------------

For a lot of forms of static analysis, you can try to use
``medi.Script(...).get_names``. It will return a list of names that you can
then filter and work with. There is also a way to list the syntax errors in a
file: ``medi.Script.get_syntax_errors``.


Refactoring
-----------

Medi supports the following refactorings:

- ``medi.Script.inline``
- ``medi.Script.rename``
- ``medi.Script.extract_function``
- ``medi.Script.extract_variable``

Code Search
-----------

There is support for module search with ``medi.Script.search``, and project
search for ``medi.Project.search``. The way to search is either by providing a
name like ``foo`` or by using dotted syntax like ``foo.bar``. Additionally you
can provide the API type like ``class foo.bar.Bar``. There are also the
functions ``medi.Script.complete_search`` and ``medi.Project.complete_search``.

Development
===========

There's a pretty good and extensive `development documentation
<https://medi.readthedocs.org/en/latest/docs/development.html>`_.

Testing
=======

The test suite uses ``pytest``::

    pip install pytest

If you want to test only a specific Python version (e.g. Python 3.8), it is as
easy as::

    python3.8 -m pytest

For more detailed information visit the `testing documentation
<https://medi.readthedocs.org/en/latest/docs/testing.html>`_.

Acknowledgements
================

Thanks a lot to all the
`contributors <https://medi.readthedocs.org/en/latest/docs/acknowledgements.html>`_!


.. _medi-vim: https://github.com/davidhalter/medi-vim
.. _youcompleteme: https://github.com/ycm-core/YouCompleteMe
.. _deoplete-medi: https://github.com/zchee/deoplete-medi
.. _completor.vim: https://github.com/maralla/completor.vim
.. _Medi.el: https://github.com/tkf/emacs-medi
.. _company-mode: https://github.com/syohex/emacs-company-medi
.. _elpy: https://github.com/jorgenschaefer/elpy
.. _anaconda-mode: https://github.com/proofit404/anaconda-mode
.. _ycmd: https://github.com/abingham/emacs-ycmd
.. _sublimemedi: https://github.com/srusskih/SublimeJEDI
.. _anaconda: https://github.com/DamnWidget/anaconda
.. _wdb: https://github.com/Kozea/wdb
.. _TextMate: https://github.com/lawrenceakka/python-medi.tmbundle
.. _Kate: https://kate-editor.org
.. _Atom: https://atom.io/
.. _autocomplete-python-medi: https://atom.io/packages/autocomplete-python-medi
.. _GNOME Builder: https://wiki.gnome.org/Apps/Builder
.. _Visual Studio Code: https://code.visualstudio.com/
.. _gedi: https://github.com/isamert/gedi
.. _Eric IDE: https://eric-ide.python-projects.org
