#Track - Condiciones Python
#Ejercicio1
Vocales="AEIOUaeiou"
Letra=input("Por favor ingrese una letra:")
x=Vocales.find(Letra)
print(x)
if x>=0:
    print(Letra,"es vocal")
else:
    print(Letra,"es consonante")
    
#Ejercicio2
N1=input("Ingrese el número 1:")
N2=input("Ingrese el número 2:")
N3=input("Ingrese el número 3:")
if N1==N2==N3:
    print("El triángulo es equilatero")
elif N1==N2 or N2==N3 or N1==N3:
    print("El triángulo es isóceles")
else:
    print("El triángulo es escaleno")

#Ejercicio3
NotaAlumno=int(input("Ingrese la nota del alumno:"))
print("El estudiante aprobó con una nota de "+str(NotaAlumno) if NotaAlumno>=65 else "El estudiante reprobó con una nota de "+str(NotaAlumno))

#Ejercicio4
def DarMes(Mes):
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
    return Meses.get(Mes,"")
Num1=int(input("Ingrese número del mes:"))
Validacion=DarMes(Num1)
if Validacion!="":
    print("El mes {0} es {1}".format(Num1,Validacion))
else:
    print("El número no corresponde a un mes válido")

#Ejercicio5
AñoIngresado=int(input("Ingrese Año:"))
if AñoIngresado<1582:
    print("El año ingresado es anterior al calendario gregoriano")
else:
    if ((AñoIngresado%100==0) and (AñoIngresado % 400 == 0)):
        print("El año {0} es bisiesto".format(AñoIngresado))
    elif ((AñoIngresado%100!=0) and (AñoIngresado%4==0)):
        print("El año {0} es bisiesto".format(AñoIngresado))  
    else:
        print("El año {0} NO es bisiesto".format(AñoIngresado))


