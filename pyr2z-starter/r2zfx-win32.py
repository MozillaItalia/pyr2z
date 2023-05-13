import requests
import urllib.request
import base64
import json
import os
import os.path
import sys
import hashlib
from jsondiff import diff

channel = "LATEST_FIREFOX_VERSION"
env_file = os.getenv('GITHUB_ENV') # https://stackoverflow.com/a/40698307

def mzlaJson(path,channel):
    urllib.request.urlretrieve(path,"firefox_versions.json")
    with open("firefox_versions.json", 'r') as f:
        response = json.load(f)
    os.remove("firefox_versions.json")
    return response[channel]

def mzlaDownload(url,filename):
    # URL di esempio https://ftp.mozilla.org/pub/firefox/releases/98.0.1/win64/it/Firefox%20Setup%2098.0.1.exe
    url = url.replace(" ", "%20") # https://stackoverflow.com/a/69811079
    urllib.request.urlretrieve(url,filename)
    hash_md5 = hashlib.md5() # https://stackoverflow.com/a/3431838
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def makewebpage(folder,zipfilename):
    pre = mid = post = ""
    with open(os.path.join("include","body-pre")) as fp:
        pre = fp.read()
    with open(os.path.join("include","body-mid")) as fp:
        mid = fp.read()
    with open(os.path.join("include","body-post")) as fp:
        post = fp.read()
    response = pre + folder + "/" + zipfilename + mid + folder + "/" + zipfilename + post
    return response

fxversion = mzlaJson("https://product-details.mozilla.org/1.0/firefox_versions.json",channel)
folder = "fx-win32"
zipfilename = "firefox-"+fxversion+"-it.win32.7z"
file_exist = os.path.join(folder,zipfilename)

if (os.path.exists(file_exist)):
    print("Same version, abort.")
    with open(env_file, "a") as ghenv:
        ghenv.write("DIFF=None\n")
    sys.exit
else:
    pkgpath = "https://ftp.mozilla.org/pub/firefox/releases/%s/win32/it/Firefox Setup %s.exe" % (fxversion,fxversion)
    pkgname = "Firefox Setup %s.exe" % fxversion
    download = mzlaDownload(pkgpath,pkgname)
    print(channel,download)
    html = makewebpage(folder,zipfilename)
    with open ("fx32.html", 'w') as fp:
        fp.write(html)

    # https://errorsfixing.com/how-to-set-environment-variables-in-github-actions-using-python/
    # https://stackoverflow.com/a/70123641
    with open(env_file, "a") as ghenv:
        ghenv.write("CHANNEL="+channel)
        ghenv.write("\nPKGNAME="+pkgname)
        ghenv.write("\nFXVERSION="+fxversion)
        ghenv.write("\nFXZIPFILE="+zipfilename)
