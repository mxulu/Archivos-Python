#IF-ELSE de una línea
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
    print("no fue un número par")


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
