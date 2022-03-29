import requests
import base64
import os
import shutil

def r2zTempClean():
    shutil.rmtree('./FxTemp32', ignore_errors=True)
    shutil.rmtree('./FxTemp64', ignore_errors=True)
    shutil.rmtree('./TbTemp32', ignore_errors=True)
    shutil.rmtree('./TbTemp64', ignore_errors=True)
    shutil.rmtree('./core32', ignore_errors=True)
    shutil.rmtree('./core64', ignore_errors=True)
    os.remove(os.environ.get("PKGNAME"))
    return

r2zTempClean()
