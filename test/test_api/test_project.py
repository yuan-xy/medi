import os
import sys

import pytest

from ..helpers import get_example_dir, set_cwd, root_dir, test_dir
from medi.api import Project, get_default_project




def test_demo_default_project_of_file(Script):
    project = get_default_project("demo", __file__)
    d = os.path.dirname
    assert project._path == d(d(d(__file__)))


def test_added_sys_path(inference_state):
    project = get_default_project("python")
    p = '/some_random_path'
    project.added_sys_path = [p]
    assert p in project._get_sys_path(inference_state)


def test_load_save_project(tmpdir):
    project = Project(tmpdir.strpath, added_sys_path=['/foo'])
    project.save()

    loaded = Project.load(tmpdir.strpath)
    assert loaded.added_sys_path == ['/foo']


@pytest.mark.parametrize(
    'string, full_names, kwargs', [
        ('test_load_save_project', ['test_api.test_project.test_load_save_project'], {}),
        ('test_load_savep', [], dict(complete=True)),
        ('test_load_save_p', ['test_api.test_project.test_load_save_project'],
         dict(complete=True)),
        ('test_load_save_p', ['test_api.test_project.test_load_save_project'],
         dict(complete=True, all_scopes=True)),

        ('some_search_test_var', [], {}),
        ('some_search_test_var', ['test_api.test_project.test_search.some_search_test_var'],
         dict(all_scopes=True)),
        ('some_search_test_var', ['test_api.test_project.test_search.some_search_test_var'],
         dict(complete=True, all_scopes=True)),

        ('sample_int', ['helpers.sample_int'], {}),
        ('sample_int', ['helpers.sample_int'], dict(all_scopes=True)),

        # With modules
        ('test_project.test_search', ['test_api.test_project.test_search'], {}),
        ('test_project.test_searc', ['test_api.test_project.test_search'], dict(complete=True)),
        ('test_api.test_project.test_search', ['test_api.test_project.test_search'], {}),
        ('test_api.test_project.test_sear', ['test_api.test_project.test_search'],
         dict(complete=True)),

        # With namespace
        ('implicit_namespace_package.ns1.pkg',
         ['examples.implicit_namespace_package.ns1.pkg'], {}),
        ('implicit_namespace_package.ns1.pkg.ns1_file',
         ['examples.implicit_namespace_package.ns1.pkg.ns1_file'], {}),
        ('examples.implicit_namespace_package.ns1.pkg.ns1_file',
         ['examples.implicit_namespace_package.ns1.pkg.ns1_file'], {}),
        ('implicit_namespace_package.ns1.pkg.',
         ['examples.implicit_namespace_package.ns1.pkg.ns1_file'],
         dict(complete=True)),
        ('implicit_namespace_package.',
         ['examples.implicit_namespace_package.ns1',
          'examples.implicit_namespace_package.ns2'],
         dict(complete=True)),

        # With stubs
        ('with_python.module', ['examples.stub_packages.with_python.module'], {}),
        ('with_python.modul', ['examples.stub_packages.with_python.module'],
         dict(complete=True)),
        ('no_python.foo', ['stub:examples.stub_packages.no_python.foo'], {}),
        ('no_python.fo', ['stub:examples.stub_packages.no_python.foo'],
         dict(complete=True)),
        ('with_python-stubs.module', [], {}),
        ('no_python-stubs.foo', [], {}),
        # Both locations are given, because they live in separate folders (one
        # suffixed with -stubs.
        ('with_python', ['examples.stub_packages.with_python'], {}),
        ('no_python', ['stub:examples.stub_packages.no_python'], {}),
        # Completion stubs
        ('stub_only', ['stub:completion.stub_folder.stub_only',
                       'stub:examples.stub_packages.with_python.stub_only'], {}),
        ('with_stub', ['completion.stub_folder.with_stub'], {}),
        ('with_stub.in_with_stub_both',
         ['completion.stub_folder.with_stub.in_with_stub_both'], {}),
        ('with_stub.in_with_stub_python',
         ['completion.stub_folder.with_stub.in_with_stub_python'], {}),
        ('with_stub.in_with_stub_stub',
         ['stub:completion.stub_folder.with_stub.in_with_stub_stub'], {}),
        # Completion stubs: Folder
        ('with_stub_folder', ['completion.stub_folder.with_stub_folder'], {}),
        ('with_stub_folder.nested_with_stub',
         ['completion.stub_folder.with_stub_folder.nested_with_stub'], {}),
        ('nested_with_stub',
         ['completion.stub_folder.stub_only_folder.nested_with_stub',
          'completion.stub_folder.with_stub_folder.nested_with_stub'], {}),

        # On sys path
        ('json.dumps', ['json.dumps'], {}),  # stdlib + stub
        ('multiprocessing', ['multiprocessing'], {}),
        ('multiprocessin', ['multiprocessing'], dict(complete=True)),
    ]
)
@pytest.mark.skipif(sys.version_info < (3, 6), reason="Ignore Python 2, because EOL")
def test_search(string, full_names, kwargs, skip_pre_python36):
    some_search_test_var = 1.0
    project = Project(test_dir)
    if kwargs.pop('complete', False) is True:
        defs = project.complete_search(string, **kwargs)
    else:
        defs = project.search(string, **kwargs)
    assert sorted([('stub:' if d.is_stub() else '') + d.full_name for d in defs]) == full_names


@pytest.mark.parametrize(
    'string, completions, all_scopes', [
        ('SomeCl', ['ass'], False),
        ('twic', [], False),
        ('twic', ['e', 'e'], True),
        ('test_load_save_p', ['roject'], False),
    ]
)
@pytest.mark.skipif(sys.version_info < (3, 6), reason="Ignore Python 2, because EOL")
def test_complete_search(Script, string, completions, all_scopes, skip_pre_python36):
    project = Project(test_dir)
    defs = project.complete_search(string, all_scopes=all_scopes)
    assert [d.complete for d in defs] == completions
