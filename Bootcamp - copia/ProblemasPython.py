from Opcion1 import FunOpcion1
from Opcion2 import FunOpcion2
from Opcion3 import FunOpcion3
from Opcion4 import FunOpcion4

Conteo=0
while(Conteo==0):
    print("Opción #1 - Imprima el día y la hora actual")
    print("Opción #2 - Abra el sitio de www.github.com en una ventana del navegador")
    print("Opción #3 - Guardará en un archivo llamado Archivo.txt en la carpeta actual (path relativo) un texto ingresado por el usuario")
    print("Opción #4 - Salir del programa")
    try:   
        Opcion=int(input("Ingrese una opción del menú:"))    
        if Opcion==1:
            FunOpcion1()
        elif Opcion==2:
            FunOpcion2()
        elif Opcion==3:
            FunOpcion3()
        elif Opcion==4:
            FunOpcion4()
            break
        elif Opcion!="":
            print("Por favor, ingrese un número correspondiente entre 1 y 4")
            print("")
    except:
        print("Por favor, ingrese un valor entero válido")
        print("")




