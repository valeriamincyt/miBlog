import json
from pandas import DataFrame
import requests
#from django.http import HttpResponseRedirect
import os

def busquedaEnRepoMincyt(sentenciaIngresada, archivoSalida):
  path_desktop = os.environ['USERPROFILE']
  #path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
  print('Ruta usuario: '+  path_desktop)  
  #print("Ingrese la sentencia de búsqueda: ")
  #ingresoUsuario = input()
  lista = sentenciaIngresada.split(" ")
  sentencia =""
  for palabra in lista:
    sentencia = sentencia + '+' + palabra

  #print("Ingrese el nombre del archivo donde quiere guardar el resultado de la búqueda: ")
  #archivoSalida = input()

  resultado = requests.get('https://repositoriosdigitales.mincyt.gob.ar/vufind/api/v1/search?lookfor='+ sentencia +'&type=AllFields&limit=2000').text
  #with open("resultado.txt","a") as archivo:
  #          archivo.write(resultado)
  dict_data = json.loads(resultado)
  if dict_data['resultCount'] > 0:
    df = DataFrame.from_dict(dict_data['records'], orient='columns')
    #df.to_excel(archivoSalida + ".xlsx", index=False)
    #df.to_excel(path_desktop +"\\" +"probandoRuta.xlsx", index=False)
    df.to_excel(path_desktop +"\\" + archivoSalida + ".xlsx", index=False)
    print("Búsqueda finalizada en RepoMincyt.")
    #resultado = archivoSalida + ".xlsx"
    #HttpResponseRedirect.allowed_schemes.append(archivoSalida + ".xlsx")
  else:
    print('0 resultados')
    #resultado = 'buscar/'
  #return HttpResponseRedirect.allowed_schemes.append(resultado)

#busquedaEnRepoMincyt()