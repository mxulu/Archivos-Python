from datetime import datetime


NombrePersona = input("Por favor ingrese su nombre:")
print("Hola, te envío un saludo", NombrePersona, "en la fecha:", datetime.today().strftime("%y-%m-%d"))
