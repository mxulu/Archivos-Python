import webbrowser
import requests
import json

#Esta función devuelve la tarea de la semana
def GetHomework(SemanaN,FilePath):
    #Parte 1
    Enlace="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enlace, new=2)
    #Parte 2
    response=requests.get(Enlace).text
    response_info=json.loads(response)
    archivo=open(FilePath, "w")
    json.dump(response_info,archivo,indent=6)
    archivo.close()


InputSemana=input("Ingrese semana:")
InputFile=input("Ingrese path y nombre de archivo:")
GetHomework(InputSemana,InputFile)
