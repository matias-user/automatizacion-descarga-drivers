from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Home
def move_in_home(driver, wait):

    wait.until(EC.visibility_of_element_located((By.ID, "topMenu1")))
    driver.find_element(By.ID, "topMenu5").click()