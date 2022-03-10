def Vuelta(Texto):
    x=len(Texto)-1
    if x==0:
        return Texto[x]
    else:
        return Texto[x] + Vuelta(Texto[x])
Cadena=input("Ingrese Cadena:")
print(Vuelta(Cadena))