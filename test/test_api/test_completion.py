from os.path import join, sep as s, dirname, expanduser
import os
import sys
from textwrap import dedent

import pytest

from ..helpers import root_dir
from medi.api.helpers import _start_match, _fuzzy_match
from medi._compatibility import scandir


def test_in_whitespace(Script):
    code = dedent('''
    def x():
        pass''')
    assert len(Script(code).complete(column=2)) > 20


def test_in_empty_space(Script):
    code = dedent('''\
    class X(object):
        def __init__(self):
            hello
            ''')
    comps = Script(code).complete(3, 7)
    self, = [c for c in comps if c.name == 'self']
    assert self.name == 'self'
    def_, = self.infer()
    assert def_.name == 'X'


def test_indent_value(Script):
    """
    If an INDENT is the next supposed token, we should still be able to
    complete.
    """
    code = 'if 1:\nisinstanc'
    comp, = Script(code).complete()
    assert comp.name == 'isinstance'


def test_keyword_value(Script):
    def get_names(*args, **kwargs):
        return [d.name for d in Script(*args, **kwargs).complete()]

    names = get_names('if 1:\n pass\n')
    assert 'if' in names
    assert 'elif' in names



def test_points_in_completion(Script):
    """At some point, points were inserted into the completions, this
    caused problems, sometimes.
    """
    c = Script("if IndentationErr").complete()
    assert c[0].name == 'IndentationError'
    assert c[0].complete == 'or'


def test_in_comment(Script):
    assert Script(" # Comment").complete()
    # TODO this is a bit ugly, that the behaviors in comments are different.
    assert not Script("max_attr_value = int(2) # Cast to int for spe").complete()


def test_in_comment_before_string(Script):
    assert not Script(" # Foo\n'asdf'").complete(line=1)


def test_async(Script, environment):
    if environment.version_info < (3, 5):
        pytest.skip()

    code = dedent('''
        foo = 3
        async def x():
            hey = 3
              ho''')
    comps = Script(code).complete(column=4)
    names = [c.name for c in comps]
    assert 'foo' in names
    assert 'hey' in names



def test_function_param_usage(Script):
    c, = Script('def func(foo_value):\n str(foo_valu').complete()
    assert c.complete == 'e'
    assert c.name == 'foo_value'

    c1, c2 = Script('def func(foo_value):\n func(foo_valu').complete()
    assert c1.complete == 'e'
    assert c1.name == 'foo_value'
    assert c2.complete == 'e='
    assert c2.name == 'foo_value='


@pytest.mark.parametrize(
    'code, has_keywords', (
        ('', True),
        ('x;', True),
        ('1', False),
        ('1 ', True),
        ('1\t', True),
        ('1\n', True),
        ('1\\\n', True),
    )
)
def test_keyword_completion(Script, code, has_keywords):
    assert has_keywords == any(x.is_keyword for x in Script(code).complete())


f1 = join(root_dir, 'example.py')
f2 = join(root_dir, 'test', 'example.py')
os_path = 'from os.path import *\n'
# os.path.sep escaped
se = s * 2 if s == '\\' else s
current_dirname = os.path.basename(dirname(dirname(dirname(__file__))))



def test_start_match():
    assert _start_match('Condition', 'C')


def test_fuzzy_match():
    assert _fuzzy_match('Condition', 'i')
    assert not _fuzzy_match('Condition', 'p')
    assert _fuzzy_match('Condition', 'ii')
    assert not _fuzzy_match('Condition', 'Ciito')
    assert _fuzzy_match('Condition', 'Cdiio')


def test_ellipsis_completion(Script):
    assert Script('...').complete() == []


def test_completion_cache(Script, module_injector):
    """
    For some modules like numpy, tensorflow or pandas we cache docstrings and
    type to avoid them slowing us down, because they are huge.
    """
    script = Script('import numpy; numpy.foo')
    module_injector(script._inference_state, ('numpy',), 'def foo(a): "doc"')
    c, = script.complete()
    assert c.name == 'foo'
    assert c.type == 'function'
    assert c.docstring() == 'foo(a)\n\ndoc'

    code = dedent('''\
        class foo:
            'doc2'
            def __init__(self):
                pass
        ''')
    script = Script('import numpy; numpy.foo')
    module_injector(script._inference_state, ('numpy',), code)
    # The outpus should still be the same
    c, = script.complete()
    assert c.name == 'foo'
    assert c.type == 'function'
    assert c.docstring() == 'foo(a)\n\ndoc'
    cls, = c.infer()
    assert cls.type == 'class'
    assert cls.docstring() == 'foo()\n\ndoc2'

