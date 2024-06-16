import pytest
class TestSample():# should start with Test
    def test_sample1(self): # should start with test_
        print("This is sample1")
    def test_sample2(self):
        print("This is sample2")
        #print(10/0)
    def hello(self):# this is not going to execute since mthod should start with "test_"
        print("hello")
#inorder to run this code the command would be : py.test {this runs all the pytest scripts}
# to run a specific file then py.test {filename}
# to print the output to console then go for py.test -s {filename}
# to print with passed statements go with py.test -s -v {filenmae}


"""
========================================= test session starts =========================================
platform linux -- Python 3.10.12, pytest-8.2.2, pluggy-1.5.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/neo/Desktop/DSA/ADV PYTHON/Unit_Testing/pyscript
plugins: anyio-3.7.1
collected 2 items                                                                                     

test_sample.py::TestSample::test_sample1 This is sample1
PASSED
test_sample.py::TestSample::test_sample2 This is sample2
PASSED

========================================== 2 passed in 0.01s ==========================================
neo@neo-Latitude-7490:~/Desktop/DSA/ADV PYTHON/Unit_Testing/pyscript$ /bin/python3 "/home/neo/Desktop/DSA/ADV PYTHON/Unit_Testing/pyscript/test_sample.py"
neo@neo-Latitude-7490:~/Desktop/DSA/ADV PYTHON/Unit_Testing/pyscript$ py.test -s -v
========================================= test session starts =========================================
platform linux -- Python 3.10.12, pytest-8.2.2, pluggy-1.5.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/neo/Desktop/DSA/ADV PYTHON/Unit_Testing/pyscript
plugins: anyio-3.7.1
collected 2 items                                                                                     

test_sample.py::TestSample::test_sample1 This is sample1
PASSED
test_sample.py::TestSample::test_sample2 This is sample2
FAILED

============================================== FAILURES ===============================================
_______________________________________ TestSample.test_sample2 _______________________________________

self = <test_sample.TestSample object at 0x7f6015261bd0>

    def test_sample2(self):
        print("This is sample2")
>       print(10/0)
E       ZeroDivisionError: division by zero

test_sample.py:7: ZeroDivisionError
======================================= short test summary info =======================================
FAILED test_sample.py::TestSample::test_sample2 - ZeroDivisionError: division by zero
===================================== 1 failed, 1 passed in 0.07s ====================================="""