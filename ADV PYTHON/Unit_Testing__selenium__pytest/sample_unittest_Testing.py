import unittest
class testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This is setupclass")
    def setUp(self):
        print("This is setup method")
    def test1(self):
        print("This is test1 method")
        #print(10/0)
    def test2(self):
        print("this is test2 method")
    def tearDown(self):
        print("this is teardown method")
        #print(a[1])
    @classmethod
    def tearDownClass(cls):
        print("This is tear down class")
unittest.main()

"""it_Testing/sample_Testing.py"
This is setupclass
This is setup method
This is test1 method
this is teardown method
EEThis is setup method
this is test2 method
this is teardown method
EThis is tear down class

======================================================================
ERROR: test1 (__main__.testing)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/neo/Desktop/DSA/ADV PYTHON/Unit_Testing/sample_Testing.py", line 10, in test1
    print(10/0)
ZeroDivisionError: division by zero

======================================================================
ERROR: test1 (__main__.testing)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/neo/Desktop/DSA/ADV PYTHON/Unit_Testing/sample_Testing.py", line 15, in tearDown
    print(a[1])
NameError: name 'a' is not defined

======================================================================
ERROR: test2 (__main__.testing)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/neo/Desktop/DSA/ADV PYTHON/Unit_Testing/sample_Testing.py", line 15, in tearDown
    print(a[1])
NameError: name 'a' is not defined

----------------------------------------------------------------------
Ran 2 tests in 0.002s

FAILED (errors=3)"""