#!/usr/bin/python

import sys
import json

# total arguments
# n = len(sys.argv)
# print("Total arguments passed:", n)

# Arguments passed
# print("Name of Python script:", sys.argv[0])

miel = sys.argv[1]

# print(miel)

# json.loads(miel)

# res = json.loads(miel)
res = json.dumps(miel)
print(miel.name)