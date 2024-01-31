import json
from pandas import DataFrame
import requests


def busquedaEnRepoMincyt(sentenciaIngresada, archivoSalida):
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
    df.to_excel(archivoSalida + ".xlsx", index=False)
    print("Búsqueda finalizada.")
  else:
    print('0 resultados')

#busquedaEnRepoMincyt()