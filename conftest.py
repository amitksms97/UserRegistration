import pytest

@pytest.fixture
def print_test_statement():
    c = 0
    c += 1
    print("Testing method number {}".format(c))

