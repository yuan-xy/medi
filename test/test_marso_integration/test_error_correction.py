from textwrap import dedent


def test_incomplete_function(Script):
    source = '''return ImportErr'''

    script = Script(dedent(source))
    assert script.complete(1, 3)

