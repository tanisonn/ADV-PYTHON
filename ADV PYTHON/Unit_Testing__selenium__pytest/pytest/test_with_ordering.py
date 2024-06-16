import pytest
@pytest.mark.run(order=3)
def test_methodA():
    print("This is method one")
@pytest.mark.run(order=2)
def test_methodB():
    print("this is method two")
@pytest.mark.run(order=1)
def test_methodC():
    print("This is method three")


