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


def neurona1(peso_sinaptico,a,b):
    #factores = fcBuffer()
    #a = factores[0]
    #b = factores[1]
    print("soy a de n1",a)
    print("soy b de n1",b)
    print('\t Pesos sinápticos de neurona 1: \n')
    print(peso_sinaptico)
    #print('\n')
    w0 = peso_sinaptico[0]
    w1 = peso_sinaptico[1]
    w2 = peso_sinaptico[2]

    sr = calculo(w0,w1,w2,a,b)
    print('Salida real de neurona 1:',sr)
    print('\n')
    return sr


def neurona2(peso_sinaptico,a,b):
    print("soy a de n2",a)
    print("soy b de n2",b)
    print('\t Pesos sinápticos de neurona 2: \n')
    print(peso_sinaptico)
    #print('\n')
    w3 = peso_sinaptico[0]
    w4 = peso_sinaptico[1]
    w5 = peso_sinaptico[2]

    sr = calculo(w3,w4,w5,a,b)
    print('Salida real de neurona 2:',sr)
    print('\n')
    return sr


def neurona3(peso_sinaptico,a,b):
    print("soy a de n3",a)
    print("soy b de n3",b)
    print('\t Pesos sinápticos de neurona 3: \n')
    print(peso_sinaptico)
    #print('\n')
    w6 = peso_sinaptico[0]
    w7 = peso_sinaptico[1]
    w8 = peso_sinaptico[2]

    sr = calculo(w6,w7,w8,a,b)
    print('Salida real de neurona 3:',sr)
    print('\n')
    return sr


def neurona4(peso_sinaptico,peso_sinap,sr1,sr2,sr3):
    print('\t Pesos sinápticos de neurona 4: \n')
    print(peso_sinaptico)
    #print('\n')
    w9 = peso_sinaptico[0]
    w10 = peso_sinaptico[1]
    w11 = peso_sinaptico[2]
    w12 = peso_sinap[0]

    sr = calculoFinal(w9,w10,w11,w12,sr1,sr2,sr3)
    print('Salida real de neurona 4:',sr)
    print('\n')
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


def reglaDelta(peso_sinaptico,listaXOR):
    error = 0
    df = 0
    LR = 0.5 #probar con 0.5
    factores = fcBuffer()
    sd = 0
    x = 0
    inicio = 1
    e1 = 1
    e2 = 1
    e3 = 1
    e4 = 1
    listPesos = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
    listError = [[],[],[],[]]
    neu1 = []
    neu2 = []
    neu3 = []
    neu4 = []
    neu4extra = []

    print('\t Pesos sinápticos: \n')
    #print('\n')
    w0 = peso_sinaptico[0]
    w1 = peso_sinaptico[1]
    w2 = peso_sinaptico[2]
    w3 = peso_sinaptico[3]
    w4 = peso_sinaptico[4]
    w5 = peso_sinaptico[5]
    w6 = peso_sinaptico[6]
    w7 = peso_sinaptico[7]
    w8 = peso_sinaptico[8]
    w9 = peso_sinaptico[9]
    w10 = peso_sinaptico[10]
    w11 = peso_sinaptico[11]
    w12 = peso_sinaptico[12]
    #listW0 = []
    #listW1 = []
    #listW2 = []
    listPesos[0].append(w0)
    listPesos[1].append(w1)
    listPesos[2].append(w2)
    listPesos[3].append(w3)
    listPesos[4].append(w4)
    listPesos[5].append(w5)
    listPesos[6].append(w6)
    listPesos[7].append(w7)
    listPesos[8].append(w8)
    listPesos[9].append(w9)
    listPesos[10].append(w10)
    listPesos[11].append(w11)
    listPesos[12].append(w12)

    neu1.append(w0)
    neu1.append(w1)
    neu1.append(w2)
    neu2.append(w3)
    neu2.append(w4)
    neu2.append(w5)
    neu3.append(w6)
    neu3.append(w7)
    neu3.append(w8)
    neu4.append(w9)
    neu4.append(w10)
    neu4.append(w11)
    neu4extra.append(w12)
    sr1=0
    sr2=0
    sr3=0
    sr4=0
    #terna = fcParticion(peso_sinaptico)

    for i in range(1):
        #cuenta = contador()
        for sd in listaXOR:
            print(sd)
            ent1 = factores[x][0]
            ent2 = factores[x][1]
            x = x+1

            if sd == 0:
                if(inicio == 1):
                    sr1 = neurona1(neu1,ent1,ent2)
                    sr2 = neurona2(neu2,ent1,ent2)
                    sr3 = neurona3(neu3,ent1,ent2)
                    sr4 = neurona4(neu4,neu4extra,sr1,sr2,sr3)
                    inicio = 0
                    neu1.clear()
                    neu2.clear()
                    neu3.clear()
                    neu4.clear()
                    neu4extra.clear()

                    sr = sr4
                    error = sd - sr
                    print('Error de sd 0: ',error)
                    df = sr*(1-sr)*error
                    print('Delta final de sd 0: ',df)

                    deltaW9 = LR*1*df
                    deltaW10 = LR*sr1*df
                    deltaW11 = LR*sr2*df
                    deltaW12 = LR*sr3*df
                    w9 = deltaW9 + w9
                    neu4.append(w9)
                    listPesos[9].append(w9)
                    print('soy w9',w9)
                    w10 = deltaW10 + w10
                    neu4.append(w10)
                    listPesos[10].append(w10)
                    print('soy w10',w10)
                    w11 = deltaW11 + w11
                    neu4.append(w11)
                    listPesos[11].append(w11)
                    print('soy w11',w11)
                    w12 = deltaW12 + w12
                    neu4extra.append(w12)
                    listPesos[12].append(w12)
                    print('soy w12',w12)

                    Doc1 = sr1*(1-sr1)*df
                    #print(Doc1)
                    deltaW0 = LR*1*Doc1
                    deltaW1 = LR*ent1*Doc1
                    deltaW2 = LR*ent2*Doc1
                    w0 = deltaW0 + w0
                    neu1.append(w0)
                    listPesos[0].append(w0)
                    print('soy w0',w0)
                    w1 = deltaW1 + w1
                    neu1.append(w1)
                    listPesos[1].append(w1)
                    print('soy w1',w1)
                    w2 = deltaW2 + w2
                    neu1.append(w2)
                    listPesos[2].append(w2)
                    print('soy w2',w2)
                    sr1 = neurona1(neu1,ent1,ent2)

                    Doc2 = sr2*(1-sr2)*df
                    #print(Doc2)
                    deltaW3 = LR*1*Doc2
                    deltaW4 = LR*ent1*Doc2
                    deltaW5 = LR*ent2*Doc2
                    w3 = deltaW3 + w3
                    neu2.append(w3)
                    listPesos[3].append(w3)
                    print('soy w3',w3)
                    w4 = deltaW4 + w4
                    neu2.append(w4)
                    listPesos[4].append(w4)
                    print('soy w4',w4)
                    w5 = deltaW5 + w5
                    neu2.append(w5)
                    listPesos[5].append(w5)
                    print('soy w5',w5)
                    sr2 = neurona2(neu2,ent1,ent2)

                    Doc3 = sr3*(1-sr3)*df
                    #print(Doc3)
                    deltaW6 = LR*1*Doc3
                    deltaW7 = LR*ent1*Doc3
                    deltaW8 = LR*ent2*Doc3
                    w6 = deltaW6 + w6
                    neu3.append(w6)
                    listPesos[6].append(w6)
                    print('soy w6',w6)
                    w7 = deltaW7 + w7
                    neu3.append(w7)
                    listPesos[7].append(w7)
                    print('soy w7',w7)
                    w8 = deltaW8 + w8
                    neu3.append(w8)
                    listPesos[8].append(w8)
                    print('soy w8',w8)
                    sr3 = neurona3(neu3,ent1,ent2)
                    print(sr1)
                    print(sr2)
                    print(sr3)
                    sr4 = neurona4(neu4,neu4extra,sr1,sr2,sr3)

                    e1 = error
                    listError[0].append(e1)
                    neu1.clear()
                    neu2.clear()
                    neu3.clear()
                    neu4.clear()
                    neu4extra.clear()
                else:
                    sr = sr4
                    error = sd - sr
                    print('Error de sd 0: ',error)
                    df = sr*(1-sr)*error
                    print('Delta final de sd 0: ',df)

                    deltaW9 = LR*1*df
                    deltaW10 = LR*sr1*df
                    deltaW11 = LR*sr2*df
                    deltaW12 = LR*sr3*df
                    w9 = deltaW9 + w9
                    neu4.append(w9)
                    listPesos[9].append(w9)
                    print('soy w9',w9)
                    w10 = deltaW10 + w10
                    neu4.append(w10)
                    listPesos[10].append(w10)
                    print('soy w10',w10)
                    w11 = deltaW11 + w11
                    neu4.append(w11)
                    listPesos[11].append(w11)
                    print('soy w11',w11)
                    w12 = deltaW12 + w12
                    neu4extra.append(w12)
                    listPesos[12].append(w12)
                    print('soy w12',w12)

                    Doc1 = sr1*(1-sr1)*df
                    #print(Doc1)
                    deltaW0 = LR*1*Doc1
                    deltaW1 = LR*ent1*Doc1
                    deltaW2 = LR*ent2*Doc1
                    w0 = deltaW0 + w0
                    neu1.append(w0)
                    listPesos[0].append(w0)
                    print('soy w0',w0)
                    w1 = deltaW1 + w1
                    neu1.append(w1)
                    listPesos[1].append(w1)
                    print('soy w1',w1)
                    w2 = deltaW2 + w2
                    neu1.append(w2)
                    listPesos[2].append(w2)
                    print('soy w2',w2)
                    sr1 = neurona1(neu1,ent1,ent2)

                    Doc2 = sr2*(1-sr2)*df
                    #print(Doc2)
                    deltaW3 = LR*1*Doc2
                    deltaW4 = LR*ent1*Doc2
                    deltaW5 = LR*ent2*Doc2
                    w3 = deltaW3 + w3
                    neu2.append(w3)
                    listPesos[3].append(w3)
                    print('soy w3',w3)
                    w4 = deltaW4 + w4
                    neu2.append(w4)
                    listPesos[4].append(w4)
                    print('soy w4',w4)
                    w5 = deltaW5 + w5
                    neu2.append(w5)
                    listPesos[5].append(w5)
                    print('soy w5',w5)
                    sr2 = neurona2(neu2,ent1,ent2)

                    Doc3 = sr3*(1-sr3)*df
                    #print(Doc3)
                    deltaW6 = LR*1*Doc3
                    deltaW7 = LR*ent1*Doc3
                    deltaW8 = LR*ent2*Doc3
                    w6 = deltaW6 + w6
                    neu3.append(w6)
                    listPesos[6].append(w6)
                    print('soy w6',w6)
                    w7 = deltaW7 + w7
                    neu3.append(w7)
                    listPesos[7].append(w7)
                    print('soy w7',w7)
                    w8 = deltaW8 + w8
                    neu3.append(w8)
                    listPesos[8].append(w8)
                    print('soy w8',w8)
                    sr3 = neurona3(neu3,ent1,ent2)

                    sr4 = neurona4(neu4,neu4extra,sr1,sr2,sr3)

                    if(ent1 == 0 and ent2 == 0):
                        e1 = error
                        listError[0].append(e1)
                    elif(ent1 == 1 and ent2 == 1):
                        e4 = error
                        listError[3].append(e4)

                    neu1.clear()
                    neu2.clear()
                    neu3.clear()
                    neu4.clear()
                    neu4extra.clear()

            elif sd == 1:
                sr = sr4
                print("sr:", sr)
                print(sr4)
                error = sd - sr
                print('Error de sd 1: ',error)
                df = sr*(1-sr)*error
                #df=0.14352998456774063
                print('Delta final de sd 1: ',df)

                deltaW9 = LR*1*df
                deltaW10 = LR*sr1*df
                deltaW11 = LR*sr2*df
                deltaW12 = LR*sr3*df
                w9 = deltaW9 + w9
                neu4.append(w9)
                listPesos[9].append(w9)
                print('soy w9',w9)
                w10 = deltaW10 + w10
                neu4.append(w10)
                listPesos[10].append(w10)
                print('soy w10',w10)
                w11 = deltaW11 + w11
                neu4.append(w11)
                listPesos[11].append(w11)
                print('soy w11',w11)
                w12 = deltaW12 + w12
                neu4extra.append(w12)
                listPesos[12].append(w12)
                print('soy w12',w12)

                Doc1 = sr1*(1-sr1)*df
                #print(Doc1)
                deltaW0 = LR*1*df
                deltaW1 = LR*ent1*df
                deltaW2 = LR*ent2*df
                w0 = deltaW0 + w0
                neu1.append(w0)
                listPesos[0].append(w0)
                print('soy w0',w0)
                w1 = deltaW1 + w1
                neu1.append(w1)
                listPesos[1].append(w1)
                print('soy w1',w1)
                w2 = deltaW2 + w2
                neu1.append(w2)
                listPesos[2].append(w2)
                print('soy w2',w2)
                sr1 = neurona1(neu1,ent1,ent2)

                Doc2 = sr2*(1-sr2)*df
                #print(Doc2)
                deltaW3 = LR*1*df
                deltaW4 = LR*ent1*df
                deltaW5 = LR*ent2*df
                w3 = deltaW3 + w3
                neu2.append(w3)
                listPesos[3].append(w3)
                print('soy w3',w3)
                w4 = deltaW4 + w4
                neu2.append(w4)
                listPesos[4].append(w4)
                print('soy w4',w4)
                w5 = deltaW5 + w5
                neu2.append(w5)
                listPesos[5].append(w5)
                print('soy w5',w5)
                sr2 = neurona2(neu2,ent1,ent2)

                Doc3 = sr3*(1-sr3)*df
                #print(Doc3)
                deltaW6 = LR*1*df
                deltaW7 = LR*ent1*df
                deltaW8 = LR*ent2*df
                w6 = deltaW6 + w6
                neu3.append(w6)
                listPesos[6].append(w6)
                print('soy w6',w6)
                w7 = deltaW7 + w7
                neu3.append(w7)
                listPesos[7].append(w7)
                print('soy w7',w7)
                w8 = deltaW8 + w8
                neu3.append(w8)
                listPesos[8].append(w8)
                print('soy w8',w8)
                sr3 = neurona3(neu3,ent1,ent2)

                sr4 = neurona4(neu4,neu4extra,sr1,sr2,sr3)

                if(ent1 == 0 and ent2 == 1):
                    e2 = error
                    listError[1].append(e2)
                elif(ent1 == 1 and ent2 == 0):
                    e3 = error
                    listError[2].append(e3)

                neu1.clear()
                neu2.clear()
                neu3.clear()
                neu4.clear()
                neu4extra.clear()
        x = 0
    print('Error e1',e1)
    print('Error e2',e2)
    print('Error e3',e3)
    print('Error e4',e4)
    print('\n')
    grafico(listPesos,listError)


#Función que grafica errores y pesos sinápticos.
def grafico(listPesos,listError):
    #listError,listW0,listW1,listW2
    figure = graph.figure()
    figure.set_size_inches(30,30)
    #figure.suptitle('w0 = azul  -  w1 = verde  -  w2 = amarillo - w3 = naranja - w4 = lila \n - w5 = cyan - w6 = magenta - w7 = marrón - w8 = gris - w9 = rosado \n - w10 = violeta - w11 = aqua - w12 = negro', fontsize = 14)
    graph.subplot(1,2,1)
    graph.plot(listPesos[0], 'b')
    graph.plot(listPesos[1], 'g')
    graph.plot(listPesos[2], 'y')
    graph.plot(listPesos[3], 'o')
    graph.plot(listPesos[4], 'p')
    graph.plot(listPesos[5], 'c')
    graph.plot(listPesos[6], 'm')
    graph.plot(listPesos[7], 'brown')
    graph.plot(listPesos[8], 'grey')
    graph.plot(listPesos[9], 'pink')
    graph.plot(listPesos[10], 'violet')
    graph.plot(listPesos[11], '#04D8B2')
    graph.plot(listPesos[12], 'k')
    graph.legend()

    graph.subplot(1,2,2)
    figure.suptitle('Errores', fontsize = 14)
    graph.plot(listError[0], 'r')
    graph.plot(listError[1], 'o')
    graph.plot(listError[2], 'b')
    graph.plot(listError[3], 'y')
    #graph.plot(listError[0], color="r", linewidth=2.5, linestyle="-", label="error 1")
    #graph.plot(listError[1], color="o",  linewidth=2.5, linestyle="-", label="error 2")
    graph.legend()
    graph.show()

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
    ent1 = 0
    ent2 = 0
    listaOR = []
    listaAND = []
    listaXOR = []
    peso_sinaptico = []
    nuevos_pesos = []
    terna = []
    count = 0
    #FuncionFX = float

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
            print('\n Los valores de pesos sinápticos formulados son:\n')
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
            print('\n')
            #terna = fcParticion(peso_sinaptico)
            #fcBuffer()
            #calculo(peso_sinaptico,listaXOR)
            #n1 = neurona1(terna[0],ent1,ent2)
            #n2 = neurona2(terna[1],ent1,ent2)
            #n3 = neurona3(terna[2],ent1,ent2)
            #n4 = neurona4(terna[3],terna[4],n1,n2,n3)
            reglaDelta(peso_sinaptico,listaXOR)

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
