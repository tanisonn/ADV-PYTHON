import pytest
class Testing():
    @pytest.fixture(scope='module')# inorder to use the setup and teardown class methods
    def test_setupClass_and_tearDownClass(self):
        print("This is setup class for testing")#this is setup class method
        yield
        print("This is tear down class for testing")# this is teardown class method
    @pytest.fixture()#inorder to use the setup and teardown instance methods
    def test_setup(self):
        print("This is setup method for testing")# this is setup method
        yield
        print("This is teardown class for testing")# this is instance method
    def test_methodA(self,test_setupClass_and_tearDownClass,test_setup):
        print("This is method A")
    def test_methodB(self,test_setupClass_and_tearDownClass,test_setup):
        print("This is method B")

