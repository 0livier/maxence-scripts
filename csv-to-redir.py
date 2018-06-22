#!/usr/bin/env python

FOUR_O_FOUR_COLUMN = 0
REDIRECT_COLUMN = 1

import sys
import re
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--nginx", help="generate rewrites for Nginx instead of Apache", action="store_true")
args = parser.parse_args()

infile = sys.stdin
next(infile) # Skip first line that should contains headers

def formatRewrite(fromPath, toUrl):
    if (args.nginx):
        return "rewrite ^%s %s permanent;" % (fromPath, toUrl)
    return "RedirectMatch 301 \"^%s\" \"%s\"" % (fromPath, toUrl)

# 200, 301 are acceptable response
def isDocumentAvailable(url):
    return 0 == subprocess.call(["curl", "--silent", url]) # 0 for no error, 1 for error

for line in infile:
    fields = line.split(',')
    fromPath = re.sub(r'^https?://[^/]+', '', fields[FOUR_O_FOUR_COLUMN])
    toUrl = fields[REDIRECT_COLUMN].rstrip()
    if (not isDocumentAvailable(toUrl)) :
        print("The following URL is not available : %s" % toUrl)
        sys.exit()

    print(formatRewrite(fromPath, toUrl))

