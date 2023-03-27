import math
import os
import matplotlib.pyplot as plt
import yaml

plt.style.use('ggplot')


def establecerPrimeraNeurona(tipoNeurona):
    if tipoNeurona == "oculta":
        neuronaOculta = {
            1: {
                1: {"Fila": 1, "bias": 1, "entrada1": 0, "entrada2": 0, "salidaReal": "sin datos"},
                2: {"Fila": 2, "bias": 1, "entrada1": 0, "entrada2": 1, "salidaReal": "sin datos"},
                3: {"Fila": 3, "bias": 1, "entrada1": 1, "entrada2": 0, "salidaReal": "sin datos"},
                4: {"Fila": 4, "bias": 1, "entrada1": 1, "entrada2": 1, "salidaReal": "sin datos"},
                5: {"w": [], "totalPesos": [[], [], []]},
            }
        }
        return neuronaOculta
    if tipoNeurona == "salida":
        neuronaSalida = {
            1: {
                1: {"Fila": 1, "bias": 1, "salidaReal": "sin datos", "error": "sin datos", "errorBajo": False, "totalErrores": []},
                2: {"Fila": 2, "bias": 1, "salidaReal": "sin datos", "error": "sin datos", "errorBajo": False, "totalErrores": []},
                3: {"Fila": 3, "bias": 1, "salidaReal": "sin datos", "error": "sin datos", "errorBajo": False, "totalErrores": []},
                4: {"Fila": 4, "bias": 1, "salidaReal": "sin datos", "error": "sin datos", "errorBajo": False, "totalErrores": []},
                5: {"w": [], "totalPesos": []}
            }
        }
        return neuronaSalida


def agregarNeuronasOcultaDict(neuronaOcultaDict, cantidadNeuronasOculta):
    # Vacio el diccionario de neuronas de la capa oculta para asi agregar toda la cantidad ingresada porque sino voy a tener 1 demàs
    neuronaOcultaDict = {}
    for i in range(cantidadNeuronasOculta):
        neuronaOcultaDict[len(neuronaOcultaDict)+1] = {
            1: {"Fila": 1, "bias": 1, "entrada1": 0, "entrada2": 0, "salidaReal": "sin datos"},
            2: {"Fila": 2, "bias": 1, "entrada1": 0, "entrada2": 1, "salidaReal": "sin datos"},
            3: {"Fila": 3, "bias": 1, "entrada1": 1, "entrada2": 0, "salidaReal": "sin datos"},
            4: {"Fila": 4, "bias": 1, "entrada1": 1, "entrada2": 1, "salidaReal": "sin datos"},
            5: {"w": [], "totalPesos": [[], [], []]}
        }
    return neuronaOcultaDict


def agregarCantidadEntradasNeuronaSalidaDict(neuronaSalidaDict, cantidadNeuronasOculta):
    numeroEntrada = 1
    for numeroFila in range(4):
        for j in range(cantidadNeuronasOculta):
            neuronaSalidaDict[1][numeroFila+1]["entrada" +
                                               str(numeroEntrada)] = "sin datos"
            numeroEntrada = numeroEntrada + 1
        numeroEntrada = 1
    return neuronaSalidaDict


def calcularPesosNecesarios(cantidadNeuronasOculta):
    cantidadPesosNeuronaOculta = 3*cantidadNeuronasOculta
    cantidadPesosNeuronaSalida = 1 + (cantidadNeuronasOculta)
    return [cantidadPesosNeuronaOculta, cantidadPesosNeuronaSalida]


def eliminarPesosSobrantes(cantidadPesosNeuronaOculta, cantidadPesosNeuronasSalida, listaTodosPesos):
    cantidadTotalPesos = cantidadPesosNeuronaOculta+cantidadPesosNeuronasSalida
    totalListaPesosPredeterminada = len(listaTodosPesos)
    diferencia = totalListaPesosPredeterminada-cantidadTotalPesos
    for i in range(diferencia):
        listaTodosPesos.pop()
    return listaTodosPesos


def repartirPesos(cantidadPesosNeuronaOculta, cantidadPesosNeuronaSalida, listaTodosPesos):
    listaPesosSalida = []
    listaPesosOculta = []

    for i in range(cantidadPesosNeuronaSalida):
        listaPesosSalida.append(listaTodosPesos.pop())
    for i in range(cantidadPesosNeuronaOculta):
        listaPesosOculta.append(listaTodosPesos.pop())
    listaPesosSalida = listaPesosSalida[::-1]
    listaPesosOculta = listaPesosOculta[::-1]

    return listaPesosOculta, listaPesosSalida


def ingresarPesosPantallaNeuronasOculta(cantidadPesos):
    # Agregar pesos neurona Oculta
    listaPesos = []
    print("-----Capa Oculta-----")
    for i in range(cantidadPesos):
        peso = float(input("Ingrese peso w"+str(i) + ": "))
        listaPesos.append(peso)
    print("")
    return listaPesos


def ingresarPesosPantallaNeuronasSalida(cantidadPesos, cantidadPesosCapaOculta):
    # Agregar pesos neurona Oculta
    print("-----Capa de Salida-----")
    listaPesos = []
    for i in range(cantidadPesos):
        peso = float(
            input("Ingrese peso w"+str(cantidadPesosCapaOculta) + ": "))
        listaPesos.append(peso)
        cantidadPesosCapaOculta = cantidadPesosCapaOculta + 1
    print("")
    return listaPesos


def agregarPesosANeuronas(cantidadNeuronasOculta, neuronaOcultaDict, listaPesosNeuronasOculta, neuronaSalidaDict, listaPesosNeuronasSalida):
    neuronaOcultaDict = agregarPesosNeuronasOculta(
        cantidadNeuronasOculta, neuronaOcultaDict, listaPesosNeuronasOculta)

    neuronaSalidaDict = agregarPesosNeuronasSalida(
        neuronaSalidaDict, listaPesosNeuronasSalida)

    neuronaSalidaDict = agregarCantidadPesosNeuronaSalidaDict(
        neuronaSalidaDict, cantidadNeuronasOculta)
    return neuronaOcultaDict, neuronaSalidaDict


# Agregar los pesos ingresados a cada neurona de la capa de oculta
def agregarPesosNeuronasOculta(cantidadNeuronasOculta, neuronaOcultaDict, listaPesos):
    listaPesosRevertida = listaPesos[::-1]
    for numeroNeuronaOculta in range(cantidadNeuronasOculta):
        for i in range(3):
            neuronaOcultaDict[numeroNeuronaOculta +
                              1][5]["w"].append(listaPesosRevertida.pop())
    return neuronaOcultaDict


# Agregar los pesos ingresados a la neurona de la capa de salida
def agregarPesosNeuronasSalida(neuronaSalidaDict, listaPesos):
    listaPesosRevertida = listaPesos[::-1]
    for i in range(len(listaPesosRevertida)):
        neuronaSalidaDict[1][5]["w"].append(listaPesosRevertida.pop())
    return neuronaSalidaDict


def agregarCantidadPesosNeuronaSalidaDict(neuronaSalidaDict, cantidadNeuronasOculta):
    cantidadNeuronasOculta = len(neuronaSalidaDict[1][5]["w"])
    # Le agrego el +1 por el peso que tiene la neurona con el bias
    for i in range(cantidadNeuronasOculta):
        nueva_lista = []
        neuronaSalidaDict[1][5]["totalPesos"].append(nueva_lista)
    return neuronaSalidaDict


# ----------------------------------------Mètodos para entrenar perceptrones----------------------------------------
# ----------------------------------------Mètodos para entrenar perceptrones----------------------------------------
# ----------------------------------------Mètodos para entrenar perceptrones----------------------------------------

# Calcular sumatoria
def calculoX(eList, wList, umbral):
    sumatoria = 0
    for i in range(len(eList)):
        termino = eList[i] * wList[i]
        sumatoria = sumatoria + termino
    # sumatoria = sumatoria - umbral
    return sumatoria


# Calcular salida Real
def calculoY(x):
    y = 1 / (1 + (math.e) ** -x)
    # y = 1/(1+(math.exp(-x)))
    return y


def calculoError(salidaDeseada, salidaReal):
    return salidaDeseada - salidaReal


def calculoDelta(salidaReal, errorDelta):
    delta = salidaReal * (1 - salidaReal) * errorDelta
    return delta


def calculoCambioPeso(lr, entrada, delta):
    cambioPeso = lr * entrada * delta
    return cambioPeso


def calculoNuevoPeso(peso, cambioPeso):
    nuevoPeso = peso + cambioPeso
    return nuevoPeso


def guardarValoresNeuronaOculta(neuronaCapaDict, numeroNeurona, cantidadFilas, y):
    # se guarda la salida real en el dict para luego usarla como entrada en las siguientes neuronas
    neuronaCapaDict[numeroNeurona +
                    1][cantidadFilas+1]["salidaReal"] = y
    return neuronaCapaDict


def buscarEntradasNeuronaSalida(neuronaSalidaDict, neuronaOcultaDict, cantidadNeuOculta, cantidadFilas, cantidadNeuSalida):
    entradasNeurona = []
    entradasNeurona.append(
        neuronaSalidaDict[cantidadNeuSalida+1][cantidadFilas+1]["bias"])

    for cantidadNeuOculta in range(len(neuronaOcultaDict)):
        entradasNeurona.append(
            neuronaOcultaDict[cantidadNeuOculta+1][cantidadFilas+1]["salidaReal"])
    return entradasNeurona


def guardarValoresNeuronaSalida(neuronaCapaDict, numeroNeurona, cantidadFilas, listaEntradas, y, nuevoError):
    for k in range(len(listaEntradas)):
        neuronaCapaDict[numeroNeurona+1][cantidadFilas +
                                         1]["entrada" + str(k+1)] = listaEntradas[k]
    # se guarda la salida real en el dict para luego usarla como entrada en las siguientes neuronas
    neuronaCapaDict[numeroNeurona +
                    1][cantidadFilas+1]["salidaReal"] = y
    neuronaCapaDict[numeroNeurona +
                    1][cantidadFilas+1]["error"] = nuevoError
    neuronaCapaDict[numeroNeurona+1][cantidadFilas +
                                     1]["totalErrores"].append(nuevoError)
    return neuronaCapaDict


def actualizarPeso(lr, j, neuronaCapaDict, cantNeuronas, cantFilas, delta, wList):
    # si j == 0 es porque vamos a cambiar el peso del bias
    if j == 0:
        cambioPeso = calculoCambioPeso(
            lr, neuronaCapaDict[cantNeuronas+1][cantFilas+1]["bias"], delta)
    else:
        cambioPeso = calculoCambioPeso(
            lr, neuronaCapaDict[cantNeuronas+1][cantFilas+1]["entrada"+str(j)], delta)
    # ir llenando la lista nuevListPeso con los pesos nuevos asi el error va bajando
    nuevoPeso = calculoNuevoPeso(wList[j], cambioPeso)
    return nuevoPeso


def agregarPesoDict(j, neuronaCapaDict, cantidadNeuCapa, nuevoPeso):
    neuronaCapaDict[cantidadNeuCapa+1][5]["w"][j] = nuevoPeso
    neuronaCapaDict[cantidadNeuCapa +
                    1][5]["totalPesos"][j].append(nuevoPeso)
    return neuronaCapaDict


# Hacer todos los calculos llamando a las otras funciones
def triggerNeuralNetwork(
    xorDict, lr, umbral, neuronaOcultaDict, neuronaSalidaDict
):
    iteracion = 0
    condicion = False

    # while iteracion < 10000:
    while condicion is False:
        # print("-----Iteracion ", iteracion+1, "-----")
        for cantidadFilas in range(4):
            # --------------------------------Feed forward--------------------------------
            # --------------------------------Feed forward--------------------------------
            # --------------------------------Feed forward--------------------------------
            # cantidad neuronas oculta
            for cantidadNeuOculta in range(len(neuronaOcultaDict)):
                entradasNeurona = [neuronaOcultaDict[cantidadNeuOculta+1][cantidadFilas+1]["bias"],
                                   neuronaOcultaDict[cantidadNeuOculta+1][cantidadFilas+1]["entrada1"], neuronaOcultaDict[cantidadNeuOculta+1][cantidadFilas+1]["entrada2"]]

                wList = neuronaOcultaDict[cantidadNeuOculta + 1][5]["w"]

                x = calculoX(entradasNeurona, wList, umbral)
                y = calculoY(x)

                neuronaOcultaDict = guardarValoresNeuronaOculta(
                    neuronaOcultaDict, cantidadNeuOculta, cantidadFilas, y)

            for cantidadNeuSalida in range(1):
                cantidadNeuOculta = len(neuronaOcultaDict)

                entradasNeurona = buscarEntradasNeuronaSalida(
                    neuronaSalidaDict, neuronaOcultaDict, cantidadNeuOculta, cantidadFilas, cantidadNeuSalida)

                wList = neuronaSalidaDict[cantidadNeuSalida +
                                          1][5]["w"]

                x = calculoX(entradasNeurona, wList, umbral)
                y = calculoY(x)
                nuevoError = calculoError(
                    xorDict[cantidadFilas + 1]["salidaDeseada"], y)
                # Saco el bias de la lista de entradas asi guardo las entradas en el diccionaro de la neurona
                entradasNeurona.pop(0)

                neuronaSalidaDict = guardarValoresNeuronaSalida(
                    neuronaSalidaDict, cantidadNeuSalida, cantidadFilas, entradasNeurona, y, nuevoError)

            # --------------------------------back Propagation--------------------------------
            # --------------------------------back Propagation--------------------------------
            # --------------------------------back Propagation--------------------------------
            deltaFinal = calculoDelta(neuronaSalidaDict[len(neuronaSalidaDict)][cantidadFilas+1]
                                      ["salidaReal"], neuronaSalidaDict[len(neuronaSalidaDict)][cantidadFilas+1]["error"])

            for cantidadNeuSalida in range(1):
                wList = neuronaSalidaDict[cantidadNeuSalida +
                                          1][5]["w"]
                for j in range(len(neuronaSalidaDict[cantidadNeuSalida+1][5]["w"])):
                    nuevoPeso = actualizarPeso(
                        lr, j, neuronaSalidaDict, cantidadNeuSalida, cantidadFilas, deltaFinal, wList)

                    neuronaSalidaDict = agregarPesoDict(
                        j, neuronaSalidaDict, cantidadNeuSalida, nuevoPeso)

            for cantidadNeuOculta in range(len(neuronaOcultaDict)):
                deltaOculta = calculoDelta(neuronaOcultaDict[cantidadNeuOculta+1][cantidadFilas+1]
                                           ["salidaReal"], deltaFinal)
                wList = neuronaOcultaDict[cantidadNeuOculta +
                                          1][5]["w"]

                for j in range(len(neuronaOcultaDict[cantidadNeuOculta+1][5]["w"])):
                    nuevoPeso = actualizarPeso(
                        lr, j, neuronaOcultaDict, cantidadNeuOculta, cantidadFilas, deltaOculta, wList)

                    neuronaOcultaDict = agregarPesoDict(
                        j, neuronaOcultaDict, cantidadNeuOculta, nuevoPeso)

            if abs(neuronaSalidaDict[cantidadNeuSalida+1][cantidadFilas+1]["error"]) < 0.1:
                neuronaSalidaDict[cantidadNeuSalida +
                                  1][cantidadFilas+1]["errorBajo"] = True

            for i in range(4):
                if neuronaSalidaDict[cantidadNeuSalida+1][i+1]["errorBajo"]:
                    condicion = True
                else:
                    condicion = False

        iteracion = iteracion + 1

    dict = [neuronaOcultaDict, neuronaSalidaDict, iteracion]
    return dict


def mostrarResultado(neuronaOcultaDict, neuronaSalidaDict, graficar):
    print("-----Capa oculta-----")
    numeroPeso = 0
    print("")
    for numeroNeuronaOculta in range(len(neuronaOcultaDict)):
        print("-----Neurona "+str(numeroNeuronaOculta+1)+"-----")
        for numeroFila in range(4):
            print("-----Fila", numeroFila+1, "-----")
            for numeroEntrada in range(2):
                print("Entrada ", numeroEntrada+1, ": ",
                      neuronaOcultaDict[numeroNeuronaOculta+1][numeroFila+1]["entrada"+str(numeroEntrada+1)])
            print("Salida real: ",
                  neuronaOcultaDict[numeroNeuronaOculta+1][numeroFila+1]["salidaReal"])
            print("")
        print("Pesos: ")
        for i in range(3):
            print("w"+str(numeroPeso)+":",
                  neuronaOcultaDict[numeroNeuronaOculta+1][5]["w"][i])
            numeroPeso = numeroPeso + 1
        print("")
        print("")

    print("-----Capa salida-----")
    print("")
    for numeroNeuronaSalida in range(len(neuronaSalidaDict)):
        print("-----Neurona "+str(numeroNeuronaSalida)+"-----")
        for numeroFila in range(4):
            print("-----Fila", numeroFila+1, "-----")
            for numeroEntrada in range(len(neuronaOcultaDict)):
                print("Entrada ", str(numeroEntrada+1), ": ",
                      neuronaSalidaDict[numeroNeuronaSalida+1][numeroFila+1]["entrada"+str(numeroEntrada+1)])
            print("Salida real: ",
                  neuronaSalidaDict[numeroNeuronaSalida+1][numeroFila+1]["salidaReal"])
            print(
                "Error: ", neuronaSalidaDict[numeroNeuronaSalida+1][numeroFila+1]["error"])
            print("")
        print("Pesos: ")
        for i in range(len(neuronaOcultaDict)+1):
            print("w"+str(numeroPeso)+":",
                  neuronaSalidaDict[numeroNeuronaSalida+1][5]["w"][i])
            numeroPeso = numeroPeso + 1
            print("")

    if graficar:
        numeroPeso = 0
        listaPesos = []
        for numeroNeuronaOculta in range(len(neuronaOcultaDict)):
            for i in range(3):
                listaPesos.append(
                    neuronaOcultaDict[numeroNeuronaOculta+1][5]["totalPesos"][i])

                numeroPeso = numeroPeso + 1

        for numeroNeuronaSalida in range(len(neuronaSalidaDict)):
            for i in range(len(neuronaSalidaDict[numeroNeuronaSalida+1][5]["totalPesos"])):
                listaPesos.append(
                    neuronaSalidaDict[numeroNeuronaSalida+1][5]["totalPesos"][i])

                numeroPeso = numeroPeso + 1

        error1 = neuronaSalidaDict[1][1]["totalErrores"]
        error2 = neuronaSalidaDict[1][2]["totalErrores"]
        error3 = neuronaSalidaDict[1][3]["totalErrores"]
        error4 = neuronaSalidaDict[1][4]["totalErrores"]

        listaErrores = [error1, error2, error3, error4]

        mostrarGrafico(listaPesos, listaErrores)


def mostrarGrafico(listaPesos, listaErrores):
    figure = plt.figure()
    figure.set_size_inches(16, 13)
    # figure.suptitle("red=error - blue=w0 - black=w1 - yellow=w2", fontsize=16)
    # Cree un nuevo subgrafo, la cuadrícula es 1x2, el número de serie es 1, el primer número es el número de filas, el segundo número es el número de columnas, lo que indica la disposición de los subgrafos, y el tercer número es el número de serie del subgrafo
    plt.subplot(1, 2, 1)
    plt.xlabel("iteraciones")
    for numeroPeso in range(len(listaPesos)):
        plt.plot(listaPesos[numeroPeso], label="w"+str(numeroPeso))
    plt.legend()
    plt.title("Pesos")

    plt.subplot(1, 2, 2)
    plt.xlabel("iteraciones")
    plt.plot(listaErrores[0], label="error1")
    plt.plot(listaErrores[1], label="error2")
    plt.plot(listaErrores[2], label="error3")
    plt.plot(listaErrores[3], label="error4")
    plt.legend()
    # Establecer el título de la subimagen
    plt.title("Errores")
    plt.show()


def menu():
    print("--------------------")
    print("1: Ingresar cantidad de neuronas capa oculta y valor LR")
    print("2: Agregar/Reestablecer valores de los pesos por defecto")
    print("3: Agregar valores de los pesos manualmente")
    print("4: Mostrar valores del perceptrón")
    print("5: Lanzar entrenamiento compuerta XOR")
    print("6: Salir del programa")
    print("")

    option = input("Ingrese el número de la opción que desea ejecutar: ")
    os.system("clear")

    return option


input("Bienvenido al perceptron, presione enter para acceder al menú")


xorDict = {
    1: {"Fila": 1, "entrada1": 0, "entrada2": 0, "salidaDeseada": 0},
    2: {"Fila": 2, "entrada1": 0, "entrada2": 1, "salidaDeseada": 1},
    3: {"Fila": 3, "entrada1": 1, "entrada2": 0, "salidaDeseada": 1},
    4: {"Fila": 4, "entrada1": 1, "entrada2": 1, "salidaDeseada": 0},


}

neuronaOcultaDict = {}
neuronaSalidaDict = {}

informationDict = {}

umbral = 0.1
lr = 0.1
cantidadNeuronasOculta = 0

cantidadPesosNeuronas = []

exit = 0


while exit != 1:
    option = menu()
    os.system("clear")

    if option == "1":
        cantidadNeuronasOculta = int(
            input("Ingrese la cantidad de neuronas de la capa oculta: "))
        lr = float(
            input("Ingrese el valor de LR: "))

        neuronaOcultaDict = establecerPrimeraNeurona("oculta")
        neuronaSalidaDict = establecerPrimeraNeurona("salida")

        neuronaOcultaDict = agregarNeuronasOcultaDict(
            neuronaOcultaDict, cantidadNeuronasOculta)
        neuronaSalidaDict = agregarCantidadEntradasNeuronaSalidaDict(
            neuronaSalidaDict, cantidadNeuronasOculta)

        cantidadPesosNeuronas = calcularPesosNecesarios(cantidadNeuronasOculta)

    if option == "2":
        print("-----Ingresar pesos predeterminados-----")
        listaTodosPesos = [0.9, 0.7, 0.5, 0.3, -0.9, -1, 0.8, 0.35, 0.1, -0.23, -0.79, 0.56, 0.6, 0.22, -0.22, -0.55, 0.31, -0.32, 0.38, -0.09, -0.95, -0.18, -0.94, -0.42, -0.27, 0.08, -0.51, -0.31, -0.29, 0.54, -0.43, 0.75, -0.09, -0.55, 0.07, -0.93, 0.52, -0.17, 0.32, -0.48, -0.02, -0.66, 0.97, 0.92, -0.24, 0.69, -0.36, -0.78, 0.21, -0.07, -0.59, 0.83, -0.97, -0.83, -0.59, -0.76, -0.28, -0.34, -0.21, -0.68, 0.05, -0.17, 0.22, -0.06, 0.63, -0.12, 0.64, -0.47, -0.38, -0.91, -0.35, -0.42, 0.13, -0.41, 0.88, 0.3, -0.01, -0.88, 0.72, -0.43, 0.81, 0.5, 0.97, -0.36, 0.45, 0.24, -0.8, 0.42, -0.42, 0.08, 0.01, -0.35, -0.21, -0.02, -0.13, -0.33, -0.73, -0.76, -0.93, -0.02, 0.06, -0.6, -0.33, -0.62, 0.54, 0.69, 0.32, -0.02, 0.67, 0.91, -0.08, 0.26, 0.6, 0.61, 0.19, 0.54, -0.47, -0.25, -0.08, 0.94, -0.07, -0.55, 0.66, 0.98, -0.72, 0.46, 0.55, -0.44, -0.81, 0.46, 0.22, 0.2, 0.01, -0.75, 0.67, 0.1, -0.92, 0.3, -0.21, 0.8, 0.43, 1.0, 0.82, 0.22, -0.63, -0.22, -0.16, 0.25, -0.3, -0.73, -0.99, -0.79, 0.56, -0.44, -0.63, -0.6, -0.44, 0.56, 0.93, 0.51, 0.18, 0.79, -0.01, 0.11, 0.54, -0.48, 0.18, 0.99, 0.54, 0.45, -0.16, -0.91, 0.26, -0.01, -0.42, -0.97, 0.89, -0.69, 0.2, 0.27, 0.07, 0.67, -0.17, 0.02, -0.85, 0.82, 0.92, 0.59, -0.17,
                           0.39, -0.4, 0.14, -0.45, -0.95, 0.14, 0.18, -0.64, 0.56, -0.11, -0.91, -0.76, 0.29, -0.29, -0.13, 0.4, -0.81, 0.96, -0.9, -0.05, 0.02, 0.87, 0.16, -0.57, -0.35, 0.25, 0.2, -0.1, -0.8, 0.49, 0.63, -0.59, 0.41, -0.2, 0.19, -0.2, 0.57, 0.69, 0.3, 0.56, -0.44, -0.02, -0.91, 0.79, -0.28, -0.54, -0.3, 0.56, -0.5, 0.28, -0.47, 0.87, 0.3, 0.14, 0.5, 0.6, -0.89, -0.36, 0.03, -0.55, 0.66, -0.9, -0.12, 0.02, -0.79, -0.26, -0.3, -0.82, -0.09, 0.47, 0.61, 0.03, -0.08, 0.72, -0.49, 0.32, -0.74, -0.61, 0.46, 0.46, -0.15, -0.67, -0.54, -0.88, 0.87, 0.86, 0.65, 0.38, 0.17, -0.59, 0.34, -0.88, 0.24, -0.9, -0.92, 0.33, -0.3, -0.31, -0.52, 0.37, -0.59, 0.13, -0.91, -0.51, -0.67, -0.94, 0.43, 0.05, 0.4, 0.83, -0.33, 0.28, -0.89, -0.66, -0.17, -0.07, -0.04, -0.71, 0.53, 0.86, -0.67, -0.33, -0.98, -0.63, -0.36, -0.49, -0.27, 0.47, 0.25, -0.35, -0.04, 0.18, -0.86, -0.43, 0.39, 0.32, -0.31, -0.22, 0.88, -0.42, -0.52, 0.98, 0.59, -0.19, 0.19, 0.3, -0.19, -0.79, -0.12, 0.44, -0.08, -0.45, 0.28, -0.7, 0.67, -0.3, 0.34, -0.13, -0.65, -0.47, -0.86, 0.47, 0.73, 0.72, 0.01, -0.29, 0.56, -0.54, 0.94, 0.77, 0.86, -0.68, -0.19, 0.48, -0.5, -0.81, 0.48, -0.34, -0.69, 0.69, 0.65, 0.3, 0.22, -0.98, -0.69, 0.0, -0.99, -0.59, 0.4, -0.81, 0.19, 0.86, -0.03, -0.53, 0.67, -0.14, 0.72, 0.21, 0.05, -0.3, -0.65, -0.31, 0.02, 0.95, -0.47, -0.27, -0.57, -0.54, -0.2, -0.84, 0.61, 0.45]

        listaTodosPesos = eliminarPesosSobrantes(
            cantidadPesosNeuronas[0], cantidadPesosNeuronas[1], listaTodosPesos)
        listaPesosNeuronasOculta, listaPesosNeuronasSalida = repartirPesos(
            cantidadPesosNeuronas[0], cantidadPesosNeuronas[1], listaTodosPesos)

        neuronaOcultaDict, neuronaSalidaDict = agregarPesosANeuronas(
            cantidadNeuronasOculta, neuronaOcultaDict, listaPesosNeuronasOculta, neuronaSalidaDict, listaPesosNeuronasSalida)

        print("")
        if any(neuronaOcultaDict and neuronaSalidaDict):
            print(
                "Se han ingresado exitosamente los valores de los pesos por defecto")
            mostrarResultado(
                neuronaOcultaDict, neuronaSalidaDict, False)
            print("")
        print("----------------")

    if option == "3":
        print("-----Ingresar pesos de las neuronas-----")
        listaPesosNeuronasOculta = ingresarPesosPantallaNeuronasOculta(
            cantidadPesosNeuronas[0])
        listaPesosNeuronasSalida = ingresarPesosPantallaNeuronasSalida(
            cantidadPesosNeuronas[1], len(listaPesosNeuronasOculta))

        neuronaOcultaDict, neuronaSalidaDict = agregarPesosANeuronas(
            cantidadNeuronasOculta, neuronaOcultaDict, listaPesosNeuronasOculta, neuronaSalidaDict, listaPesosNeuronasSalida)

        mostrarResultado(
            neuronaOcultaDict, neuronaSalidaDict, False)

    if option == "4":
        print("-----Mostrar valores del perceptrón-----")
        print("")
        if not any(neuronaOcultaDict or neuronaSalidaDict):
            print(
                "Aùn no se han agregado datos, regrese al menu y elija la opciòn 1 para agregarlos")
            print("")
        else:
            mostrarResultado(
                neuronaOcultaDict, neuronaSalidaDict, False)

    # compuerta XOR
    if option == "5":
        print("-----Lanzar entrenamiento compuerta XOR-----")

        neuronas = triggerNeuralNetwork(
            xorDict, lr, umbral, neuronaOcultaDict, neuronaSalidaDict
        )
        print("")
        # print(yaml.dump(neuronas, default_flow_style=False))
        print("Iteraciones: ", neuronas[2])
        print("")
        mostrarResultado(neuronas[0], neuronas[1], True)

    if option == "6":
        exit = 1
        break

    input("Presione enter para regresar al menú del programa")
    os.system("clear")
