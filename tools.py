from pathlib import Path

import zipfile
import json
import os

def current() -> str:
    return str(Path().absolute())

def unzip(zip, extractTo):
    with zipfile.ZipFile(zip, 'r') as zip_ref:
        zip_ref.extractall(extractTo)
    os.remove(zip)

def textify(lines: str) -> str:
    text = ''
    for line in lines:
        text += line
    return text

def reconfiguration(workspace, name, file):
    workspace["packages"].append(name)
    file.seek(0)
    file.write(json.dumps(workspace, indent=4))
    file.truncate()
    return

def packagesList(workspace):
    return os.listdir(workspace)