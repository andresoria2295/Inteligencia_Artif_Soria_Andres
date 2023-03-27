#!/usr/bin/python3

import random
def lista_random_simple():
    random_numbers = random.sample(range(6), 3)
    print(random_numbers)
    type(random_numbers)
#random.sample(range(hasta el nro tanto), cantidad de valores)

def lista_random_acotada():
    random_acotado = [random.randint(4, 6) for x in range(3)]
    print(random_acotado)
#random.randint (min, max) para un rango de 3 valores.

def take_input():
    #definimos una lista vacia
    lista = []
    #disponemos un ciclo de 5 vueltas
    for x in range(9):
        valor=int(input("Ingrese un valor entero:"))
        lista.append(valor)

        #imprimimos la lista
    print(lista)


if __name__ == '__main__':
    lista_random_simple()
    lista_random_acotada()
    take_input()
