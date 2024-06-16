import unittest
class sample1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This is setup class from sample1")
    def setUp(self) -> None:
        print("This is setup instance method from sample1")
    def test1(self):
        print("This is test1 method from sample1")
    def test2(self):
        print("This is test2 method from sample1")
    def tearDown(self) -> None:
        print("This is teardown instance method from sample1")
    @classmethod
    def tearDownClass(cls) -> None:
        print("This is tear down class method")
