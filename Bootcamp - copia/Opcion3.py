def FunOpcion3():
    texto=input("Ingrese el texto a colocar dentro del archivo:")
    try: 
        archivo=open("Archivo.txt", "w") #Archivo.txt creado en path relativo/actual
        archivo.write(texto)
    except:
        print("Error al abrir el archivo")
    finally:
        try:
            archivo.close()
            print("Archivo.txt abierto, modificado y cerrado exitosamente")
            print("")
        except:
            print("No se pudo cerrar")