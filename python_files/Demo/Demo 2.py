# oraculo de reglas
import numpy as np
from matplotlib import pyplot as plt

from python_files.GPI import GPI
from python_files.Interfaz import graficar_red
from python_files.Juego import Juego


def ReglasGato(llave,ficha):
  jugadas_posibles = []
  # regla: pone una "ficha" en cualquier casilla vacia
  for indice in range(len(llave)):
    if llave[indice] != ' ':
      continue
    jugadas_posibles.append(llave[:indice]+ficha+llave[indice+1:])
  return jugadas_posibles

# reglas jugador 1
def ReglasGatoJugador1(llave):
  return ReglasGato(llave,'x')

# reglas jugador 2
def ReglasGatoJugador2(llave):
  return ReglasGato(llave,'o')


# oraculo condicion de victoria
def CondicionVictoriaGato(llave,palabra):
  # gana cuando: forma una palabra en una de las siguientes lineas

  # lineas horizontales
  for fila in range(3):
    if llave[fila*3:(fila+1)*3] == palabra:
      return True

  # lineas verticales
  for columna in range(3):
    if llave[columna]+llave[columna+3]+llave[columna+6] == palabra:
      return True

  # lineas diagonales
  if llave[0]+llave[4]+llave[8] == palabra:
    return True

  if llave[2]+llave[4]+llave[6] == palabra:
    return True

  # no hay condicion de victoria
  return False

# condicion de victoria jugador 1
def CondicionVictoriaGatoJ1(llave):
    return CondicionVictoriaGato(llave,'xxx')

# condicion de victoria jugador 2
def CondicionVictoriaGatoJ2(llave):
    return CondicionVictoriaGato(llave,'ooo')









Gato = Juego(3,3,' '*9)
Gato.cambiar_reglasJ1(ReglasGatoJugador1)
Gato.cambiar_reglasJ2(ReglasGatoJugador2)
Gato.cambiar_victoriaJ1(CondicionVictoriaGatoJ1)
Gato.cambiar_victoriaJ2(CondicionVictoriaGatoJ2)

figGato = {}

Demo2 = GPI(Gato)







n = 1
np.random.seed(1)
U = np.random.rand(n,10)
u = np.random.rand(n)

for i in range(n):
  Demo2.Iteracion(u[i],U[i])





figGato[1] = plt.figure(figsize=(7,18))
graficar_red(9,Demo2.estimador,Demo2.partida)
plt.show()






n = 9
np.random.seed(12)
U = np.random.rand(n,9)
u = np.random.rand(n)

for i in range(n):
  Demo2.Iteracion(u[i],U[i])

  figGato[2] = plt.figure(figsize=(7, 18))
  graficar_red(9, Demo2.estimador, Demo2.partida)
  plt.show()



figGato[2] = plt.figure(figsize=(7,18))
graficar_red(9,Demo2.estimador,Demo2.partida)
plt.show()




n = 90
np.random.seed(123)
U = np.random.rand(n,9)
u = np.random.rand(n)

for i in range(n):
  Demo2.Iteracion(u[i],U[i])



figGato[3] = plt.figure(figsize=(7,18))
graficar_red(9,Demo2.estimador)
plt.show()




n = 900
np.random.seed(1234)
U = np.random.rand(n,9)
u = np.random.rand(n)

for i in range(n):
  Demo2.Iteracion(u[i],U[i])



figGato[4] = plt.figure(figsize=(7,18))
graficar_red(9,Demo2.estimador)




estimador_gato_backtracking = {}
estimador_gato_backtracking[' '*9] = [0, False, Gato.reglas[0](' '*9)]

def BackTracking(juego,estimador,llave,jugador):
  if ' ' not in llave:
    if estimador[llave][1]:
      estimador[llave] = [1]+estimador[llave][1:]
      return
    estimador[llave] = [0,True,[]]
    return

  if estimador[llave][1]:
    estimador[llave] = [1]+estimador[llave][1:]
    return

  for siguiente in estimador[llave][2]:
    aux = -1
    if siguiente not in estimador:
      estimador[siguiente] = [0,juego.victorias[jugador](siguiente),juego.reglas[1-jugador](siguiente)]
      BackTracking(juego,estimador,siguiente,1-jugador)
    aux = max(aux,estimador[siguiente][0])
  estimador[llave] = [-aux]+estimador[llave][1:]


BackTracking(Gato,estimador_gato_backtracking,' '*9,0)



total_tableros_gato = len(estimador_gato_backtracking)
total_tableros_hoja_gato = len([llave for llave in estimador_gato_backtracking if estimador_gato_backtracking[llave][1]==True])
tableros_visitados_gato = [llave for llave in Demo2.estimador.tableros if Demo2.estimador.tablero(llave).visitado]
total_tableros_visitados_gato = len(tableros_visitados_gato)
lista_auxiliar = [llave for llave in tableros_visitados_gato if len(Demo2.estimador.jugadas_viables(llave))==0]
total_tableros_hoja_visitados_gato = len(lista_auxiliar)
#for llave in lista_auxiliar:
#  if ' ' not in llave:
#    tableros_hoja_visitados_gato+= 1
#    continue
#  jugador = len([i for i in llave if i==' '])%2
#  if Gato.victorias[jugador](llave):
#    tableros_hoja_visitados_gato+= 1

print('cantidad total de hojas:',total_tableros_hoja_gato)
print('cantidad de hojas visitadas:',total_tableros_hoja_visitados_gato)
print('proporcion:',total_tableros_hoja_visitados_gato/total_tableros_hoja_gato)
print('cantidad total de tableros:',total_tableros_gato)
print('cantidad de tableros visitados:',total_tableros_visitados_gato)
print('proporcion:',total_tableros_visitados_gato/total_tableros_gato)