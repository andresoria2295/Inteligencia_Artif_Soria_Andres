#!/usr/bin/python3
#coding=utf-8

#def mostrar_menu(opciones):
#    print('Seleccionar una opción:')
#    for clave in sorted(opciones):
        #print(f' {clave}) {opciones[clave][0]}')
#        print('hola')

def leer_opcion(opciones):
    #while (a == input('Opción: ')) not in opciones:
    #    print('Opción incorrecta, vuelva a intentarlo.')
    #eturn a
    while True:
        ans = input("How many continents in the world?: ")
        if ans == "7":
            #name = True
            print("Right")
            break
        else:
            print("\nThat is incorrect, please try again.\n")

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        #mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1' : ('Opción 1', accion1),
        '2' : ('Opción 2', accion2),
        '3' : ('Opción 3', accion3),
        '4' : ('Salir', salir)
    }

    #generar_menu(opciones, '4')
    leer_opcion(opciones)

def accion1():
    print('Has elegido la opcion 1')

def accion2():
    print('Has elegido la opcion 2')

def accion3():
    print('Has elegido la opcion 3')

def salir():
    print('Has elegido la opcion salir')

if __name__ == '__main__':
    menu_principal()
