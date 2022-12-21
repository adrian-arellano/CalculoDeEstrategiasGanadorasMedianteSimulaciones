import matplotlib.pyplot as plt

def niveles_tableros(estimador, llave_casilla_vacia=' '):
  niveles = {}

  # guardar niveles de red
  for llave in estimador.tableros:
    nivel = len(llave) - llave.count(llave_casilla_vacia)
    if nivel not in niveles:
      niveles[nivel] = []
    niveles[nivel] = niveles[nivel] + [llave]

  return niveles


def coordenadas_nodos(niveles):
  coords = []
  for nivel in niveles:
    n = len(niveles[nivel])
    h = 1 / n
    coords.append([[nivel] * n, [1 - h * i for i in range(n)]])

  return coords


def graficar_red(max_niveles, estimador, partida=None, llave_casilla_vacia=' ', scale=1, colores=['y', 'g', 'r']):
  niveles = niveles_tableros(estimador, llave_casilla_vacia)
  coords = coordenadas_nodos(niveles)

  # fig = plt.figure(figsize=(3*scale,max_niveles*2*scale))
  ejes = plt.gca()

  # conexiones
  for nivel in range(max_niveles, -1, -1):
    if nivel not in niveles:
      continue
    for llave in niveles[nivel]:
      estimador.actualizar_tableros_viables(llave, True)

  for nivel in niveles:
    for llave in niveles[nivel]:
      for vecino in estimador.jugadas_viables(llave):
        nivel_vecino = len(vecino) - vecino.count(llave_casilla_vacia)
        plt.plot(
          [coords[nivel][1][niveles[nivel].index(llave)], coords[nivel_vecino][1][niveles[nivel_vecino].index(vecino)]],
          [-nivel, -nivel_vecino],
          color='black')

  # nodos
  for nivel in range(len(coords)):
    for nodo in range(len(coords[nivel][0])):
      # no testeado
      if not estimador.tablero(niveles[nivel][nodo]).visitado:
        ejes.scatter(coords[nivel][1][nodo],
                     -coords[nivel][0][nodo],
                     s=[50],
                     # color=colores[int(2*estimador.valor(niveles[nivel][nodo]))-1],
                     color='black',
                     zorder=5)
        continue
      ejes.scatter(coords[nivel][1][nodo],
                   -coords[nivel][0][nodo],
                   s=[100],
                   # color=colores[int(2*estimador.valor(niveles[nivel][nodo]))-1],
                   color=colores[estimador.valor(niveles[nivel][nodo])],
                   zorder=5)

  # destacar partida
  if partida != None:
    nivel_actual = len(partida.tablero_en_turno(0).llave) - partida.tablero_en_turno(0).llave.count(llave_casilla_vacia)
    for i in range(1, len(partida.tableros)):
      nivel_siguiente = len(partida.tablero_en_turno(i).llave) - partida.tablero_en_turno(i).llave.count(
        llave_casilla_vacia)
      plt.plot([coords[nivel_actual][1][niveles[nivel_actual].index(partida.tablero_en_turno(i - 1).llave)],
                coords[nivel_siguiente][1][niveles[nivel_siguiente].index(partida.tablero_en_turno(i).llave)]],
               [-nivel_actual, -nivel_siguiente],
               color='purple',
               linewidth=3)
      nivel_actual = nivel_siguiente


def llave_a_arreglo(n, m, llave):
  return [list(llave[i * m:(i + 1) * m]) for i in range(n)]


def graficar_tablero(n, m, llave, scale=1, font=1, xscale=1, yscale=1):
  # tipear arreglo llave
  arreglo = llave_a_arreglo(n, m, llave)

  fig = plt.figure(figsize=(n, m))
  ejes = plt.gca()
  # _,ejes = plt.subplots()
  # fig.patch.set_visible(False)
  ejes.axis('off')
  ejes.axis('tight')
  tablero = ejes.table(cellText=arreglo,
                       loc='center',
                       colWidths=[0.12] * m,
                       cellLoc='center')

  # fig.tight_layout()
  tablero.auto_set_font_size(False)
  tablero.set_fontsize(20 * font * scale)
  tablero.scale(1 * scale * xscale, 2.5 * scale * yscale)

# Bibliografia
# -sintaxis tabla: https://www.geeksforgeeks.org/how-to-create-a-table-with-matplotlib/
# -reajuste de escala tabla: https://stackoverflow.com/questions/15514005/how-to-change-the-tables-fontsize-with-matplotlib-pyplot
# -ajuste texto en celdas : https://stackoverflow.com/questions/25896964/centered-text-in-matplotlib-tables
# -documentacion: https://matplotlib.org/stable/api/table_api.html