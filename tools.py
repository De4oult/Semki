from pathlib import Path

import zipfile
import os

def current():
    return str(Path().absolute())

def unzip(zip, extractTo):
    with zipfile.ZipFile(zip, 'r') as zip_ref:
        zip_ref.extractall(extractTo)
    os.remove(zip)