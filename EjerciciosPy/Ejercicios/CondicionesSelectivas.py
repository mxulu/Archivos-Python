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
    