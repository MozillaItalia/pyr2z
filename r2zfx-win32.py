import os
import os.path
import sys
from jsondiff import diff
from r2z_functions import *

channel = "LATEST_FIREFOX_VERSION"
env_file = os.getenv('GITHUB_ENV') # https://stackoverflow.com/a/40698307
fxversion = mzlaJson("https://product-details.mozilla.org/1.0/firefox_versions.json",channel)
zipfilename = "firefox-"+fxversion+"-it.win32.7z"

if checkversion(fxversion,"r2zfx") == "same":
    print("Same version, abort.")
    with open(env_file, "a") as ghenv:
        ghenv.write("DIFF=None\n")
    sys.exit
else:
    pkgpath = "https://ftp.mozilla.org/pub/firefox/releases/%s/win32/it/Firefox Setup %s.exe" % (fxversion,fxversion)
    pkgname = "Firefox Setup %s.exe" % fxversion
    download = mzlaDownload(pkgpath,pkgname)
    print(channel,download)

    # https://errorsfixing.com/how-to-set-environment-variables-in-github-actions-using-python/
    # https://stackoverflow.com/a/70123641
    with open(env_file, "a") as ghenv:
        ghenv.write("CHANNEL="+channel)
        ghenv.write("\nPKGNAME="+pkgname)
        ghenv.write("\nFXVERSION="+fxversion)
        ghenv.write("\nFXZIPFILE="+zipfilename)
