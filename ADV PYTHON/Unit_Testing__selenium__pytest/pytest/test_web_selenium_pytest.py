import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Test_class():
    @pytest.fixture(scope='module')
    def setupclass_and_teardownclass(self):
        global drive
        drive=webdriver.Chrome()
        drive.get("https://www.google.com")
        print("Set up class method executed:")
        yield
        print("Tear down class method executed")
        drive.close()
    @pytest.fixture()
    def setup_and_teardown(self):
        print("Setup method executed")
        yield
        print("Tear down method executed")
    def test_methodA(self,setupclass_and_teardownclass,setup_and_teardown):
        print("Test method executed")
        ke=drive.find_element(By.CLASS_NAME,"gLFyf")
        ke.send_keys("Vijay devarakonda")
        ke.send_keys(Keys.RETURN)
        drive.find_element(By.XPATH,"//h3[text()='Vijay Deverakonda']").click()

        