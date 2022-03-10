#Track - Ciclos Python
#Ejercicio 1
from io import TextIOBase, TextIOWrapper


Num1=int(input("Ingrese un número:"))
x=Num1
while x>=1:
    j=x
    while j>=1:
        if j==1:
            print(j)
        else:
            print(j,end=",")
        j-=1
    x-=1

#Ejercicio 2
Num1=int(input("Ingrese Num1:"))
Elnum=str(Num1)
x=len(Elnum)
for i in range(x-1,-1,-1):
    print(Elnum[i],end="")

#Ejercicio 3
Num1=int(input("Ingrese Num1:"))
i=0
x=0
s1=""
while i<Num1:
    i+=1
    s1=s1+"3"
    if i==Num1:
        print(s1)
    else:
        print(s1, end=" + ")
    x=x+int(s1)
print("La suma total es:",x)

#Ejercicio 4
i=1
s1="* * * * *"
while i<=9:
    print(s1[:i])
    i+=2
i=7
s1="* * * *"
while i>=1:
    print(s1[:i])
    i-=2

#Ejercicio 5
ListaNumeros=[10,20,30,40,50,60,70,80,90,100]
for i in range(1,10,2):
    if i == 9:
        print(ListaNumeros[i])
    else:
        print(ListaNumeros[i],end=",")
for i in range(0,10,2):
    if i == 8:
        print(ListaNumeros[i])
    else:
        print(ListaNumeros[i],end=",")

#Ejercicio 6
Cadena=input("Ingrese Texto:")
x=len(Cadena)
for i in range(x-1,-1,-1):
    print(Cadena[i],end="")

#Ejercicio 7
def Vuelta(Texto):
    x=len(Texto)-1
    if x==0:
        return Texto[x]
    else:
        return Texto[x] + Vuelta(Texto[:x])
Cadena=input("Ingrese Cadena:")
print(Vuelta(Cadena))

