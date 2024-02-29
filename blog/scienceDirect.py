import requests
import json
#from pandas import DataFrame, concat
import pandas
from django.http import HttpResponseRedirect

def busquedaEnScienceDirect(sentenciaIngresada, archivoSalida):
  #print("Ingrese la sentencia de búsqueda sin acentos: ")
  #ingresoUsuario = input()
  lista = sentenciaIngresada.split(" ")
  sentencia =""
  for palabra in lista:
    sentencia = sentencia + '+' + palabra
  #print("Ingrese el nombre del archivo donde quiere guardar el resultado de la búqueda: ")
  #archivoSalida = input()
  dfAcum = pandas.DataFrame()
  #body = '{"qs": "inteligencia+artificial","display": {"offset": 0,"show": 10,"sortBy": "relevance"}}'
  body = '{"qs": "'+ sentencia +'","display": {"offset": 0,"show": 10,"sortBy": "relevance"}}'
  #print(body)
  resultado = requests.put('https://api.elsevier.com/content/search/sciencedirect', body, headers={"x-els-apikey":"7f59af901d2d86f78a1fd60c1bf9426a"}).text
  print(resultado)
  dict_data = json.loads(resultado)
  print(dict_data.keys())
  cantidadDeResultados = int(dict_data['resultsFound'])
  cantidadDeResultados = cantidadDeResultados + 1
  for i in range(0,cantidadDeResultados, 100):
    #body = '{"qs": "inteligencia+artificial","display": {"offset": '+str(i)+',"show": '+str(100)+',"sortBy": "relevance"}}'
    body = '{"qs": "'+ sentencia +'","display": {"offset": '+str(i)+',"show": '+str(100)+',"sortBy": "relevance"}}'
    #print(body)
    resultado = requests.put('https://api.elsevier.com/content/search/sciencedirect', body, headers={"x-els-apikey":"f2f2d6b3d5be1de776a6d4f2ba68203c"}).text
    #print(resultado)
    dict_data = json.loads(resultado)
    df = pandas.DataFrame.from_dict(dict_data['results'], orient='columns')
    frames = [dfAcum, df]
    dfAcum = pandas.concat(frames)
  dfAcum.to_excel(archivoSalida + ".xlsx",  index=False)
  print("Búsqueda finalizada.")
  HttpResponseRedirect(archivoSalida + ".xlsx")