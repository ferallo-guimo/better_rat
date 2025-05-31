import os
import sys
import subprocess
import urllib.request
import socket
import tempfile

URL = "https://products.s.kaspersky-labs.com/homeuser/kaspersky_standard/latest/standard.exe"

def is_connected(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception:
        return False

def download_installer(url, download_path):
    print("Downloading Kaspersky installer...")
    urllib.request.urlretrieve(url, download_path)
    print("Download complete.")

def run_installer(installer_path):
    print("Running installer...")
    subprocess.run([installer_path], shell=True)

def main():
    if not is_connected():
        print("No internet connection.")
        sys.exit(1)

    temp_installer_path = os.path.join(tempfile.gettempdir(), "kaspersky_installer.exe")
    download_installer(URL, temp_installer_path)
    run_installer(temp_installer_path)

if __name__ == "__main__":
    main()
