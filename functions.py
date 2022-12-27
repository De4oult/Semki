from tools import current, unzip
from datetime import datetime
from pysondb import db

import urllib.request
import json
import os

workspaces = db.getDb('/usr/lib/semki/workspaces.json')

def initialize(name, author):
    workspaces.add(
        {
            "name"            : name,
            "author"          : author,
            "created"         : datetime.now().strftime("%H:%M:%S %d %B, %Y"),
            "project_folder"  : current(),
            "packages_folder" : current() + '/semki-packages',
        }
    )

    with open(f'{current()}/workspace.json', 'w') as file:
        workspace = {
            "name"        : name,
            "version"     : '1.0.0',
            "description" : '',
            "author"      : author,
            "created"     : datetime.now().strftime("%H:%M:%S %d %B, %Y"),
            "packages"    : [
                
            ],
        }

        try:
            os.mkdir(current() + '/semki-packages')
        except:
            pass

        file.write(json.dumps(workspace, indent=4))
        



workspaces = db.getDb('/usr/lib/semki/workspaces.json')

def download(name):
    projects = workspaces.getBy(
        {
            "project_folder" : current()
        }
    )
    for workspace in projects:
        if workspace["project_folder"] == current():
            saveTo = f'{str(workspace["packages_folder"])}/{str(name)}'
            urllib.request.urlretrieve('http://46.151.27.39/semki-packages/' + str(name) + '.zip', saveTo + '.zip')
            unzip(saveTo + '.zip', saveTo)



def build(name):
    pass