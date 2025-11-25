import subprocess

def execute_msi(ruta_msi):
    print(f"Ejecutando MSI: {ruta_msi}")
    subprocess.run(["msiexec", "/i", ruta_msi], shell=True)