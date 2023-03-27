#!/usr/bin/python3
#coding=utf-8
import copy
import random
from random import shuffle
N = []

#Función que toma posición del elemento nulo.
def nodoNulo(lista):
    for i in range(9):
        if lista[i]==0:
            return i
            #moverArriba(i,N)
            #moverAbajo(i,N)
            #moverIzquierda(i,N)
            #moverDerecha(i,N)
            #print (i)

#Función que desplaza el elemento nulo hacia arriba.
def  moverArriba (b,N):
    subir =  copy.deepcopy(N)
    if  b>2:
        subir[b] = subir[b-3]   # Intercambiar fichas
        subir[b-3] = 0
    #print(subir)
    return subir       # Volver nuevo nodo

#Función que desplaza el elemento nulo hacia abajo.
def moverAbajo(b,N):
    bajar = copy.deepcopy(N)
    if b<6:
        bajar[b]=bajar[b+3]  # Swap Tiles
        bajar[b+3] = 0
    #print(bajar)
    return bajar       # Return New Node

#Función que desplaza el elemento nulo hacia la izquierda.
def moverIzquierda(b,N):
    izq = copy.deepcopy(N)
    if b!=0 and b!=3 and b!=6:
        izq[b] = izq[b-1]  # Swap Tiles
        izq[b-1] = 0
    #print(izq)
    return izq       # Return New Node

#Función que desplaza el elemento nulo hacia la derecha.
def moverDerecha(b,N):
    der = copy.deepcopy(N)
    if b!=2 and b!=5 and b!=8:
        der[b] = der[b+1]  # Swap Tiles
        der[b+1] = 0
    #print(der)
    return der       # Return New Node

#Función que desordena lista inicial.
def listaRandom(listaMod):
    for x in range(50):
        mov = random.randint(1,4)
        N = nodoNulo(listaMod)
        if mov == 1:
            listaMod = moverArriba(N,listaMod)
            print(listaMod)
            #return listaMod
            #break
        elif mov == 2:
            listaMod = moverAbajo(N,listaMod)
            print(listaMod)
            #return listaMod
            #break
        elif mov == 3:
            listaMod = moverIzquierda(N,listaMod)
            print(listaMod)
            #return listaMod
            #break
        elif mov == 4:
            listaMod = moverDerecha(N,listaMod)
            print(listaMod)
            #return listaMod
            #break
    return listaMod

#Función que cuenta elementos.
def contador():
  numero = 0
  while True:
    numero += 1
    yield numero

#Función que encuentra lista inicial a partir de la lista modificada.
def busquedaAnchura(lista,lista_modificada):
    #padre = dict(lista)
    #padre = (dict(zip(lista, lista_modificada)))
    encontrado = False
    final_count = 0
    sumatoria = 0
    if lista_modificada != lista:
        while not encontrado:
            cuenta = contador()
            for i in lista_modificada:
                mov = random.randint(1,4)
                N = nodoNulo(lista_modificada)
                if mov == 1:
                    lista_modificada = moverArriba(N,lista_modificada)
                    print(lista_modificada)
                elif mov == 2:
                    lista_modificada = moverAbajo(N,lista_modificada)
                    print(lista_modificada)
                elif mov == 3:
                    lista_modificada = moverIzquierda(N,lista_modificada)
                    print(lista_modificada)
                elif mov == 4:
                    lista_modificada = moverDerecha(N,lista_modificada)
                    print(lista_modificada)
                    #if lista == lista_modificada:
                    #    encontrado = True
                final_count = next(cuenta)
            sumatoria = sumatoria + final_count
            print('\n',sumatoria, ' iteraciones al momento.\n')
            if lista_modificada == lista:
                encontrado = True
                return sumatoria

#Función que encuentra una lista compartida entre listas inicial y final modificada.
def busquedaBidireccional(lista,lista_modificada):
    lista_orig = lista
    lista_orig_mod = lista_modificada
    encontrado = False
    final_count_lista = 0
    final_count_mod = 0
    sumatoria_lista = 0
    sumatoria_mod = 0
    while not encontrado:
        print("Buscando desde lista inicial: ")
        cuenta_lista = contador()
        for i in lista:
            mov = random.randint(1,4)
            N = nodoNulo(lista)
            if mov == 1:
                lista = moverArriba(N,lista)
                print(lista_modificada)
            elif mov == 2:
                lista = moverAbajo(N,lista)
                print(lista)
            elif mov == 3:
                lista = moverIzquierda(N,lista)
                print(lista)
            elif mov == 4:
                lista = moverDerecha(N,lista)
                print(lista)
                #if lista == lista_modificada:
                #    encontrado = True
            final_count_lista = next(cuenta_lista)
        sumatoria_lista = sumatoria_lista + final_count_lista

        print("Buscando desde lista modificada: ")
        cuenta_mod = contador()
        for i in lista_modificada:
            mov = random.randint(1,4)
            N = nodoNulo(lista_modificada)
            if mov == 1:
                lista_modificada = moverArriba(N,lista_modificada)
                print(lista_modificada)
            elif mov == 2:
                lista_modificada = moverAbajo(N,lista_modificada)
                print(lista_modificada)
            elif mov == 3:
                lista_modificada = moverIzquierda(N,lista_modificada)
                print(lista_modificada)
            elif mov == 4:
                lista_modificada = moverDerecha(N,lista_modificada)
                print(lista_modificada)
                    #if lista == lista_modificada:
                    #    encontrado = True
            final_count_mod = next(cuenta_mod)
        sumatoria_mod = sumatoria_mod + final_count_mod
        if lista_modificada == lista:
            print('Lista modificada: \n')
            print(lista_orig_mod)
            print('\n')
            print('Lista provienente de lista modificada: ',lista_modificada)
            print('\n')
            print('\n',sumatoria_mod, ' iteraciones desde la lista modificada.')
            print('\n')
            print('Lista inicial: \n')
            print(lista_orig)
            print('\n')
            print('Lista provienente de lista inicial: ',lista)
            print('\n')
            print('\n',sumatoria_lista, ' iteraciones desde la lista inicial.')
            encontrado = True

#Función Salir
def salir():
    print('Has elegido la opcion salir')

#Función que toma valores correctos.
def seleccion():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("\n Selecciona una opción: "))
            correcto=True
        except ValueError:
            print('Opción incorrecta, vuelva a intentarlo. ')
    return num

#Función de selección de opciones.
def menuPrincipal():
    salir = False
    opcion = 0

    print ("\n Cargar valores al Puzzle 8 \n")
    lista = []
    lista_modificada = []
    for x in range(9):
        valor=int(input("Ingresar un valor entero entre 0-8:"))
        lista.append(valor)
    print('\n La lista ingresada es:  \n')
    print(lista)
    print('\n')

    while not salir:
        print ("1. Mezcla de valores.")
        print ("2. Búsqueda en anchura.")
        print ("3. Búsqueda bidireccional.")
        print ("4. Salir")

        opcion = seleccion()

        if opcion == 1:
            print("\n A continuación, se procederá con la mezcla al azar de valores. Por favor, espere. \n")
            lista_modificada = listaRandom(lista)
            print('\n Lista final iterada 50 veces: \n')
            print(lista_modificada)
            #break
        elif opcion == 2:
            contador = busquedaAnchura(lista,lista_modificada)
            print('\n')
            print('Se requirieron ', contador, ' movimientos validos.\n')
        elif opcion == 3:
            busquedaBidireccional(lista,lista_modificada)
        elif opcion == 4:
            salir = True
        else:
            print ("Introduce un numero entre 1 y 4")

        print ("\n Fin \n")


if __name__ == '__main__':
    menuPrincipal()
