# oraculo de reglas
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from python_files.GPI import GPI
from python_files.Interfaz import graficar_red
from python_files.Juego import Juego


def ReglasTab42(llave):
  jugadas_posibles = []
  for indice in range(len(llave)):
    if llave[indice] != ' ':
      continue
    jugadas_posibles.append(llave[:indice]+'1'+llave[indice+1:])
    jugadas_posibles.append(llave[:indice]+'2'+llave[indice+1:])
  return jugadas_posibles

# oraculo de condicion de victoria
def CondicionVictoriaTab42(llave):
  total = sum([int(i) for i in llave if i != ' '])
  return total == 4




Tab42 = Juego(3,1,' '*3)
Tab42.cambiar_reglasJ1(ReglasTab42)
Tab42.cambiar_reglasJ2(ReglasTab42)
Tab42.cambiar_victoriaJ1(CondicionVictoriaTab42)
Tab42.cambiar_victoriaJ2(CondicionVictoriaTab42)

Demo1 = GPI(Tab42)





def AnimacionRed(frame):
  graficar_red(Demo1.estimador,Demo1.partida)
  Demo1.Iteracion(u[frame],U[frame])

  n = 10
  np.random.seed(42)
  U = np.random.rand(n, 3)
  u = np.random.rand(n)

  FigTab42 = plt.Figure()
  animacionTab42 = FuncAnimation(FigTab42, AnimacionRed, frames=n, interval=100)

  # video = animacionTab42.to_html5_video()
  # html = display.HTML(video)
  # display.display(html)
  # plt.show()
  # good practice to close the plt object.
  # plt.close()
  plt.show()
