import hashlib
import json
import os
import shutil
import subprocess
import urllib.request

destfolder = "C:/Users/giovanni.solone/TbDaily"

def mzlaJson(path,channel):
    urllib.request.urlretrieve(path,"channels.json")
    with open("channels.json", 'r') as f:
        response = json.load(f)
    os.remove("channels.json")
    return response[channel]

def mzlaDownload(url,filename):
    url = url.replace(" ", "%20") # https://stackoverflow.com/a/69811079
    urllib.request.urlretrieve(url,filename)
    hash_md5 = hashlib.md5() # https://stackoverflow.com/a/3431838
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

shutil.rmtree("core", ignore_errors=True)

channel = "LATEST_THUNDERBIRD_NIGHTLY_VERSION"
tbversion = mzlaJson("https://product-details.mozilla.org/1.0/thunderbird_versions.json",channel)
zipfilename = "thunderbird-nightly-"+tbversion+"-it.win64.7z"
pkgpath = "https://ftp.mozilla.org/pub/thunderbird/nightly/latest-comm-central-l10n/thunderbird-%s.it.win64.installer.exe" % (tbversion)
pkgname = "thunderbird-%s.it.win64.installer.exe" % tbversion

mzlaDownload(pkgpath,pkgname)
subprocess.call(["C:/Program Files/7-Zip/7z.exe", "x", pkgname])

shutil.rmtree('core/uninstall')
shutil.copytree("core", destfolder, dirs_exist_ok=True)

os.remove("setup.exe")
os.remove(pkgname)
shutil.rmtree("core", ignore_errors=True)