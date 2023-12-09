#!/usr/bin/python

import sys

maxAbs = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print(str(maxAbs))
        oldKey = thisKey;
        maxAbs = 0

    oldKey = thisKey
#pilla precio de cada metodo de pago, y compara
    if maxAbs < float(thisSale):
     maxAbs += float(thisSale)

if oldKey != None:
    print("Maximo:"+"\t"+str(maxAbs))

