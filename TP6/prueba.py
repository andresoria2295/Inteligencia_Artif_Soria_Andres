#!/usr/bin/python3
#coding=utf-8
import copy
import random
from math import exp

a = [0,1,2,3]
b = [4,5,6,7]
c = [8,9,10,11]
d = [12,13]

lista = []

lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)

print(lista)
print(lista[0])

for ent in range(4):
    if(lista[ent] == lista[1]):
        entradas = lista[ent]
        print('salio')
    elif(lista[ent] == lista[2]):
        entradas = lista[ent]
        print('otro')
    print('sigue')
