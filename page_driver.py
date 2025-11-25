from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Page Driver/Tool
def move_in_driver(driver, wait, number_floor):
    wait.until(EC.visibility_of_element_located((By.ID, "sidemenuSoftwareDownload")))
    driver.find_element(By.ID, "sidemenuPushPrintDriver").click()

    # Selector jQuery
    btn = wait.until(EC.element_to_be_clickable((By.ID, "SelDeviceWinClientList-button")))
    btn.click()

    option = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//ul[@id='SelDeviceWinClientList-menu']//li[contains(., 'Piso {number_floor}')]")
        )
    )
    option.click()

    # Botón de descarga
    btn_download = driver.find_element(By.CLASS_NAME, "downloadDriverWinClient")
    btn_download.click()