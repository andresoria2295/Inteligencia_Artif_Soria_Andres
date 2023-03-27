#!/usr/bin/python3
#coding=utf-8
import copy
import random
from math import exp


def tablaXOR():
    booleano = [0,1]
    resultado = int
    listaXOR = []

    print('Tabla de la verdad XOR: \n')
    print('a \t b \t salida \n')
    for X in booleano:
        for Y in booleano:
            resultado = int((X and not Y) or (not X and Y))
            #res = int(resultado)
            listaXOR.append(resultado)
            print('{} \t {} \t {}'.format(X,Y,resultado))
    print('\n')
    #listaXOR.reverse()
    return listaXOR


def pesoSinaptico():
    lista_peso = []

    while True:
        try:
            print('Ingresar pesos sinápticos entre -1 y 1 para los perceptrones:\n')
            for p in range(19):
                valor=float(input('Ingresar valor de peso sináptico: '))
                if valor >= -1 and valor <= 1:
                    lista_peso.append(valor)
                else:
                    print("Valor ingresado incorrecto. Intente nuevamente.\n")
            return lista_peso

        except ValueError:
            print("Valores ingresados incorrectos.\n")
            continue
        else:
            break


def fcBuffer():
    factoresX = [0,0,0,1,1,0,1,1]
    doble = []
    for i in range(0, len(factoresX), 2):
        doble.append(factoresX[i:i+2])

    factores = [0,0]
    return factores


def neurona1(peso_sinaptico):
    terna_pesos = []
    factores = fcBuffer()
    a = factores[0]
    b = factores[1]
    for i in range(0, len(peso_sinaptico), 3):
        terna_pesos.append(peso_sinaptico[i:i+3])
    print('\t Pesos sinápticos de neurona 1: \n')
    print(terna_pesos[0])
    #print('\n')

    w0 = terna_pesos[0][0]
    w1 = terna_pesos[0][1]
    w2 = terna_pesos[0][2]

    sr = calculo(w0,w1,w2,a,b)
    print('Salida real de neurona 1:',sr)
    print('\n')
    return sr


def neurona2(peso_sinaptico):
    terna_pesos = []
    factores = fcBuffer()
    a = factores[0]
    b = factores[1]

    for i in range(0, len(peso_sinaptico), 3):
        terna_pesos.append(peso_sinaptico[i:i+3])
    print('\t Pesos sinápticos de neurona 2: \n')
    print(terna_pesos[1])
    #print('\n')

    w3 = terna_pesos[1][0]
    w4 = terna_pesos[1][1]
    w5 = terna_pesos[1][2]

    sr = calculo(w3,w4,w5,a,b)
    print('Salida real de neurona 2:',sr)
    print('\n')
    return sr


def neurona3(peso_sinaptico,sr1,sr2):
    terna_pesos = []

    for i in range(0, len(peso_sinaptico), 3):
        terna_pesos.append(peso_sinaptico[i:i+3])
    print('\t Pesos sinápticos de neurona 3: \n')
    print(terna_pesos[2])
    #print('\n')

    w6 = terna_pesos[2][0]
    w7 = terna_pesos[2][1]
    w8 = terna_pesos[2][2]

    sr = calculo(w6,w7,w8,sr1,sr2)
    print('Salida real de neurona 3:',sr)
    print('\n')
    return sr


def neurona4(peso_sinaptico,sr1,sr2):
    terna_pesos = []

    for i in range(0, len(peso_sinaptico), 3):
        terna_pesos.append(peso_sinaptico[i:i+3])
    print('\t Pesos sinápticos de neurona 4: \n')
    print(terna_pesos[3])
    #print('\n')

    w9 = terna_pesos[3][0]
    w10 = terna_pesos[3][1]
    w11 = terna_pesos[3][2]

    sr = calculo(w9,w10,w11,sr1,sr2)
    print('Salida real de neurona 4',sr)
    print('\n')
    return sr


def neurona5(peso_sinaptico,sr1,sr2):
    terna_pesos = []

    for i in range(0, len(peso_sinaptico), 3):
        terna_pesos.append(peso_sinaptico[i:i+3])
    print('\t Pesos sinápticos de neurona 5: \n')
    print(terna_pesos[4])
    #print('\n')

    w12 = terna_pesos[4][0]
    w13 = terna_pesos[4][1]
    w14 = terna_pesos[4][2]

    sr = calculo(w12,w13,w14,sr1,sr2)
    print('Salida real de neurona 5:',sr)
    print('\n')
    return sr


def neurona6(peso_sinaptico,sr1,sr2,sr3):
    #sr1 = neurona1(peso_sinaptico)
    #sr2 = neurona2(peso_sinaptico)
    terna_pesos = []

    for i in range(0, len(peso_sinaptico), 3):
        terna_pesos.append(peso_sinaptico[i:i+3])
    print('\t Pesos sinápticos de neurona 6: \n')
    print(terna_pesos[5])
    print(terna_pesos[6])
    #print('\n')

    w15 = terna_pesos[5][0]
    w16 = terna_pesos[5][1]
    w17 = terna_pesos[5][2]
    w18 = terna_pesos[6][0]

    sr = calculoFinal(w15,w16,w17,w18,sr1,sr2,sr3)
    print('Salida real de neurona 6:',sr)
    return sr


def calculo(wa,wb,wc,sra,srb):
    #if sra == 0 and srb == 0:
    sumatoriaX = wa*1 + wb*sra + wc*srb
    funcionY = 1/(1+exp(-sumatoriaX))
    return funcionY


def calculoFinal(wa,wb,wc,wd,sra,srb,src):
    #if sra == 0 and srb == 0:
    sumatoriaX = wa*1 + wb*sra + wc*srb + wd*src
    funcionY = 1/(1+exp(-sumatoriaX))
    return funcionY


def seleccion():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("\n Selecciona una opción: "))
            print('\n')
            correcto = True
        except ValueError:
            print('Opción incorrecta, vuelva a intentarlo. ')
    return num

def menuPrincipal():
    salir = False
    continuar = False
    opcion = 0
    op = 0
    listaOR = []
    listaAND = []
    listaXOR = []
    peso_sinaptico = []
    count = 0
    #FuncionFX = float

    print("\n Escoger el método de asignación de pesos sinápticos: \n")
    while not continuar:
        print ("1. Ingresar valores de pesos sinápticos por teclado.")
        print ("2. Pesos sináticos escogidos en forma aleatoria.")

        op = seleccion()

        if op == 1:
            peso_sinaptico = pesoSinaptico()
            print('\n Los pesos sinápticos iniciales son: \n')
            for w in peso_sinaptico:
                print('w',count,':',w)
                count = count + 1
            print('\n')

        elif op == 2:
            peso_sinaptico = [random.uniform(-1, 1) for x in range(19)]
            print('\n Los valores de pesos sinápticos formulados son:\n')
            for w in peso_sinaptico:
                print('w',peso_sinaptico.index(w),':',w)
            print('\n')

        continuar = True

    print("\n Seleccionar el comportamiento del perceptron: \n")
    while not salir:
        print ("1. Compuerta XOR.")
        print ("2. Compuerta AND.")
        print ("3. Compuerta OR.")
        print ("4. Salir")

        opcion = seleccion()

        if opcion == 1:
            listaXOR = tablaXOR()
            print('Valores de salida:',listaXOR)
            print('\n')
            #calculo(peso_sinaptico,listaXOR)
            n1 = neurona1(peso_sinaptico)
            n2 = neurona2(peso_sinaptico)
            n3 = neurona3(peso_sinaptico,n1,n2)
            n4 = neurona4(peso_sinaptico,n1,n2)
            n5 = neurona5(peso_sinaptico,n1,n2)
            n6 = neurona6(peso_sinaptico,n3,n4,n5)

        elif opcion == 2:
            print('listaAND')


        elif opcion == 3:
            print('listaOR')

        elif opcion == 4:
            salir = True
        else:

            print ("Introduce un numero entre 1 y 4")
        print ("\n Fin \n")


if __name__ == '__main__':
    menuPrincipal()
