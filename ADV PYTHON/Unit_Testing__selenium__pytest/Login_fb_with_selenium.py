import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import getpass  
class facebook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global a,b
        a=input("Enter your facebook username:")
        b=getpass.getpass("Enter you facebook password(hidden):")
        global driver
        driver=webdriver.Chrome()
        driver.get("https://www.facebook.com")
    def test(self):
        driver.find_element(By.NAME,"email").send_keys(a)
        driver.find_element(By.NAME,"pass").send_keys(b)
        driver.find_element(By.NAME,"login").click()
        time.sleep(1000)
    @classmethod
    def tearDownClass(cls):
        a=int(input())
        driver.close()

unittest.main()