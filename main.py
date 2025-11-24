from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import subprocess
import time
import os

options = Options()
service = Service(ChromeDriverManager().install())

# Carpeta donde se descargará el archivo
folder_downloads = r"C:\Drivers"

# Evitar bloqueos de descarga
prefs = {
    "download.prompt_for_download": False,
    "download.default_directory": folder_downloads,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "safebrowsing.disable_download_protection": True
}

# Permitir descargas “peligrosas”
options.add_argument("--safebrowsing-disable-download-protection")

# Permitir contenido inseguro (HTTP)
options.add_argument("--allow-running-insecure-content")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://10.10.100.109")

options.add_experimental_option("prefs", prefs)

# Mantener Chrome abierto al final
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

# Permitir descargas usando Chrome DevTools Protocol (NECESARIO)
driver.execute_cdp_cmd(
    "Page.setDownloadBehavior",
    {
        "behavior": "allow",
        "downloadPath": folder_downloads
    }
)

driver.get("http://10.10.100.109/printadminweb")
wait = WebDriverWait(driver, 10)

number_floor = 8

# Login
input_username = driver.find_element(By.ID, "UserId")
input_password = driver.find_element(By.ID, "Password")
btn_login = driver.find_element(By.ID, "loginButton")

input_username.send_keys("admin")
input_password.send_keys("admin.1111")

driver.find_element(By.CSS_SELECTOR, "#SelectDomain_chosen .chosen-single").click()
driver.find_element(By.XPATH, "//div[@id='SelectDomain_chosen']//li[text()='(Local)']").click()
btn_login.click()

# Home
wait.until(EC.visibility_of_element_located((By.ID, "topMenu1")))
driver.find_element(By.ID, "topMenu5").click()

# Page Driver/Tool
wait.until(EC.visibility_of_element_located((By.ID, "sidemenuSoftwareDownload")))
driver.find_element(By.ID, "sidemenuPushPrintDriver").click()

wait = WebDriverWait(driver, 15)

# Selector jQuery
btn = wait.until(EC.element_to_be_clickable((By.ID, "SelDeviceWinClientList-button")))
btn.click()

menu = wait.until(EC.visibility_of_element_located((By.ID, "SelDeviceWinClientList-menu")))

option = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, f"//ul[@id='SelDeviceWinClientList-menu']//li[contains(., 'Piso {number_floor}')]")
    )
)
option.click()

# Botón de descarga
btn_download = driver.find_element(By.CLASS_NAME, "downloadDriverWinClient")
btn_download.click()

# ---------------- FUNCIONES DE DESCARGA -------------------

def esperar_descarga_real(download_dir, timeout=120):
    """
    Espera hasta que el archivo descargado deje de aumentar su tamaño.
    Funciona incluso cuando no existe .crdownload.
    """
    tiempo_inicio = time.time()
    archivo_descarga = None
    tamano_anterior = -1

    while True:
        archivos = [f for f in os.listdir(download_dir) if not f.endswith(".crdownload")]

        if archivos:
            # Archivo más reciente
            archivo_descarga = max(
                (os.path.join(download_dir, f) for f in archivos),
                key=os.path.getmtime
            )

            tamano_actual = os.path.getsize(archivo_descarga)

            # Si el tamaño no cambia → terminó
            if tamano_actual == tamano_anterior:
                return archivo_descarga

            tamano_anterior = tamano_actual

        if time.time() - tiempo_inicio > timeout:
            raise TimeoutError("La descarga no terminó a tiempo.")

        time.sleep(1)

# Esperar que termine la descarga
archivo_final = esperar_descarga_real(folder_downloads)
print("Descarga completa:", archivo_final)

# -----------------------------------------------------------

def get_msi_downloaded(folder):
    for file in os.listdir(folder):
        if file.lower().endswith(".msi"):
            return os.path.join(folder, file)
    return None

msi = get_msi_downloaded(folder_downloads)

def execute_msi(ruta_msi):
    print(f"Ejecutando MSI: {ruta_msi}")
    subprocess.run(["msiexec", "/i", ruta_msi], shell=True)

if msi:
    execute_msi(msi)
else:
    print("No se encontró archivo MSI en la carpeta Drivers.")

time.sleep(15)
