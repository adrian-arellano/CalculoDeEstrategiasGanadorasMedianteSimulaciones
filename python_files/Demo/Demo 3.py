# oraculo de reglas
import numpy as np

from python_files.GPI import GPI
from python_files.Juego import Juego


def ReglasABC(llave):
  jugadas_posibles = []
  for indice in range(len(llave)):
    if llave[indice] != ' ':
      continue
    jugadas_posibles.append(llave[:indice] + 'A' + llave[indice + 1:])
    jugadas_posibles.append(llave[:indice] + 'B' + llave[indice + 1:])
    jugadas_posibles.append(llave[:indice] + 'C' + llave[indice + 1:])
  return jugadas_posibles


# oraculo de condicion de victoria
def CondicionVictoriaABC(llave):
  # horizontal
  for fila in range(5):
    for columna in range(3):
      palabra = llave[5 * fila + columna:5 * fila + columna + 3]
      if 'A' in palabra:
        if 'B' in palabra:
          if 'C' in palabra:
            return True

  # vertical
  for columna in range(5):
    for fila in range(3):
      palabra = llave[5 * fila + columna] + llave[5 * (fila + 1) + columna] + llave[5 * (fila + 2) + columna]
      if 'A' in palabra:
        if 'B' in palabra:
          if 'C' in palabra:
            return True

  return False


ABC = Juego(5, 5, ' ' * 25)
ABC.cambiar_reglasJ1(ReglasABC)
ABC.cambiar_reglasJ2(ReglasABC)
ABC.cambiar_victoriaJ1(CondicionVictoriaABC)
ABC.cambiar_victoriaJ2(CondicionVictoriaABC)

Demo3 = GPI(ABC)

n = 50000
np.random.seed(123456)
U = np.random.rand(n, 25)
u = np.random.rand(n)

for i in range(n):
  Demo3.Iteracion(u[i], U[i])

print(len(Demo3.estimador.tableros))
