from .scienceDirect import busquedaEnScienceDirect
from .repoMincyt import busquedaEnRepoMincyt

def buscar(fuente, sentencia):
  menu = """Ingrese el número de la fuente donde quiere buscar:
  1 - Repositorio Digital del Mincyt
  2 - Science Direct
  """
  print('Fuente elegida: ' + fuente)
  print(type(fuente))
  if  fuente == '1':
      busquedaEnRepoMincyt(sentencia)
  elif fuente == '2':
      busquedaEnScienceDirect(sentencia)
  else:
      print('Opcion inválida')

#buscar()