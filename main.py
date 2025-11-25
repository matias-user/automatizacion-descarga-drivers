from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import do_login
from page_home import move_in_home
from page_driver import move_in_driver
from config import folder_downloads
from utilites.wait_for_download_complete import wait_for_download_complete
from utilites.get_msi_downloaded import get_msi_downloaded
from utilites.execute_msi import execute_msi

def main():

    number_floor = input("Ingresa el número de piso del colaborador (6 a 14): ")

    from config import driver
    wait = WebDriverWait(driver, 10)

    do_login(driver=driver)

    move_in_home(driver=driver, wait=wait)

    move_in_driver(driver=driver, wait=wait, number_floor=number_floor)

    # Esperar que termine la descarga
    final_file = wait_for_download_complete(folder_downloads)
    print("Descarga completa:", final_file)

    msi = get_msi_downloaded(folder_downloads)

    if msi:
        execute_msi(msi)
    else:
        print("No se encontró archivo MSI en la carpeta Drivers.")
if __name__ == '__main__':
    main()