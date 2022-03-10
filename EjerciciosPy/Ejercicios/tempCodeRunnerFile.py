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