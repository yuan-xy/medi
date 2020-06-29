.. include:: ../global.rst

Using Medi
==========

|medi| is can be used with a variety of plugins and software. It is also possible
to use |medi| in the :ref:`Python shell or with IPython <repl-completion>`.

Below you can also find a list of :ref:`recipes for type hinting <recipes>`.


.. _editor-plugins:

Editor Plugins
--------------

Vim
~~~

- medi-vim_
- YouCompleteMe_
- deoplete-medi_

Visual Studio Code
~~~~~~~~~~~~~~~~~~

- `Python Extension`_

Emacs
~~~~~

- Medi.el_
- elpy_
- anaconda-mode_

Sublime Text 2/3
~~~~~~~~~~~~~~~~

- SublimeJEDI_ (ST2 & ST3)
- anaconda_ (only ST3)

SynWrite
~~~~~~~~

- SynMedi_

TextMate
~~~~~~~~

- Textmate_ (Not sure if it's actually working)

Kate
~~~~

- Kate_ version 4.13+ `supports it natively
  <https://projects.kde.org/projects/kde/applications/kate/repository/entry/addons/kate/pate/src/plugins/python_autocomplete_medi.py?rev=KDE%2F4.13>`__,
  you have to enable it, though.

Atom
~~~~

- autocomplete-python-medi_

GNOME Builder
~~~~~~~~~~~~~

- `GNOME Builder`_ `supports it natively
  <https://git.gnome.org/browse/gnome-builder/tree/plugins/medi>`__,
  and is enabled by default.

Gedit
~~~~~

- gedi_

Eric IDE
~~~~~~~~

- `Eric IDE`_ (Available as a plugin)

Web Debugger
~~~~~~~~~~~~

- wdb_

and many more!


.. autofunction:: medi.utils.setup_readline

.. _recipes:

Recipes
-------

Here are some tips on how to use |medi| efficiently.


Sphinx style
++++++++++++

http://www.sphinx-doc.org/en/stable/domains.html#info-field-lists

::

    def myfunction(node, foo):
        """
        Do something with a ``node``.

        :type node: ProgramNode
        :param str foo: foo parameter description
        """
        node.| # complete here

Epydoc
++++++

http://epydoc.sourceforge.net/manual-fields.html

::

    def myfunction(node):
        """
        Do something with a ``node``.

        @type node: ProgramNode
        """
        node.| # complete here

Numpydoc
++++++++

https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

In order to support the numpydoc format, you need to install the `numpydoc
<https://pypi.python.org/pypi/numpydoc>`__ package.

::

    def foo(var1, var2, long_var_name='hi'):
        r"""
        A one-line summary that does not use variable names or the
        function name.

        ...

        Parameters
        ----------
        var1 : array_like
            Array_like means all those objects -- lists, nested lists,
            etc. -- that can be converted to an array. We can also
            refer to variables like `var1`.
        var2 : int
            The type above can either refer to an actual Python type
            (e.g. ``int``), or describe the type of the variable in more
            detail, e.g. ``(N,) ndarray`` or ``array_like``.
        long_variable_name : {'hi', 'ho'}, optional
            Choices in brackets, default first when optional.

        ...

        """
        var2.| # complete here

.. _medi-vim: https://github.com/davidhalter/medi-vim
.. _youcompleteme: https://valloric.github.io/YouCompleteMe/
.. _deoplete-medi: https://github.com/zchee/deoplete-medi
.. _Medi.el: https://github.com/tkf/emacs-medi
.. _elpy: https://github.com/jorgenschaefer/elpy
.. _anaconda-mode: https://github.com/proofit404/anaconda-mode
.. _sublimemedi: https://github.com/srusskih/SublimeJEDI
.. _anaconda: https://github.com/DamnWidget/anaconda
.. _SynMedi: http://uvviewsoft.com/synmedi/
.. _wdb: https://github.com/Kozea/wdb
.. _TextMate: https://github.com/lawrenceakka/python-medi.tmbundle
.. _kate: https://kate-editor.org/
.. _autocomplete-python-medi: https://atom.io/packages/autocomplete-python-medi
.. _GNOME Builder: https://wiki.gnome.org/Apps/Builder/
.. _gedi: https://github.com/isamert/gedi
.. _Eric IDE: https://eric-ide.python-projects.org
.. _Python Extension: https://marketplace.visualstudio.com/items?itemName=ms-python.python
