import pytest
def test_methodA(setup_common_and_teardown_class,setup_teardown):
    print("testA executed")
def test_methodB(setup_common_and_teardown_class,setup_teardown):
    print("TestB executed")
# the command to get output in html fform is "py.test -s -v test_with_outputpage.py --html=output.html"
# a new html page is created