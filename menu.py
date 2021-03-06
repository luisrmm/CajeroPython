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
    
    print("________________________________")
    print("Bienvenido Administrador")
    print("________________________________")
    print()
    print("Opciones disponibles:")
    print("1. Crear cliente o cuenta")
    print("2. Modificar cliente o cuenta")
    print("3. Eliminar cliente o cuenta")
    print("0. Salir")
    print()

def eleccionCuentaCliente():
    print("_____________________________________")
    print("Desea crear un cliente o una cuenta?: ")
    print("_____________________________________")
    print()
    print("Opciones disponibles:")
    print("1. Crear cliente")
    print("2. Crear cuenta")
    print("0. Salir")

def eleccionCuentaClienteModi():
    print("__________________________________________")
    print("Desea modificar un cliente o una cuenta?: ")
    print("__________________________________________")
    print()
    print("Opciones disponibles:")
    print("1. Modificar cliente")
    print("2. Modificar cuenta")
    print("0. Salir")

def eleccionCuentaClienteElimi():
    print("_________________________________________")
    print("Desea eliminar un cliente o una cuenta?: ")
    print("_________________________________________")
    print()
    print("Opciones disponibles:")
    print("1. ELiminar cliente")
    print("2. Eliminar cuenta")
    print("0. Salir")

def menu(milogin):
    salir = 0
    opcion = 0
    while not salir:
        if valid_admin(milogin) == True:
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
                eleccionCuentaClienteModi()
                opcion = pedirNumeroEntero()
                if opcion == 1:
                  modiuser()
                elif opcion == 2:
                  modiaccount()
                else:
                  pass
            elif opcion == 3:
                eleccionCuentaClienteElimi()
                opcion = pedirNumeroEntero()
                if opcion == 1:
                  eliminarusuario()
                elif opcion == 2:
                  eliminarCuenta()
                else:
                  pass
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
    