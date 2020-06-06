"""
Test of keywords and ``medi.keywords``
"""

import pytest


def test_goto_keyword(Script):
    """
    Bug: goto assignments on ``in`` used to raise AttributeError::

      'unicode' object has no attribute 'generate_call_path'
    """
    Script('in').goto()


def test_keyword(Script, environment):
    """ github medi-vim issue #44 """
    defs = Script("print").infer()
    if environment.version_info.major < 3:
        assert defs == []
    else:
        assert [d.docstring() for d in defs]

    assert Script("import").goto() == []

    completions = Script("import").complete(1, 1)
    assert len(completions) > 10 and 'if' in [c.name for c in completions]
    assert Script("assert").infer() == []

