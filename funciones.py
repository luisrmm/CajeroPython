from clases import Account, User, Login
import os.path as path
from tempfile import mkstemp
from shutil import move
from os import remove, close

#Funciones login#
account_file = 'cuenta.txt'
account_client = 'cliente.txt'

def crearadmin():
    try:
        with open(account_client, "w") as archivo:
         archivo.write("admin,admin,admin,admin,admin")
    except Exception as e:
        print(e)

def logueo(credenciales):
    print("____________________________")
    print("Bienvenido al Banco Central")
    print("____________________________\n")
    print("Digite su usuario")
    credenciales.user = input()
    print("\nDigite su contraseña: ")
    credenciales.password = input()
    
    if userIntxt(credenciales.user, credenciales.password):
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

def userIntxt(ident, passw):
    inttxt = False
    try:
        archivo = open(account_client, "r")
        for linea in archivo:
            txt = linea

            x = txt.split(",")
            usuario = x[0]
            contra = x[1]
            if (usuario == ident and contra == passw):
                inttxt = True
                break
            
        archivo.close()
        
    except Exception as e:
            print(e)
    
    return inttxt

def validUserName(ident, passw):
    inttxt = False
    try:
        archivo = open(account_client, "r")
        for linea in archivo:
            txt = linea

            x = txt.split(",")
            usuario = x[0]
            contra = x[1]
            if (usuario == ident or contra == passw ):
                inttxt = True
                break
            
        archivo.close()
        
    except Exception as e:
            print(e)
    
    return inttxt
 
#Funciones crud#
#Crear cuenta y crear cliente#
def crearuser():
    action = False
    try:
        while not action:
            currentUser = User()
            archivo = open(account_client, "a")
            print("-------------------------")
            print("Creando Cliente")
            print("-------------------------")
            print("Digite el usuario: ")
            currentUser.userName = input()
            print("Digite la contrasena: ")
            currentUser.passw = input()
            if validUserName(currentUser.userName, currentUser.passw):
                print("Error usuario y contrasena ya han sido registrados")
                action = False
            else:
                print("Digite la cedula: ")
                currentUser.id = pedirNumeroEntero()
                if validarIdentCliente(currentUser.id):
                    print("El cliente ya esta registrado")
                    action = False
                else:
                    print("Digite el nombre: ")
                    currentUser.name = input()
                    print("Digite el apellido: ")
                    currentUser.lastname = input()
                    action = True
                    archivo = open(account_client, "a")
                    archivo.write("\n"+currentUser.userName+","+currentUser.passw+","+str(currentUser.id)+","+currentUser.name+","+currentUser.lastname) 
            archivo.close()
        #return action
    except Exception as e:
        print(e)

def crearaccount():    
    try:
        currentAccount = Account()
        print("-------------------------")
        print("Creando Cuenta")
        print("-------------------------")
        print("Digite el numero de cedula: ")
        currentAccount.iden = pedirNumeroEntero()
        if not validarIdentCliente(currentAccount.iden):
          print("El usuario no esta registrado como cliente")
        else:
            print("Digite el numero de cuenta: ")
            currentAccount.num_account = input()
            print("Digite el saldo inicial de la cuenta: ")
            currentAccount.balance = pedirNumeroEntero()
            action = True
            if not validar_archivo(account_file):
                archivo = open(account_file, "w")
                print("Desea agregar una segunda cuenta: 1 (Si) * (No)")
                entrada = input()
                if entrada == "1":
                    print("Digite el numero de cuenta #2: ")
                    currentAccount.num_account2 = input()
                    print("Digite el saldo inicial de cuenta #2: ")
                    currentAccount.balance2  = pedirNumeroEntero()
                archivo.write(str(currentAccount.iden)+","+currentAccount.num_account+","+str(currentAccount.balance)+","+currentAccount.num_account2+","+str(currentAccount.balance2))      
            else:
                if validarIdentCuenta(currentAccount.iden):
                    print("El usuario ya posee una o mas cuentas")
                    action = False
                else:
                    archivo = open(account_file, "a")
                    print("Desea agregar una segunda cuenta: 1 (Si) * (No)")
                    entrada = input()
                    if entrada == "1":
                        print("Digite el numero de cuenta #2: ")
                        currentAccount.num_account2 = input()
                        print("Digite el saldo inicial de cuenta #2: ")
                        currentAccount.balance2  = pedirNumeroEntero()
                    archivo.write("\n"+str(currentAccount.iden)+","+currentAccount.num_account+","+str(currentAccount.balance)+","+currentAccount.num_account2+","+str(currentAccount.balance2))   
            return action
    except Exception as e:
            print(e) 
 

def validar_archivo(archivo):
    return path.exists(archivo)

def validarIdentCuenta(ident):
    inttxt = False
    try:
        archivo = open(account_file, "r")
        for linea in archivo:
            txt = linea
            x = txt.split(",")
            cedula = x[0]
            if (cedula == str(ident)):
                inttxt = True
                break
            
        archivo.close()
        
    except Exception as e:
            print(e) 
    
    return inttxt

def validarIdentCliente(ident):
    inttxt = False
    try:
        archivo = open(account_client, "r")
        for linea in archivo:
            txt = linea
            x = txt.split(",")
            id = x[2]
            if (id == str(ident)):
                inttxt = True
                break
            
        archivo.close()
        
    except Exception as e:
            print(e) 
    
    return inttxt

def validarNumAccount1(num1):
    inttxt = False
    try:
        archivo = open(account_file, "r")
        for linea in archivo:
            txt = linea
            x = txt.split(",")
            account1 = x[1]
            
            if (account1 == str(num1)):
                inttxt = True
                break
            
        archivo.close()
    except Exception as e:
            print(e)  
    
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
            replaceUser(updateUser)
    except Exception as e:
        print(e)
            
def replaceUser(updateUser):
    #archivo = open(account_client, "r")
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(account_client) as old_file:
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
    remove(account_client)
    #Move new file
    move(abs_path, account_client)
    #archivo.close()

def modiaccount():
    
    try:
        updateAccount = Account()
        print("-------------------------")
        print("Modificando cuenta")
        print("-------------------------\n")
        print("Digite el numero de cedula: ")
        updateAccount.iden = input()
        if not validarIdentCuenta(updateAccount.iden):
            print("El cliente no existe")
        else:
            print("Digite el numero de la cuenta ")
            updateAccount.num_account = input()
            print("Digite el saldo: ")
            updateAccount.balance = input()
            print("Digite el nombre de la cuenta: ")
            updateAccount.num_account2 = input()
            print("Digite el saldo: ")
            updateAccount.balance2 = input()
            replaceAccount(updateAccount)
    except Exception as e:
        print(e)
           
def replaceAccount(updateAccount):
    #archivo = open(account_client, "r")
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(account_file) as old_file:
            for line in old_file:
                txt = line
                x = txt.split(",")
                id = x[0]
                if (id == updateAccount.iden):
                    newline =updateAccount.iden+","+updateAccount.num_account+","+updateAccount.balance+","+updateAccount.num_account2+","+updateAccount.balance2
                    new_file.write(newline+"\n")
                else:
                    new_file.write(line)
    close(fh)
    #Remove original file
    remove(account_file)
    #Move new file
    move(abs_path, account_file)
    #archivo.close()

#Eliminar cleinte y cuenta

def borrarcliente(ident):
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(account_client) as old_file:
            for line in old_file:
                txt = line
                x = txt.split(",")
                id = x[2]
                if (id != ident):
                   new_file.write(line)
                    
    close(fh)
    #Remove original file
    remove(account_client)
    #Move new file
    move(abs_path, account_client)
    #archivo.close()

def borrarcuenta(ident):
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(account_file) as old_file:
            for line in old_file:
                txt = line
                x = txt.split(",")
                id = x[0]
                if (id != ident):
                   new_file.write(line)
                    
    close(fh)
    #Remove original file
    remove(account_file)
    #Move new file
    move(abs_path, account_file)
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
            borrarcliente(ident)
        
        
    except Exception as e:
        print(e)

def eliminarCuenta():
    try:
        
        print("-------------------------")
        print("Elimando cuenta")
        print("-------------------------\n")
        print("Digite el numero de cedula: ")
        ident = input()
        if not validarIdentCuenta(ident):
            print("El cliente no existe")
        else:
            borrarcuenta(ident)
        
        
    except Exception as e:
        print(e)
        
def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input(""))
            correcto=True
        except ValueError:
            print("Error, digite numeros enteros\nDigite el numero de cedula:")
     
    return num