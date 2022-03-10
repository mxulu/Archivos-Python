#IF-ELSE de una línea
from email.errors import MessageError


Num1=int(input("Ingrese número 1:"))
Num2=int(input("Ingrese número 2:"))

print("Los números",Num1,"y",Num2,"son iguales") if(Num1==Num2) else print("Los números",Num1,"son diferentes")


#IF anidados
Num1=int(input("Ingrese número 1:"))
if(Num1%2==0):
    Num2=int(input("Ingrese número2:"))
    if(Num2%2==0):
        print("El resultado de",Num1,"elevado a la potencia",Num2,"es:",Num1**Num2)
    else:
        print("El resultado de",Num1,"dividido",Num2,"es:",Num1/Num2)


#Pass
Num1=int(input("Ingrese número 1:"))
if(Num1%2==0):
    pass
else:
    print(Num1,"No fue un número par")


#Switcher
Num1=int(input("Ingrese número de día de la semana:"))
DiasSemana={
    1:"Lunes",
    2:"Martes",
    3:"Miércoles",
    4:"Jueves",
    5:"Viernes",
    6:"Sábado",
    7:"Domingo",
}

print("El día de la semana para el número",Num1,"es:",DiasSemana.get(Num1,"No es un día de la semana"))



Num1=int(input("Ingrese número del mes:"))
Meses={
    1:"Enero",
    2:"Febrero",
    3:"Marzo",
    4:"Abril",
    5:"Mayo",
    6:"Junio",
    7:"Julio",
    8:"Agosto",
    9:"Septiembre",
    10:"Octubre",
    11:"Noviembre",
    12:"Diciembre",
}

print("El mes número",Num1,"es",Meses.get(Num1,"El número no corresponde a un mes válido"))

#Excepciones
try:
    print("Estoy en el bloque de TRY")
    print(int(input("Número1"))/int(input("Número2")))
except ZeroDivisionError:
    print("Capturé un error de división por cero")
except:
    print("Detecte un error en las líneas anteriores")
else:
    print("No hubieron errores")


#Ejemplo
archivo=open("c:\\Json\\prueba.txt","w")
try:
    archivo.write("Este es el nuevo contenido del archivo")
except:
    print("No se pudo")
else:
    print("archivo modificado exitosamente")
finally:
    archivo.close()
    print("se cerró el arhivo exitosamente")


import os
carpeta="c:\\Json\\Semana3.json"
nombrearchivo=os.path.basename(carpeta)
directorio=os.path.dirname(carpeta)

print(nombrearchivo)
print(directorio)


arch=os.path.exists("c:\\Json\\Semana2.json")
print(arch)








