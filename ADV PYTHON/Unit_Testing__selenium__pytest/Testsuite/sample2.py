import unittest
class sam(unittest.TestCase):
    def setUp(self) -> None:
        print("This is setup method from sam")
    def test_1(self):
        print("This is test method from sam")
    def tearDown(self) -> None:
        print("This is tear down from same")

