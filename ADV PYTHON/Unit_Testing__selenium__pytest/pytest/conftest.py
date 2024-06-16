import pytest
@pytest.fixture(scope="module")
def setup_common_and_teardown_class(scope="module"):
    print("This is setup class method")
    yield
    print("this is teardown class method")
@pytest.fixture()
def setup_teardown():
    print("this is setup instance mthod")
    yield
    print("this is teardown instanc method")
