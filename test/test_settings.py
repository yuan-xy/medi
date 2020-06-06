import pytest

from medi import settings
from medi.inference.names import ValueName
from medi.inference.compiled import CompiledValueName
from medi.inference.gradual.typeshed import StubModuleValue


@pytest.fixture()
def auto_import_json(monkeypatch):
    monkeypatch.setattr(settings, 'auto_import_modules', ['json'])


def test_auto_import_modules_imports(auto_import_json, Script):
    main, = Script('from json import tool; tool.main').infer()
    assert isinstance(main._name, CompiledValueName)


def test_cropped_file_size(monkeypatch, get_names, Script):
    code = 'class Foo(): pass\n'
    monkeypatch.setattr(
        settings,
        '_cropped_file_size',
        len(code)
    )

    foo, = get_names(code + code)
    assert foo.line == 1

    # It should just not crash if we are outside of the cropped range.
    script = Script(code + code + 'Foo')
    assert not script.infer()
    assert 'Foo' in [c.name for c in script.complete()]
