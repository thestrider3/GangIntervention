# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:20:56 2016

@author: strider
"""
countH = 0
fout = open('Homicide.csv','r')
for row in fout:
    #print(row)
    countH = countH+1
print(countH)
fout.close()

countA = 0
fout = open('Assault.csv','r')
for row in fout:
    #print(row)
    countA = countA+1
print(countA)
fout.close()

countB = 0
fout = open('Battery.csv','r')
for row in fout:
    print(row)
    countB = countB+1
print(countB)
fout.close()

