#Estructuras Repetitivas
#While
Num=int(input("Ingrese número para factorial:"))
Factorial=0
i=1
while(i<=Num):
    Factorial+=1
    i+=1
print(Factorial)

#Ejemplo while, conteo de dígitos
Num1=int(input("Ingrese el número a operar:"))
conteodigitos=0
numero=Num1
while(numero!=0):
    conteodigitos+=1
    numero=numero//10   # // Haciendo división pero solo almacena el divisor entero
print("El número:",Num1,"tiene los siguientes dígitos:",conteodigitos)

#For
#Conteo de número pares e impares
Num1=int(input("Ingrese un número entero:"))
Listado=list(range(1,Num1+1))
ContadorPares=0
ContadorImpares=0
for i in Listado:
    if (i%2==0):    # % Devuelve residuo
        ContadorPares+=1
    elif (i%3==0):
        ContadorImpares+=1
print("El conteo de números pares es:",ContadorPares)
print("El conteo de números impares es:",ContadorImpares)

#For y while anidado
#Ejemplo ciclo anidado
Num1=int(input("Ingrese el número a operar:"))
for i in range(1,Num1+1):
    for y in range(1,i+1):
        print(y,end=" ")
    print("")

#Comandos break y else
#Ejemplo de números primos
Num1=int(input("Ingrese el primer número entero:"))
Num2=int(input("Ingrese el segundo número entero:"))
for i in range(Num1,Num2+1):
    for x in range(2,i):
        if (i%x==0):
            break
    else:
        print("Encontré el número primo:",i)

#Ejercicio Sucesión de Fibonacci
Num1=int(input("Ingrese el número final de la serie Fibonacci:"))
if(Num1<2):
    print("Por favor ingrese un número mayor a 2")
    exit()
x=0
y=1
print(x, end=" ")
print(y, end=" ")
z=x+y
for i in range(3,Num1+1):
    z=x+y
    print(z, end=" ")
    x=y
    y=z

#Planteamiento no recursivo
Num1=int(input("Ingrese el primer número entero:"))
Suma=0
for i in range(1,Num1+1):
    Suma+=i
print("La suma de los números 1 hasta",Num1,"es de:",Suma)


#Recursividad
Num1=int(input("Ingrese el primer número entero:"))
def SumatoriaRecursiva(Num1):
    if (Num1==1):
        return 1
    else:
        return Num1+SumatoriaRecursiva(Num1-1)

print("La suma de los números 1 hasta",Num1,"es de:",SumatoriaRecursiva(Num1))

#Ejercicio sucesión Fibonacci con Recursividad
Num1=int(input("Ingrese el número final de pasos para la serie Fibonacci:"))
if(Num1<2):
    print("Por favor ingrese un número mayor a 2")
    exit()
x=0
y=1
print(x, end=" ")

def FibonacciRecursivo(PrimerNum, SegundoNum, ConteoSecuencia, límite):
    if (ConteoSecuencia==límite):
        return SegundoNum
    else:
        print(SegundoNum, end=" ")
        return FibonacciRecursivo(SegundoNum, PrimerNum+SegundoNum,ConteoSecuencia+1,límite)

FibonacciRecursivo(x,y,1,Num1)    