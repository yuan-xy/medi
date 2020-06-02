.. include:: ../global.rst

Medi Development
================

.. currentmodule:: medi

.. note:: This documentation is for Medi developers who want to improve Medi
    itself, but have no idea how Medi works. If you want to use Medi for 
    your IDE, look at the `plugin api <api.html>`_.
    It is also important to note that it's a pretty old version and some things
    might not apply anymore.


Introduction
------------

This page tries to address the fundamental demand for documentation of the
|medi| internals. Understanding a dynamic language is a complex task. Especially
because type inference in Python can be a very recursive task. Therefore |medi|
couldn't get rid of complexity. I know that **simple is better than complex**,
but unfortunately it sometimes requires complex solutions to understand complex
systems.

In six chapters I'm trying to describe the internals of |medi|:

- :ref:`The Medi Core <core>`
- :ref:`Core Extensions <core-extensions>`
- :ref:`Imports & Modules <imports-modules>`
- :ref:`Stubs & Annotations <stubs>`
- :ref:`Caching & Recursions <caching-recursions>`
- :ref:`Helper modules <dev-helpers>`

.. note:: Testing is not documented here, you'll find that
   `right here <testing.html>`_.


.. _core:

The Medi Core
-------------

The core of Medi consists of three parts:

- :ref:`Parser <parser>`
- :ref:`Python type inference <inference>`
- :ref:`API <dev-api>`

Most people are probably interested in :ref:`type inference <inference>`,
because that's where all the magic happens. I need to introduce the :ref:`parser
<parser>` first, because :mod:`medi.inference` uses it extensively.

.. _parser:

Parser
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Medi used to have its internal parser, however this is now a separate project
and is called `marso <http://marso.readthedocs.io>`_.

The parser creates a syntax tree that |medi| analyses and tries to understand.
The grammar that this parser uses is very similar to the official Python
`grammar files <https://docs.python.org/3/reference/grammar.html>`_.

.. _inference:

Type inference of python code (inference/__init__.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: medi.inference

Inference Values (inference/base_value.py)
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. automodule:: medi.inference.base_value

.. inheritance-diagram::
   medi.inference.value.instance.TreeInstance
   medi.inference.value.klass.ClassValue
   medi.inference.value.function.FunctionValue
   medi.inference.value.function.FunctionExecutionContext
   :parts: 1


.. _name_resolution:

Name resolution (inference/finder.py)
+++++++++++++++++++++++++++++++++++++

.. automodule:: medi.inference.finder


.. _dev-api:

API (api/__init__.py and api/classes.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The API has been designed to be as easy to use as possible. The API
documentation can be found `here <api.html>`_. The API itself contains
little code that needs to be mentioned here. Generally I'm trying to be
conservative with the API.  I'd rather not add new API features if they are not
necessary, because it's much harder to deprecate stuff than to add it later.


.. _core-extensions:

Core Extensions
---------------

Core Extensions is a summary of the following topics:

- :ref:`Iterables & Dynamic Arrays <iterables>`
- :ref:`Dynamic Parameters <dynamic_params>`
- :ref:`Docstrings <docstrings>`
- :ref:`Refactoring <refactoring>`

These topics are very important to understand what Medi additionally does, but
they could be removed from Medi and Medi would still work. But slower and
without some features.

.. _iterables:

Iterables & Dynamic Arrays (inference/value/iterable.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To understand Python on a deeper level, |medi| needs to understand some of the
dynamic features of Python like lists that are filled after creation:

.. automodule:: medi.inference.value.iterable


.. _dynamic_params:

Parameter completion (inference/dynamic_params.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: medi.inference.dynamic_params


.. _docstrings:

Docstrings (inference/docstrings.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: medi.inference.docstrings

.. _refactoring:

Refactoring (inference/api/refactoring.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: medi.api.refactoring


.. _imports-modules:

Imports & Modules
-----------------


- :ref:`Modules <modules>`
- :ref:`Builtin Modules <builtin>`
- :ref:`Imports <imports>`


.. _builtin:

Compiled Modules (inference/compiled.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: medi.inference.compiled


.. _imports:

Imports (inference/imports.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: medi.inference.imports

.. _stubs:

Stubs & Annotations (inference/gradual)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: medi.inference.gradual

.. _caching-recursions:

Caching & Recursions
--------------------


- :ref:`Caching <cache>`
- :ref:`Recursions <recursion>`

.. _cache:

Caching (cache.py)
~~~~~~~~~~~~~~~~~~

.. automodule:: medi.cache

.. _recursion:

Recursions (recursion.py)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: medi.inference.recursion


.. _dev-helpers:

Helper Modules
--------------

Most other modules are not really central to how Medi works. They all contain
relevant code, but you if you understand the modules above, you pretty much
understand Medi.
