#!/usr/bin/python3
#coding=utf-8
import copy
import random
from math import exp
import matplotlib.pyplot as graph

#new = [[],[],[],[],[]]
#lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
#print(lista)
#nuevo = lista[:3]
#print(nuevo)
#['tres', 'cuatro', 'cinco']
#for i in range(len(new)):
    #print('\n')
    #print(listPesos[i])
    #print('\n')
#    new[i].append(lista[i])
#print(new)

new =[ [],[],[],[],[] ]
lista = [['uno', 'dos', 'tres', 'cuatro', 'cinco'],['seis','siete','ocho','nueve']]
lista2= lista[0]


print(lista)
print(lista2)

for i in range(len(new)):
     new[i].append(lista2[i])

print(new)
