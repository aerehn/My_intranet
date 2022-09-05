from sok_website.settings import MEDIA_ROOT, DEBUG, STATICFILES_DIRS
import zipfile, io, os
from os.path import basename
import shutil
import random
from wsgiref.util import FileWrapper


import time

MAX_RANDOM_VALUE = 1000000


def handle_uploaded_file(f, directory):
    with open(MEDIA_ROOT / directory / f.name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def handle_uploaded_excel_file(f, directory):
    existing_files = (MEDIA_ROOT / "pdfconverter").iterdir()
    for file in existing_files:
        if file.suffix == ".xlsx":
            file.unlink()
    with open(MEDIA_ROOT / directory / f.name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def getTimestamp():
    return str(int(time.time()))

def handle_textnote(data):
    channel=data['channel']
    save_path=MEDIA_ROOT / "boards"
    timestamp = getTimestamp()
    print(timestamp)
    header, content = data["nimi"],data["teksti"].replace("\r","")
    filename = str(timestamp)+"."+header+"."+channel+".txt"
    full_path = save_path/filename
    
    with open(full_path, 'w') as f:
        f.writelines(content)


def handle_photonote(data,photo):
    print(data)
    channel=data['channel']
    extension = str(photo).split(".")[-1]
    save_path=MEDIA_ROOT / "boards"
    timestamp = getTimestamp()
    header = data['nimi'] if data['nimi']!="" else str(photo).split(".")[0]
    filename = str(timestamp)+"."+header+"."+channel+"."+extension
    full_path = save_path/filename
    with open(full_path, "wb+") as destination:
        for chunk in photo.chunks():
            destination.write(chunk)
        destination.close()

