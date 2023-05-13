import urllib.request
import json
import os
import os.path
import hashlib
from jsondiff import diff

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

def checkrepo(updates_file):
    with open(updates_file, "r") as f:
        content = f.read()
        first_line = content.split('\n', 1)[0]
    return first_line

def checkversion(pkgversion,updatefile):
    if (pkgversion != checkrepo(os.path.join("updates",updatefile))):
        print("New version is available: %s, i'm updating version file." % pkgversion)
        writenewversion(os.path.join("updates",updatefile),pkgversion)
        return "new"
    else:
        print("Latest version is the same of the repository, skip.")
        return "same"

def writenewversion(updates_file,newversion):
    with open(updates_file, "w") as readversion:
        readversion.write(newversion)
    return