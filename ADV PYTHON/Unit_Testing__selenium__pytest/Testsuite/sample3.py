from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time
class sample3(unittest.TestCase):
    def setUp(self):
        print("This is setup instance method")
        self.driver=webdriver.Chrome()
    def test(self):
        print("This is test method ")
        driver=self.driver
        driver.get("https://www.google.com")
        sb=driver.find_element(By.NAME,"q")
        sb.send_keys("mahesh babu")
        sb.send_keys(Keys.RETURN)
        wikipedia_link = driver.find_element(By.XPATH, "//h3[text()='Mahesh Babu']")
        wikipedia_link.click()
    def tearDown(self):
        print("This is teardown instance method")
        self.driver.close()