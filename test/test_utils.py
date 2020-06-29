from medi import utils


def test_version_info():
    assert utils.version_info()[:2] > (0, 7)
