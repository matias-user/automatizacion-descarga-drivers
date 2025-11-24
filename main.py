from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://10.10.100.109/printadminweb")
wait = WebDriverWait(driver, 10)

# Login
input_username = driver.find_element(By.ID, "UserId")
input_password = driver.find_element(By.ID, "Password")
btn_login = driver.find_element(By.ID, "loginButton")

input_username.send_keys("admin")
input_password.send_keys("admin.1111")
# El select para elegir el dominio, es con una librería por lo que se usan estas dos lineas para porder hacer click
driver.find_element(By.CSS_SELECTOR, "#SelectDomain_chosen .chosen-single").click()
driver.find_element(By.XPATH, "//div[@id='SelectDomain_chosen']//li[text()='(Local)']").click()
btn_login.click()


# Home
# Esperar que cargue el 
wait.until(EC.visibility_of_element_located((By.ID, "topMenu1")))
anchor_driver_tool = driver.find_element(By.ID, "topMenu5")

anchor_driver_tool.click()

# Page Driver/Tool
wait.until(EC.visibility_of_element_located((By.ID, "sidemenuSoftwareDownload")))
anchor_push_print_driver = driver.find_element(By.ID, "sidemenuPushPrintDriver") 
anchor_push_print_driver.click()

wait = WebDriverWait(driver, 15)

# 1. CLIC EN EL SELECT (el botón creado por jQuery UI)
btn = wait.until(EC.element_to_be_clickable((By.ID, "SelDeviceWinClientList-button")))
btn.click()

# 2. ESPERAR A QUE APAREZCA EL MENÚ
menu = wait.until(EC.visibility_of_element_located((By.ID, "SelDeviceWinClientList-menu")))

# 3. BUSCAR LA OPCIÓN POR TEXTO CONTENIDO
option = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//ul[@id='SelDeviceWinClientList-menu']//li[contains(., 'Piso 10 - Centro')]")
    )
)
# 4. CLIC EN LA OPCIÓN
option.click()

select = wait.until(EC.presence_of_element_located(
    (By.ID, "SelDeviceWinClientList")
))
print_options = select.find_elements(By.TAG_NAME, "option")
ubications_list = [opt.text.split("|")[0].strip() for opt in print_options ]


print(ubications_list)

time.sleep(15)