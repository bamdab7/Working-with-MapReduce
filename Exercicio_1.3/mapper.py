#!/usr/bin/python

import sys


for line in sys.stdin:
   data = line.strip().split("\t")
   _, _, _, _, cost, payment = data
   
   print(payment+"\t"+cost)	
   
   
   

