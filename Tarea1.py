from clases import *
from funciones import *
from menu import *

def main():
    loop = False
    miLogin = Login()

    while loop == False:
     if logueo(miLogin):
        menu(miLogin)
        loop = True
     else:
       loop = False
       
     
if __name__ == "__main__":
    main()