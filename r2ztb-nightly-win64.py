import os
import os.path
import sys
from jsondiff import diff
from r2z_functions import *

channel = "LATEST_THUNDERBIRD_NIGHTLY_VERSION"
env_file = os.getenv('GITHUB_ENV') # https://stackoverflow.com/a/40698307
tbversion = mzlaJson("https://product-details.mozilla.org/1.0/thunderbird_versions.json",channel)
zipfilename = "thunderbird-nightly-"+tbversion+"-it.win64.7z"

if checkversion(tbversion,"r2ztb-nightly-64") == "same":
    print("Same version, abort.")
    with open(env_file, "a") as ghenv:
        ghenv.write("DIFF=None\n")
    sys.exit
else:
    pkgpath = "https://ftp.mozilla.org/pub/thunderbird/nightly/latest-comm-central-l10n/thunderbird-%s.it.win64.installer.exe" % (tbversion)
    pkgname = "thunderbird-%s.it.win64.installer.exe" % tbversion
    download = mzlaDownload(pkgpath,pkgname)
    print(channel,download)

    # https://errorsfixing.com/how-to-set-environment-variables-in-github-actions-using-python/
    # https://stackoverflow.com/a/70123641
    with open(env_file, "a") as ghenv:
        ghenv.write("CHANNEL="+channel)
        ghenv.write("\nPKGNAME="+pkgname)
        ghenv.write("\nTBVERSION="+tbversion)
        ghenv.write("\nTBZIPFILE="+zipfilename)
