import os
from clases import *
from funciones import *

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Seleccione una opcion: "))
            correcto=True
        except ValueError:
            print('Error, error la opcion no es valida')
     
    return num

def imprimir():
   
    print("________________________")
    print("Bienvenido al Cajero")
    print("________________________")
    print()
    print("Opciones disponibles:")
    print("1. Ver saldo disponible")
    print("2. Extraer Dinero")
    print("3. Depositar dinero")
    print("0. Salir")
    print()

def imprimir_admin():
    
    print("________________________")
    print("Bienvenido Administrador")
    print("________________________")
    print()
    print("Opciones disponibles:")
    print("1. Crear cuenta")
    print("2. Modificar")
    print("3. Eliminar")
    print("0. Salir")
    print()

def eleccionCuentaCliente():
    print("_____________________________________")
    print("Desea crea un cliente o una cuenta?: ")
    print("_____________________________________")
    print()
    print("Opciones disponibles:")
    print("1. Crear cliente")
    print("2. Crear cuenta")
    print("0. Salir")

def menu(miLogin):
    salir = 0
    opcion = 0
    while not salir:
        if valid_admin(miLogin) == True:
            imprimir_admin()
            opcion = pedirNumeroEntero()
            if opcion == 1:
                eleccionCuentaCliente()
                opcion = pedirNumeroEntero()
                if opcion == 1:
                  crearuser()
                elif opcion == 2:
                  crearaccount()
                else:
                  pass
            elif opcion == 2:
               modiuser()
            elif opcion == 3:
                eliminarusuario()
            elif opcion == 0:
                print("Vuelva pronto")
                salir = True
            else:
                print ("Introduzca un numero entre 1 y 3")
        else:
            imprimir()
            opcion = pedirNumeroEntero()
            if opcion == 1:
                pass
            elif opcion == 2:
                print ("Opcion 2")
            elif opcion == 3:
                print("Opcion 3")
            elif opcion == 0:
                salir = True
            else:
                print ("Introduzca un numero entre 1 y 3")
        
            print ("Vuelva Pronto")
    