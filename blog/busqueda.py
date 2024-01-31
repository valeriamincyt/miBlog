from .scienceDirect import busquedaEnScienceDirect
from .repoMincyt import busquedaEnRepoMincyt

def buscar(fuente, sentencia,archivoSalida):
  menu = """Ingrese el número de la fuente donde quiere buscar:
  1 - Repositorio Digital del Mincyt
  2 - Science Direct
  """
  #opcion = int(input(menu)) 
  #print("Indique la fuente donde desea buscar:")
  print(fuente)
  print(type(fuente))
  if  fuente == '1':
      busquedaEnRepoMincyt(sentencia,archivoSalida)
  elif fuente == '2':
      busquedaEnScienceDirect(sentencia,archivoSalida)
  else:
      print('Opcion inválida')

#buscar()