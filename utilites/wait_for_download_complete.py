import time
import os

def wait_for_download_complete(download_dir:str, timeout=120):
    start_time = time.time()
    downloaded_file = None
    previous_size = -1

    while True:
        files = [f for f in os.listdir(download_dir) if not f.endswith(".crdownload")]

        if files:
            downloaded_file = max(
                (os.path.join(download_dir, f) for f in files),
                key=os.path.getmtime
            )

            current_size = os.path.getsize(downloaded_file)

            if current_size == previous_size:
                return downloaded_file

            previous_size = current_size

        if time.time() - start_time > timeout:
            raise TimeoutError("La descarga no termino a tiempo")

        time.sleep(1)
