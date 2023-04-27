import requests
import urllib.request
import base64
import json
import os
import os.path
import sys
import hashlib
from jsondiff import diff

channel = "LATEST_THUNDERBIRD_VERSION"
env_file = os.getenv('GITHUB_ENV') # https://stackoverflow.com/a/40698307

def mzlaJson(path,channel):
    urllib.request.urlretrieve(path,"thunderbird_versions.json")
    with open("thunderbird_versions.json", 'r') as f:
        response = json.load(f)
    os.remove("thunderbird_versions.json")
    return response[channel]

def mzlaDownload(url,filename):
    # URL di esempio https://ftp.mozilla.org/pub/thunderbird/releases/91.7.0/win64/it/Thunderbird%20Setup%2091.7.0.exe
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

tbversion = mzlaJson("https://product-details.mozilla.org/1.0/thunderbird_versions.json",channel)
folder = "tb-win64"
zipfilename = "thunderbird-"+tbversion+"-it.win64.7z"
file_exist = os.path.join(folder,zipfilename)

if (os.path.exists(file_exist)):
    print("Same version, abort.")
    with open(env_file, "a") as ghenv:
        ghenv.write("DIFF=None\n")
    sys.exit
else:
    pkgpath = "https://ftp.mozilla.org/pub/thunderbird/releases/%s/win64/it/Thunderbird Setup %s.exe" % (tbversion,tbversion)
    pkgname = "Thunderbird Setup %s.exe" % tbversion
    download = mzlaDownload(pkgpath,pkgname)
    print(channel,download)
    html = makewebpage(folder,zipfilename)
    with open ("tb64.html", 'w') as fp:
        fp.write(html)

    # https://errorsfixing.com/how-to-set-environment-variables-in-github-actions-using-python/
    # https://stackoverflow.com/a/70123641
    with open(env_file, "a") as ghenv:
        ghenv.write("CHANNEL="+channel)
        ghenv.write("\nPKGNAME="+pkgname)
        ghenv.write("\nTBVERSION="+tbversion)
        ghenv.write("\nTBZIPFILE="+zipfilename)
