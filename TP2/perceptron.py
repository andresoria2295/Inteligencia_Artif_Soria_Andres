#!/usr/bin/python3
#coding=utf-8
import copy
import random
from math import exp
import matplotlib.pyplot as graph


def tablaOR():
    booleano = [0,1]
    resultado = int
    listaOR = []

    print('Tabla de la verdad OR: \n')
    print('a \t b \t salida \n')
    for X in booleano:
        for Y in booleano:
            resultado = format(X or Y)
            listaOR.append(int(resultado))
            print('{} \t {} \t {}'.format(X,Y,X or Y))
    print('\n')
    #listaOR.reverse()
    return listaOR


def tablaAND():
    booleano = [0,1]
    resultado = int
    listaAND = []

    print('Tabla de la verdad AND: \n')
    print('a \t b \t salida \n')
    for X in booleano:
        for Y in booleano:
            resultado = format(X and Y)
            listaAND.append(int(resultado))
            print('{} \t {} \t {}'.format(X,Y,X and Y))
    print('\n')
    #listaAND.reverse()
    return listaAND


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


#Función que cuenta elementos.
def contador():
  numero = 0
  while True:
    numero += 1
    yield numero


#Función para ingresar valores por pantalla.
def pesoSinaptico():
    lista_peso = []

    while True:
        try:
            print('\n')
            for p in range(3):
                valor=float(input('Ingresar valores de pesos sinápticos para el perceptrón: '))
                lista_peso.append(valor)

            if((lista_peso[0] >= -1 and lista_peso[0] <= 1) and (lista_peso[1] >= -1 and lista_peso[1] <= 1) and (lista_peso[2] >= -1 and lista_peso[2] <= 1)):
                print('\n Los valores de pesos sinápticos ingresados son:\n')
                print('w1: ',lista_peso[0])
                print('w2: ',lista_peso[1])
                print('w0: ',lista_peso[2])
                return lista_peso

        except ValueError:
            print("Valores ingresados incorrectos.")
            continue
        else:
            break


#Función que devuelve salida real en búsqueda de la salida deseada.
def salidaDeseada(w1,w2,w0,a,b):
    #w1 = pesos[0]
    #w2 = pesos[1]
    #w0 = pesos[2]
    #booleano = [0,1]
    sumatoriaX = 0
    funcionY = 0
    #a = 0
    #b = 0

    #for a in booleano:
    #    for b in booleano:
    #sumatoriaX = w1*a + w2*b + w0*1
    #funcionY = 1/(1+exp(sumaX))
    #lista_funcionesFX.append(funcionY)
    #return lista_funcionesFX
    if a == 0 and b == 0:
        sumatoriaX = w1*a + w2*b + w0*1
        funcionY = 1/(1+exp(-sumatoriaX))
    elif a == 0 and b == 1:
        sumatoriaX = w1*a + w2*b + w0*1
        funcionY = 1/(1+exp(-sumatoriaX))
    elif a == 1 and b == 0:
        sumatoriaX = w1*a + w2*b + w0*1
        funcionY = 1/(1+exp(-sumatoriaX))
    elif a == 1 and b == 1:
        sumatoriaX = w1*a + w2*b + w0*1
        funcionY = 1/(1+exp(-sumatoriaX))
    print('Salida real: ',funcionY)
    return funcionY


#Función que calcula los nuevos pesos, nuevos errores y delta.
def reglaDelta(w1,w2,w0,lista):
    sd = 0
    LR = 0.1
    a = 0
    b = 0
    e1 = 1
    e2 = 1
    e3 = 1
    e4 = 1
    sr = salidaDeseada(w1,w2,w0,a,b)
    final_count = 0
    sumatoria = 0
    listError = []
    listPesos = [[],[],[]]
    #listW0 = []
    #listW1 = []
    #listW2 = []
    listPesos[0].append(w0)
    listPesos[1].append(w1)
    listPesos[2].append(w2)
    #for index, value in enumerate(list)

    #    while error >= 0.1:
    #       cuenta = contador()
    #for i in range(2):
    while True:
        cuenta = contador()
        for sd in lista:
            print(sd)
            if sd == 0:
                error = sd - sr
                print('Error de sd 0: ',error)
                delta = sr*(1-sr)*error
                print('Delta de sd 0: ',delta)

                if a == 0 and b == 0:
                    delw0 =LR*1*delta
                    w0 = w0 +delw0
                    #listW0.append(w0)
                    #listPesos.append(listW0)
                    listPesos[0].append(w0)
                    print('Nuevo w0 de 0,0',w0)

                    delw1 =LR*a*delta
                    w1 = w1 +delw1
                    #listW1.append(w1)
                    #listPesos.append(listW1)
                    listPesos[1].append(w1)
                    print('Nuevo w1 de 0,0',w1)

                    delw2 =LR*b*delta
                    w2 = w2 +delw2
                    #listW2.append(w2)
                    #listPesos.append(listW2)
                    listPesos[2].append(w2)
                    print('Nuevo w2 de 0,0',w2)
                    a = 0
                    b = 1
                    e1 = error
                    listError.append(e1)
                    sr = salidaDeseada(w1,w2,w0,a,b)

                elif a == 0 and b == 1:
                    delw0 =LR*1*delta
                    w0 = w0 +delw0
                    #listW0.append(w0)
                    #listPesos.append(listW0)
                    listPesos[0].append(w0)
                    print('Nuevo w0 de 0,1',w0)

                    delw1 =LR*a*delta
                    w1 = w1 +delw1
                    #listW1.append(w1)
                    #listPesos.append(listW1)
                    listPesos[1].append(w1)
                    print('Nuevo w1 de 0,1',w1)

                    delw2 =LR*b*delta
                    w2 = w2 +delw2
                    #listW2.append(w2)
                    #listPesos.append(listW2)
                    listPesos[2].append(w2)
                    print('Nuevo w2 de 0,1',w2)
                    a = 1
                    b = 0
                    e2 = error
                    listError.append(e2)
                    sr = salidaDeseada(w1,w2,w0,a,b)
                    #break

                elif a == 1 and b == 0:
                    delw0 =LR*1*delta
                    w0 = w0 +delw0
                    #listW0.append(w0)
                    #listPesos.append(listW0)
                    listPesos[0].append(w0)
                    print('Nuevo w0 de 1,0',w0)

                    delw1 =LR*a*delta
                    w1 = w1 +delw1
                    #listW1.append(w1)
                    #listPesos.append(listW1)
                    listPesos[1].append(w1)
                    print('Nuevo w1 de 1,0',w1)

                    delw2 =LR*b*delta
                    w2 = w2 +delw2
                    #listW2.append(w2)
                    #listPesos.append(listW2)
                    listPesos[2].append(w2)
                    print('Nuevo w2 de 1,0',w2)
                    a = 1
                    b = 1
                    e3 = error
                    listError.append(e3)
                    sr = salidaDeseada(w1,w2,w0,a,b)

                elif a == 1 and b == 1:
                    delw0 =LR*1*delta
                    w0 = w0 +delw0
                    #listW0.append(w0)
                    #listPesos.append(listW0)
                    listPesos[0].append(w0)
                    print('Nuevo w0 de 1,1',w0)

                    delw1 =LR*a*delta
                    w1 = w1 +delw1
                    #listW1.append(w1)
                    #listPesos.append(listW1)
                    listPesos[1].append(w1)
                    print('Nuevo w1 de 1,1',w1)

                    delw2 =LR*b*delta
                    w2 = w2 +delw2
                    #listW2.append(w2)
                    #listPesos.append(listW2)
                    listPesos[2].append(w2)
                    print('Nuevo w2 de 1,1',w2)
                    a = 0
                    b = 0
                    e4 = error
                    listError.append(e4)
                    sr = salidaDeseada(w1,w2,w0,a,b)

            elif sd == 1:
                error = sd - sr
                print('Error de sd 1: ',error)
                delta = sr*(1-sr)*error
                print('Delta de sd 1: ',delta)

                if a == 0 and b == 1:
                    delw0 =LR*1*delta
                    w0 = w0 +delw0
                    #listW0.append(w0)
                    #listPesos.append(listW0)
                    listPesos[0].append(w0)
                    print('Nuevo w0 de 0,1',w0)

                    delw1 =LR*a*delta
                    w1 = w1 +delw1
                    #listW1.append(w1)
                    #listPesos.append(listW1)
                    listPesos[1].append(w1)
                    print('Nuevo w1 de 0,1',w1)

                    delw2 =LR*b*delta
                    w2 = w2 +delw2
                    #listW2.append(w2)
                    #listPesos.append(listW2)
                    listPesos[2].append(w2)
                    print('Nuevo w2 de 0,1',w2)
                    a = 1
                    b = 0
                    e2 = error
                    listError.append(e2)
                    sr = salidaDeseada(w1,w2,w0,a,b)
                    #break

                elif a == 1 and b == 0:
                    delw0 =LR*1*delta
                    w0 = w0 +delw0
                    #listW0.append(w0)
                    #listPesos.append(listW0)
                    listPesos[0].append(w0)
                    print('Nuevo w0 de 1,0',w0)

                    delw1 =LR*a*delta
                    w1 = w1 +delw1
                    #listW1.append(w1)
                    #listPesos.append(listW1)
                    listPesos[1].append(w1)
                    print('Nuevo w1 de 1,0',w1)

                    delw2 =LR*b*delta
                    w2 = w2 +delw2
                    #listW2.append(w2)
                    #listPesos.append(listW2)
                    listPesos[2].append(w2)
                    print('Nuevo w2 de 1,0',w2)
                    a = 1
                    b = 1
                    e3 = error
                    listError.append(e3)
                    sr = salidaDeseada(w1,w2,w0,a,b)
                    #break

                elif a == 1 and b == 1:
                    delw0 =LR*1*delta
                    w0 = w0 +delw0
                    #listW0.append(w0)
                    #listPesos.append(listW0)
                    listPesos[0].append(w0)
                    print('Nuevo w0 de 1,1',w0)

                    delw1 =LR*a*delta
                    w1 = w1 +delw1
                    #listW1.append(w1)
                    #listPesos.append(listW1)
                    listPesos[1].append(w1)
                    print('Nuevo w1 de 1,1',w1)

                    delw2 =LR*b*delta
                    w2 = w2 +delw2
                    #listW2.append(w2)
                    #listPesos.append(listW2)
                    listPesos[2].append(w2)
                    print('Nuevo w2 de 1,1',w2)
                    a = 0
                    b = 0
                    e4 = error
                    listError.append(e4)
                    sr = salidaDeseada(w1,w2,w0,a,b)
        final_count = next(cuenta)
        sumatoria = sumatoria + final_count
        #listPesos.append(listW0)
        #listPesos.append(listW1)
        #listPesos.append(listW2)
        print('\n')
        print('\n Iteraciones al momento: ',sumatoria)
        print('Error e1',e1)
        print('Error e2',e2)
        print('Error e3',e3)
        print('Error e4',e4)
        print('\n')
        if ((abs(e1) <= 0.1) and (abs(e2) <= 0.1) and (abs(e3) <= 0.1) and (abs(e4) <= 0.1)):
            print('\n Numero de iteraciones total realizadas: ',sumatoria)
            #grafico(listError,listW0,listW1,listW2)
            grafico(listError,listPesos)
            return False


#Función que grafica errores y pesos sinápticos.
def grafico(listError,listPesos):
    #listError,listW0,listW1,listW2
    figure = graph.figure()
    figure.suptitle('error = rojo  -  w0 = azul  -  w1 = verde  -  w2 = amarillo', fontsize = 14)
    graph.plot(listError, 'r')
    graph.plot(listPesos[0], 'b')
    graph.plot(listPesos[1], 'g')
    graph.plot(listPesos[2], 'y')
    graph.show()


def seleccion():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("\n Selecciona una opción:"))
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
    #FuncionFX = float

    print("\n Escoger el método de asignación de pesos sinápticos: \n")
    while not continuar:
        print ("1. Ingresar valores de pesos sinápticos por teclado.")
        print ("2. Pesos sináticos escogidos en forma aleatoria.")

        op = seleccion()

        if op == 1:
            peso_sinaptico = pesoSinaptico()
            print('\n Los pesos sinápticos iniciales son: \n')
            print(peso_sinaptico)
            #print('\n')
            w1 = peso_sinaptico[0]
            w2 = peso_sinaptico[1]
            w0 = peso_sinaptico[2]

        elif op == 2:
            peso_sinaptico = [random.uniform(-1, 1) for x in range(3)]
            print('\n Los valores de pesos sinápticos ingresados son:\n')
            w1 = peso_sinaptico[0]
            w2 = peso_sinaptico[1]
            w0 = peso_sinaptico[2]
            print('w1: ',w1)
            print('w2: ',w2)
            print('w0: ',w0)
            print('\n Los pesos sinápticos iniciales son: \n')
            print(peso_sinaptico)
            #print('\n')

        #elif op == 3:
        continuar = True
        #else:

        #    print ("Introduce un numero entre 1 y 3")

    print("\n Seleccionar el comportamiento del perceptron: \n")
    while not salir:
        print ("1. Compuerta OR.")
        print ("2. Compuerta AND.")
        print ("3. Compuerta XOR.")
        print ("4. Salir")

        opcion = seleccion()

        if opcion == 1:
            listaOR = tablaOR()
            print(listaOR)
            print('\n')
            #peso_sinaptico = pesoSinaptico()
            #print('Los pesos sinápticos iniciales son: \n')
            #print(peso_sinaptico)
            #print('\n')
            #w1 = peso_sinaptico[0]
            #w2 = peso_sinaptico[1]
            #w0 = peso_sinaptico[2]
            #salidaDeseada(w1,w2,w0)
            #print(FuncionFX)
            reglaDelta(w1,w2,w0,listaOR)
            #break

        elif opcion == 2:
            listaAND = tablaAND()
            print(listaAND)
            print('\n')
            #peso_sinaptico = pesoSinaptico()
            #print('Los pesos sinápticos iniciales son: \n')
            #print(peso_sinaptico)
            #print('\n')
            #w1 = peso_sinaptico[0]
            #w2 = peso_sinaptico[1]
            #w0 = peso_sinaptico[2]
            reglaDelta(w1,w2,w0,listaAND)
            #break

        elif opcion == 3:
            listaXOR = tablaXOR()
            print(listaXOR)
            print('\n')
            #peso_sinaptico = pesoSinaptico()
            #print('Los pesos sinápticos iniciales son: \n')
            #print(peso_sinaptico)
            #print('\n')
            #w1 = peso_sinaptico[0]
            #w2 = peso_sinaptico[1]
            #w0 = peso_sinaptico[2]
            reglaDelta(w1,w2,w0,listaXOR)

        elif opcion == 4:
            salir = True
        else:

            print ("Introduce un numero entre 1 y 4")
        print ("\n Fin \n")


if __name__ == '__main__':
    menuPrincipal()
