#!/usr/bin/python

import sys

maxPayment = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey+"\t"+str(maxPayment))
        oldKey = thisKey;
        maxPayment = 0

    oldKey = thisKey
#pilla precio de cada metodo de pago, y compara
    if maxPayment < float(thisSale):
     maxPayment += float(thisSale)

if oldKey != None:
    print(oldKey+"\t"+str(maxPayment))

