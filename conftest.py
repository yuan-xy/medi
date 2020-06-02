import tempfile
import shutil
import os
import sys
from functools import partial

import pytest

import medi
from medi.api.environment import get_system_environment, InterpreterEnvironment
from medi._compatibility import py_version
from test.helpers import test_dir

collect_ignore = [
    'setup.py',
    'medi/__main__.py',
    'medi/inference/compiled/subprocess/__main__.py',
    'build/',
    'test/examples',
]
if sys.version_info < (3, 6):
    # Python 2 not supported syntax
    collect_ignore.append('test/test_inference/test_mixed.py')


# The following hooks (pytest_configure, pytest_unconfigure) are used
# to modify `medi.settings.cache_directory` because `clean_medi_cache`
# has no effect during doctests.  Without these hooks, doctests uses
# user's cache (e.g., ~/.cache/medi/).  We should remove this
# workaround once the problem is fixed in pytest.
#
# See:
# - https://github.com/davidhalter/medi/pull/168
# - https://bitbucket.org/hpk42/pytest/issue/275/

medi_cache_directory_orig = None
medi_cache_directory_temp = None


def pytest_addoption(parser):
    parser.addoption("--medi-debug", "-D", action='store_true',
                     help="Enables Jedi's debug output.")

    parser.addoption("--warning-is-error", action='store_true',
                     help="Warnings are treated as errors.")

    parser.addoption("--env", action='store',
                     help="Execute the tests in that environment (e.g. 35 for python3.5).")
    parser.addoption("--interpreter-env", "-I", action='store_true',
                     help="Don't use subprocesses to guarantee having safe "
                          "code execution. Useful for debugging.")


def pytest_configure(config):
    global medi_cache_directory_orig, medi_cache_directory_temp
    medi_cache_directory_orig = medi.settings.cache_directory
    medi_cache_directory_temp = tempfile.mkdtemp(prefix='medi-test-')
    medi.settings.cache_directory = medi_cache_directory_temp

    if config.option.medi_debug:
        medi.set_debug_function()

    if config.option.warning_is_error:
        import warnings
        warnings.simplefilter("error")


def pytest_unconfigure(config):
    global medi_cache_directory_orig, medi_cache_directory_temp
    medi.settings.cache_directory = medi_cache_directory_orig
    shutil.rmtree(medi_cache_directory_temp)


@pytest.fixture(scope='session')
def clean_medi_cache(request):
    """
    Set `medi.settings.cache_directory` to a temporary directory during test.

    Note that you can't use built-in `tmpdir` and `monkeypatch`
    fixture here because their scope is 'function', which is not used
    in 'session' scope fixture.

    This fixture is activated in ../pytest.ini.
    """
    from medi import settings
    old = settings.cache_directory
    tmp = tempfile.mkdtemp(prefix='medi-test-')
    settings.cache_directory = tmp

    @request.addfinalizer
    def restore():
        settings.cache_directory = old
        shutil.rmtree(tmp)


@pytest.fixture(scope='session')
def environment(request):
    version = request.config.option.env
    if version is None:
        version = os.environ.get('JEDI_TEST_ENVIRONMENT', str(py_version))

    if request.config.option.interpreter_env or version == 'interpreter':
        return InterpreterEnvironment()

    return get_system_environment(version[0] + '.' + version[1:])


@pytest.fixture(scope='session')
def Script(environment):
    return partial(medi.Script, environment=environment)


@pytest.fixture(scope='session')
def ScriptWithProject(Script):
    project = medi.Project(test_dir)
    return partial(medi.Script, project=project)


@pytest.fixture(scope='session')
def get_names(Script):
    return lambda code, **kwargs: Script(code).get_names(**kwargs)


@pytest.fixture(scope='session', params=['goto', 'infer'])
def goto_or_infer(request, Script):
    return lambda code, *args, **kwargs: getattr(Script(code), request.param)(*args, **kwargs)


@pytest.fixture(scope='session', params=['goto', 'help'])
def goto_or_help(request, Script):
    return lambda code, *args, **kwargs: getattr(Script(code), request.param)(*args, **kwargs)


@pytest.fixture(scope='session', params=['goto', 'help', 'infer'])
def goto_or_help_or_infer(request, Script):
    return lambda code, *args, **kwargs: getattr(Script(code), request.param)(*args, **kwargs)


@pytest.fixture(scope='session')
def has_typing(environment):
    if environment.version_info >= (3, 5, 0):
        # This if is just needed to avoid that tests ever skip way more than
        # they should for all Python versions.
        return True

    script = medi.Script('import typing', environment=environment)
    return bool(script.infer())


@pytest.fixture(scope='session')
def has_django(environment):
    return False


@pytest.fixture(scope='session')
def medi_path():
    return os.path.dirname(__file__)


@pytest.fixture()
def skip_python2(environment):
    if environment.version_info.major == 2:
        # This if is just needed to avoid that tests ever skip way more than
        # they should for all Python versions.
        pytest.skip()


@pytest.fixture()
def skip_pre_python38(environment):
    if environment.version_info < (3, 8):
        # This if is just needed to avoid that tests ever skip way more than
        # they should for all Python versions.
        pytest.skip()


@pytest.fixture()
def skip_pre_python37(environment):
    if environment.version_info < (3, 7):
        # This if is just needed to avoid that tests ever skip way more than
        # they should for all Python versions.
        pytest.skip()


@pytest.fixture()
def skip_pre_python35(environment):
    if environment.version_info < (3, 5):
        # This if is just needed to avoid that tests ever skip way more than
        # they should for all Python versions.
        pytest.skip()


@pytest.fixture()
def skip_pre_python36(environment):
    if environment.version_info < (3, 6):
        # This if is just needed to avoid that tests ever skip way more than
        # they should for all Python versions.
        pytest.skip()
