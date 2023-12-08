#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

total_sales = 0
for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, store, item, cost, payment = data
    #print(store+"\t"+cost)
    cost = float(cost)

    total_sales+=cost
print("Total Ventas:\t"+ str(total_sales))
