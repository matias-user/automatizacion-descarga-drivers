import os

def get_msi_downloaded(folder):
    for file in os.listdir(folder):
        if file.lower().endswith(".msi"):
            return os.path.join(folder, file)
    return None