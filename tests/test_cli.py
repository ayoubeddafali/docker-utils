import pytest
from dutils import cli

@pytest.fixture()
def parser():
    return cli.create_parser()


def test_first_pass(parser):
    """
    test 
    """
    assert True     











