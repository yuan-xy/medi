from textwrap import dedent


def test_error_correction_with(Script):
    source = """
    with open() as f:
        try:
            f."""
    comps = Script(source).complete()
    assert len(comps) > 30
    # `open` completions have a closed attribute.
    assert [1 for c in comps if c.name == 'closed']



def test_incomplete_function(Script):
    source = '''return ImportErr'''

    script = Script(dedent(source))
    assert script.complete(1, 3)


def test_decorator_string_issue(Script):
    """
    Test case from #589
    """
    source = dedent('''\
    """
      @"""
    def bla():
      pass

    bla.''')

    s = Script(source)
    assert s.complete()
    assert s._get_module_context().tree_node.get_code() == source
