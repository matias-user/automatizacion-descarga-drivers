from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


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