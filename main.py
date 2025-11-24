from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://10.10.100.109/printadminweb")

# Login
input_username = driver.find_element(By.ID, "UserId")
input_password = driver.find_element(By.ID, "Password")
btn_login = driver.find_element(By.ID, "loginButton")

input_username.send_keys("admin")
input_password.send_keys("admin.1111")
btn_login.click()

time.sleep(30)