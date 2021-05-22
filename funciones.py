from clases import Account, User
import os.path as path
from tempfile import mkstemp
from shutil import move
from os import remove, close

#Funciones login#
archivo_cuenta = 'cuenta.txt'
archivo_cliente = 'cliente.txt'
 
def logueo(credenciales):
    print("____________________________")
    print("Bienvenido al Banco Central")
    print("____________________________\n")
    print("Digite su usuario")
    credenciales.user = input()
    print("\nDigite su contraseña: ")
    credenciales.password = input()
    
    if userIntxt(credenciales):
        print("Usuario encontrado")
        return True
    else:
      print("Error!, usuario no registrado")
      return False

def valid_admin(credenciales):
    valid = False
    if credenciales.user == "admin" and credenciales.password == "admin":
        valid = True
    return valid

def userIntxt(credenciales):
    inttxt = False
    try:
        archivo = open(archivo_cliente, "r")
        for linea in archivo:
            txt = linea

            x = txt.split(",")
            usuario = x[0]
            contra = x[1]
            if (usuario == credenciales.user and contra == credenciales.password):
                inttxt = True
                break
            
        archivo.close()
        
    except:
        print("Error al abrir el archivo")   
    
    return inttxt
 
#Funciones crud#
#Crear cuenta y crear cliente#
def crearuser():
    try:
        currentUser = User()
        archivo = open(archivo_cliente, "a")
        print("-------------------------")
        print("Creando Cliente")
        print("-------------------------")
        print("Digite el usuario: ")
        currentUser.userName = input()
        print("Digite la contrasena: ")
        currentUser.passw = input()
        print("Digite la cedula: ")
        currentUser.id = input()
        print("Digite el nombre: ")
        currentUser.name = input()
        print("Digite el apellido: ")
        currentUser.lastname = input()
        action = True
        if not validar_archivo(archivo_cliente):
            archivo = open(archivo_cliente, "w")
            archivo.write(currentUser.userName+","+currentUser.passw+","+currentUser.id+","+currentUser.name+","+currentUser.lastname)   
        else:
            if validarIdentCliente(currentUser.id):
                 print("El cliente ya esta registrado")
                 action = False
            else:
                archivo = open(archivo_cliente, "a")
                archivo.write("\n"+currentUser.userName+","+currentUser.passw+","+currentUser.id+","+currentUser.name+","+currentUser.lastname) 
        archivo.close()
        return action
    except:
        print("Error al abrir el archivo")

def crearaccount():    
    try:
        currentAccount = Account()
        print("-------------------------")
        print("Creando Cuenta")
        print("-------------------------")
        print("Digite el numero de cedula: ")
        currentAccount.iden = input()
        print("Digite el numero de cuenta: ")
        currentAccount.num_account = input()
        print("Digite el saldo inicial de la cuenta: ")
        currentAccount.balance = input()
        action = True
        if not validar_archivo(archivo_cuenta):
            archivo = open(archivo_cuenta, "w")
            print("Desea agregar una segunda cuenta: 1 (Si) * (No)")
            entrada = input()
            c2 = "_"
            na2 = "_"
            if entrada == "1":
                print("Digite el numero de cuenta #2: ")
                na2 = input()
                print("Digite el saldo inicial de cuenta #2: ")
                c2  = input()
            archivo.write(currentAccount.iden+","+currentAccount.num_account+","+currentAccount.balance+","+na2+","+c2)   
                
        else:
            if validarIdentCuenta(currentAccount.iden):
                 print("El usuario ya posee una cuenta o mas cuentas")
                 action = False
            else:
                archivo = open(archivo_cuenta, "a")
                print("Desea agregar una segunda cuenta: 1 (Si) * (No)")
                entrada = input()
                c2 ="_"
                na2 = "_"
                if entrada == "1":
                    print("Digite el numero de cuenta #2: ")
                    na2 = input()
                    print("Digite el saldo inicial de cuenta #2: ")
                    c2  = input()
                archivo.write("\n"+currentAccount.iden+","+currentAccount.num_account+","+currentAccount.balance+","+na2+","+c2)   
        return action
    except:
        print("Error al abrir el archivo")   
 

def validar_archivo(archivo):
    return path.exists(archivo)

def validarIdentCuenta(ident):
    inttxt = False
    try:
        archivo = open(archivo_cuenta, "r")
        for linea in archivo:
            txt = linea
            x = txt.split(",")
            cedula = x[0]
            if (cedula == ident):
                inttxt = True
                break
            
        archivo.close()
        
    except:
        print("Error al abrir el archivo")   
    
    return inttxt

def validarIdentCliente(ident):
    inttxt = False
    try:
        archivo = open(archivo_cliente, "r")
        for linea in archivo:
            txt = linea
            x = txt.split(",")
            id = x[2]
            if (id == ident):
                inttxt = True
                break
            
        archivo.close()
        
    except:
        print("Error al abrir el archivo")   
    
    return inttxt

#Modoficar cliente y cuenta#

def modiuser():
    
    try:
        updateUser = User()
        print("-------------------------")
        print("Modificando usuario")
        print("-------------------------\n")
        print("Digite el numero de cedula: ")
        updateUser.id = input()
        if not validarIdentCliente(updateUser.id):
            print("El cliente no existe")
        else:
            print("Digite el usuario: ")
            updateUser.userName = input()
            print("Digite la contrasena: ")
            updateUser.passw = input()
            print("Digite el nombre: ")
            updateUser.name = input()
            print("Digite el apellido: ")
            updateUser.lastname = input()
            replace(updateUser)
        
        
    except Exception as e:
        print(e)
        print("Error al abrir el archivo")   
    
def replace(updateUser):
    #archivo = open(archivo_cliente, "r")
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(archivo_cliente) as old_file:
            for line in old_file:
                txt = line
                x = txt.split(",")
                id = x[2]
                if (id == updateUser.id):
                    newline =updateUser.userName+","+updateUser.passw+","+updateUser.id+","+updateUser.name+","+updateUser.lastname
                    new_file.write(newline+"\n")
                else:
                    new_file.write(line)
    close(fh)
    #Remove original file
    remove(archivo_cliente)
    #Move new file
    move(abs_path, archivo_cliente)
    #archivo.close()

#Eliminar cleinte y cuenta

def borrar(ident):
    #archivo = open(archivo_cliente, "r")
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(archivo_cliente) as old_file:
            for line in old_file:
                txt = line
                x = txt.split(",")
                id = x[2]
                if (id != ident):
                   new_file.write(line)
                    
    close(fh)
    #Remove original file
    remove(archivo_cliente)
    #Move new file
    move(abs_path, archivo_cliente)
    #archivo.close()

def eliminarusuario():
    try:
        
        print("-------------------------")
        print("Elimando usuario")
        print("-------------------------\n")
        print("Digite el numero de cedula: ")
        ident = input()
        if not validarIdentCliente(ident):
            print("El cliente no existe")
        else:
            borrar(ident)
        
        
    except Exception as e:
        print(e)
        print("Error al abrir el archivo")