#!/usr/bin/python3
#coding=utf-8
import copy
import random
from math import exp

factoresX = [0,0,0,1,1,0,1,1]
doble = []
for i in range(0, len(factoresX), 2):
    doble.append(factoresX[i:i+2])
print(doble)
print(doble[2])
print(doble[0][1])
