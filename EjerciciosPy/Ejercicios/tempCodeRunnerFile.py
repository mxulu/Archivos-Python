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