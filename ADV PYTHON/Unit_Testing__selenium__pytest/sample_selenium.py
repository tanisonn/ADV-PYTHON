from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.fb.com")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(10)  
driver.get("https://www.google.com")
driver.back()
time.sleep(10)
driver.forward()
driver.close()
