import os
import os.path
import sys
from jsondiff import diff
from r2z_functions import *

channel = "LATEST_THUNDERBIRD_VERSION"
env_file = os.getenv('GITHUB_ENV') # https://stackoverflow.com/a/40698307
tbversion = mzlaJson("https://product-details.mozilla.org/1.0/thunderbird_versions.json",channel)
zipfilename = "thunderbird-"+tbversion+"-it.win32.7z"

if checkversion(tbversion,"r2ztb") == "same":
    print("Same version, abort.")
    with open(env_file, "a") as ghenv:
        ghenv.write("DIFF=None\n")
    sys.exit
else:
    pkgpath = "https://ftp.mozilla.org/pub/thunderbird/releases/%s/win32/it/Thunderbird Setup %s.exe" % (tbversion,tbversion)
    pkgname = "Thunderbird Setup %s.exe" % tbversion
    download = mzlaDownload(pkgpath,pkgname)
    print(channel,download)

    # https://errorsfixing.com/how-to-set-environment-variables-in-github-actions-using-python/
    # https://stackoverflow.com/a/70123641
    with open(env_file, "a") as ghenv:
        ghenv.write("CHANNEL="+channel)
        ghenv.write("\nPKGNAME="+pkgname)
        ghenv.write("\nTBVERSION="+tbversion)
        ghenv.write("\nTBZIPFILE="+zipfilename)
