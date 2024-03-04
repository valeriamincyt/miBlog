import json
from pandas import DataFrame
import requests
import os
#from django.http import FileResponse
from django.http import HttpResponseRedirect

def busquedaEnRepoMincyt(sentenciaIngresada):
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
  filepath = BASE_DIR + '/blog/archivos/' + 'busqueda.xlsx'
  lista = sentenciaIngresada.split(" ")
  sentencia =""
  for palabra in lista:
    sentencia = sentencia + '+' + palabra
  resultado = requests.get('https://repositoriosdigitales.mincyt.gob.ar/vufind/api/v1/search?lookfor='+ sentencia +'&type=AllFields&limit=2000').text
  #with open("resultado.txt","a") as archivo:
  #          archivo.write(resultado)
  dict_data = json.loads(resultado)
  if dict_data['resultCount'] > 0:
    df = DataFrame.from_dict(dict_data['records'], orient='columns')
    #df.to_excel(archivoSalida + ".xlsx", index=False)
    df.to_excel(filepath, index=False) #uso local
    print("Búsqueda finalizada en RepoMincyt.")
  else:
    print('0 resultados')
    resultado = 'buscar/'
  return HttpResponseRedirect.allowed_schemes.append(resultado)

#busquedaEnRepoMincyt()