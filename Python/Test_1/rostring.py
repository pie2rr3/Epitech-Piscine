#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
    print("")
    exit(84)

strings = sys.argv[1].split()
rostring = ""

for istring in range(1, len(strings)):
    rostring += strings[istring]
    rostring += " "
rostring += strings[0]
print(rostring)