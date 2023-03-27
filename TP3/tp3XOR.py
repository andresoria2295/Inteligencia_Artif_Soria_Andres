#!/usr/bin/python3
#coding=utf-8
import copy
import random
from math import exp
import matplotlib.pyplot as graph
graph.style.use('ggplot')


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
            for p in range(13):
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
    factores = []
    for i in range(0, len(factoresX), 2):
        factores.append(factoresX[i:i+2])
    #factores = [0,0]
    return factores


def fcParticion(peso_sinaptico):
    terna_pesos = []
    #lista_pesos = []
    for i in range(0, len(peso_sinaptico), 3):
        terna_pesos.append(peso_sinaptico[i:i+3])
    return(terna_pesos)


#Función que cuenta elementos.
def contador():
  numero = 0
  while True:
    numero += 1
    yield numero


def MuestraSR(salReales):
    count = 0
    print('\n Salidas reales:\n')
    for s in salReales:
        #print('sr',salReales.index(s),':',s)
        print('Salida real Nuerona',count+1,':',s)
        count = count + 1
    return


def MuestraPesos(ternaPesos,ternaFinal):
    count = 0
    ternaPesos.extend(ternaFinal)
    ternaPesos = fcParticion(ternaPesos)
    print('\t \tNeurona 1\n')
    #for i in range nro_neurona:
    for w in ternaPesos[0]:
        #print('sr',salReales.index(s),':',s)
        print('\t w',count,':',w)
        count = count + 1
    print('\n')
    print('\t \tNeurona 2\n')
    for w in ternaPesos[1]:
        #print('sr',salReales.index(s),':',s)
        print('\t w',count,':',w)
        count = count + 1
    print('\n')
    print('\t \tNeurona 3\n')
    for w in ternaPesos[2]:
        #print('sr',salReales.index(s),':',s)
        print('\t w',count,':',w)
        count = count + 1
    print('\n')
    print('\t \tNeurona 4\n')
    for w in ternaPesos[3]:
        #print('sr',salReales.index(s),':',s)
        print('\t w',count,':',w)
        count = count + 1
    for w in ternaPesos[4]:
        #print('sr',salReales.index(s),':',s)
        print('\t w',count,':',w)
        count = count + 1
    return


def neuronaOculta(peso_sinaptico):
    terna_pesos = []
    terna_inicial = []
    terna_final = []
    salReales = []
    recepcion = [[],[]]
    listError = [[],[],[],[]]
    listPesos = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
    dataInicial = 1
    x = 0
    fila = 1
    it = 1
    final_count = 0
    sumatoria = 0
    terna_pesos = fcParticion(peso_sinaptico)
    entradas = fcBuffer()

    #Toma de a 3 pesos repetidos el nro de neruona. Lo sobrante es para neurona final.
    for i in range (10001):
        ent1 = entradas[x][0]
        ent2 = entradas[x][1]
        x = x+1
        cuenta = contador()
        #print('Entrada 1: ',ent1)
        #print('Entrada 2:',ent2)
        if (dataInicial == 1):
            #terna_inicial = peso_sinaptico[:(nro_neurona*3)]
            terna_inicial = peso_sinaptico[:(3*3)]
            #terna_final = peso_sinaptico[-(nro_neurona+1):]
            terna_final = peso_sinaptico[-(4):]
            #print("\nPesos y salidas iniciales\n")
            #MuestraPesos(terna_inicial,terna_final,nro_neurona)
            print('\n')
            MuestraPesos(terna_inicial,terna_final)
            print('\n')
            print('\n ---------- Iteración',it, '----------')
            it = it + 1
            print("\n Fila",fila)
            fila = fila + 1

        dataInicial = 0
        print('\nEntrada 1: ',ent1)
        print('\nEntrada 2: ',ent2)

        #for i in range (nro_neurona):
        for i in range (3):
            sr = calculo(terna_pesos[i],ent1,ent2)
            salReales.append(sr)
        MuestraSR(salReales)
        #terna_final = peso_sinaptico[-(nro_neurona+1):]
        srf = calculoFinal(terna_final,salReales)
        print("Salida real neurona final :",srf)
        print('\n Actualización de pesos sinápticos: \n')

        #print(terna_pesos)
        #print(terna_final)

        #recepcion = reglaDeltaFinal(ent1,ent2,nro_neurona,terna_pesos,terna_final,salReales,srf,sumatoria,listError,listPesos)
        recepcion = reglaDeltaFinal(ent1,ent2,terna_pesos,terna_final,salReales,srf,sumatoria,listError,listPesos)
        print('\n')

        if(fila == 1):
            print('\n ---------- Iteración',it, '----------')
            it = it + 1

        print("\n Fila",fila)
        fila = fila + 1
        #print('\n')
        #MuestraSR(salReales)
        #print('\n')
        #print("sr 4: ",srf)
        salReales.clear()
        terna_pesos.clear()
        terna_final.clear()

        listaRecibida = recepcion[0]
        terna_pesos = fcParticion(listaRecibida)
        #print(terna_pesos)
        terna_final = recepcion[1]
        #print(terna_final)
        if (x == 4):
            x = 0
        if (fila == 5):
            fila = 1
        final_count = next(cuenta)
        sumatoria = sumatoria + final_count


def calculo(terna_pesos,ent1,ent2):
    #if sra == 0 and srb == 0:
    wa = terna_pesos[0]
    wb = terna_pesos[1]
    wc = terna_pesos[2]
    sumatoriaX = wa*1 + wb*ent1 + wc*ent2
    funcionY = 1/(1+exp(-sumatoriaX))
    return funcionY


def calculoFinal(terna_final,salReales):
    #if sra == 0 and srb == 0:
    wa = terna_final[0]
    wb = terna_final[1]
    wc = terna_final[2]
    wd = terna_final[3]
    sumatoriaX = wa*1 + wb*salReales[0] + wc*salReales[1] + wd*salReales[2]
    funcionY = 1/(1+exp(-sumatoriaX))
    return funcionY


def contadorError(listError,error,ent1,ent2,sd):
    if((ent1 == 0 and ent2 == 0) and (sd == 0)):
        listError[0].append(error)
    elif((ent1 == 0 and ent2 == 1) and (sd == 1)):
        listError[1].append(error)
    elif((ent1 == 1 and ent2 == 0) and (sd == 1)):
        listError[2].append(error)
    elif((ent1 == 1 and ent2 == 1) and (sd == 0)):
        listError[3].append(error)

    return listError


def contadorPeso(listPesos,pesosGuardados):
    concatenacion = pesosGuardados[0] + pesosGuardados[1]
    for i in range (13):
        listPesos[i].append(concatenacion[i])
    return listPesos


def grafico(listError,listPesos):
    figure = graph.figure()
    figure.set_size_inches(30,30)
    graph.subplot(1,2,1)
    graph.xlabel('Iteraciones')
    for numPeso in range (len(listPesos)):
        graph.plot(listPesos[numPeso], label='w'+str(numPeso))
    graph.legend()
    graph.title("Pesos sinápticos")
    graph.subplot(1,2,2)
    graph.xlabel('Iteraciones')
    #figure.suptitle('Errores', fontsize = 14)
    graph.plot(listError[0], label='Error 1')
    graph.plot(listError[1], label='Error 2')
    graph.plot(listError[2], label='Error 3')
    graph.plot(listError[3], label='Error 4')
    #graph.plot(listError[0], color="r", linewidth=2.5, linestyle="-", label="error 1")
    #graph.plot(listError[1], color="o",  linewidth=2.5, linestyle="-", label="error 2")
    graph.legend()
    graph.title("Errores")
    graph.show()


def reglaDeltaFinal(ent1,ent2,terna_pesos,terna_final,salReales,srf,sumatoria,listError,listPesos):
    LR = 0.5
    nuevaTernaFinal = []
    nuevaTernaPesos = []
    deltaOculto = []
    listaGuardado = []

    if((ent1 == 0 and ent2 == 0) or (ent1 == 1 and ent2 == 1)):
        sd = 0
    elif ((ent1 == 0 and ent2 == 1) or (ent1 == 1 and ent2 == 0)):
        sd = 1
    #print("SOY SD",sd)
    #print(ent1)
    #print(ent2)
    error = sd - srf
    df = srf*(1-srf)*error

    listadoError = contadorError(listError,error,ent1,ent2,sd)

    deltaWbias = LR*1*df #seria como el w9 en 3 neuronas
    nuevoWbias = terna_final[0] + deltaWbias
    nuevaTernaFinal.append(nuevoWbias)
    #for i in range (nro_neurona):
    for i in range (3):
        #saca w10,w11,w12
        deltaW = LR*salReales[i]*df
        nuevoW = terna_final[i+1] + deltaW
        nuevaTernaFinal.append(nuevoW)
    #print(nuevaTernaFinal)

    for i in range (3):
        #Doc1 = sr1*(1-sr1)*df, luego con sr2 Doc2, sr3 Doc3
        deltaOc = salReales[i]*(1-salReales[i])*df
        deltaOculto.append(deltaOc)

    for i in range (3):
        deltaWbiasOc = LR*1*deltaOculto[i]
        nuevoWbiasOc = terna_pesos[i][0] + deltaWbiasOc
        nuevaTernaPesos.append(nuevoWbiasOc)
        deltaWOc1 = LR*ent1*deltaOculto[i]
        deltaWOc2 = LR*ent2*deltaOculto[i]
        nuevoWoc1 = terna_pesos[i][1] + deltaWOc1
        nuevoWoc2 = terna_pesos[i][2] + deltaWOc2
        nuevaTernaPesos.append(nuevoWoc1)
        nuevaTernaPesos.append(nuevoWoc2)
    #print(nuevaTernaPesos)
    MuestraPesos(nuevaTernaPesos,nuevaTernaFinal)
    listaGuardado.append(nuevaTernaPesos)
    listaGuardado.append(nuevaTernaFinal)
    listadoPesos = contadorPeso(listPesos,listaGuardado)

    if (sumatoria == 10000):
        #listadoError = contadorError(error,ent1,ent2,sd)
        grafico(listadoError,listadoPesos)
        #print(listadoError)
        #grafico(listadoError)
    return listaGuardado


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
    nuevos_pesos = []
    terna = []
    count = 0

    print("\n Escoger el método de asignación de pesos sinápticos: \n")
    while not continuar:
        print ("1. Ingresar valores de pesos sinápticos por teclado.")
        print ("2. Pesos sináticos escogidos en forma aleatoria.")
        print ("3. Emplear pesos sinátipticos predeterminados.")

        op = seleccion()

        if op == 1:
            peso_sinaptico = pesoSinaptico()
            print('\n Los pesos sinápticos iniciales son: \n')
            for w in peso_sinaptico:
                print('w',count,':',w)
                count = count + 1
            print('\n')

        elif op == 2:
            peso_sinaptico = [random.uniform(-1, 1) for x in range(13)]
            print('Los valores de pesos sinápticos formulados son:\n')
            for w in peso_sinaptico:
                print('w',peso_sinaptico.index(w),':',w)
            print('\n')

        elif op == 3:
            peso_sinaptico = [0.9,0.7,0.5,0.3,-0.9,-1,0.8,0.35,0.1,-0.23,-0.79,0.56,0.6]
            print('\n Los valores de pesos sinápticos predeterminados son:\n')
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
            neuronaOculta(peso_sinaptico)

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
