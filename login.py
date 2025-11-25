from selenium.webdriver.common.by import By


def do_login(driver):
    # Login
    input_username = driver.find_element(By.ID, "UserId")
    input_password = driver.find_element(By.ID, "Password")
    btn_login = driver.find_element(By.ID, "loginButton")

    input_username.send_keys("admin")
    input_password.send_keys("admin.1111")

    driver.find_element(By.CSS_SELECTOR, "#SelectDomain_chosen .chosen-single").click()
    driver.find_element(By.XPATH, "//div[@id='SelectDomain_chosen']//li[text()='(Local)']").click()
    btn_login.click()