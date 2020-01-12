#!/usr/bin/python

# Program:  count2json
# Author:   @iamtsofu
# Date:     2020/01/12
# License:  MIT
# Purpose:  This program is designed to count each line in a file,
#           and export list of them sorted in descending order in JSON format


import sys
import pandas as pd

dic = {}


# error checks
if len(sys.argv) != 3:
    print("Call program as:\n\n\t$ python3 count2json.py [input file] [output file]\n")
    quit()

# opens input file and creates list
try:
    with open(sys.argv[1],"r") as f:
        ip = f.readlines()
        ip = [x.strip() for x in ip]
        f.close()
        print(f"Found {sys.argv[1]}")
except FileNotFoundError:
    print(f"Could not find {sys.argv[1]}\nQuiting program")
    quit()

# populates dic and counts unique lines
print("sorting...")
for i in ip:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# creates df from dic, sorts by occurance, exports to json
df = pd.DataFrame.from_dict(dic,orient="index")
df = df.sort_values(by=[0],ascending=False)
df.to_json(sys.argv[2])
print(f"Done.\n\nFile at {sys.argv[2]}")
