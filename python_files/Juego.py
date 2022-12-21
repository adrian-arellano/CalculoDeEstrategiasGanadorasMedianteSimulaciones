import numpy as np

### funcion de interfaz

def jugada_a_llave(columnas,filas,tablero,jugada):
  if len(tablero)!= filas*columnas:
    return ''
  try:
    y = int(jugada[:jugada.find(',')])-1
  except:
    return ''
  if y < 0 or y >= filas:
    return ''
  try:
    x = int(jugada[jugada.find(',')+1:jugada.find(',',jugada.find(',')+1)])-1
  except:
    return ''
  if x < 0 or x >= columnas:
    return ''
  return tablero[:columnas*y+x]+jugada[-1]+tablero[columnas*y+x+1:]

### test llaves de jugadas

assert jugada_a_llave(3,1,'   ','1,1,1') == '1  '
assert jugada_a_llave(4,3,' '*12,'2,3,1') == '      1     '

class Juego:
  def __init__(self, columnas=1, filas=1, llave_tablero_inicial=' '):
    self.palabra_segura = 'x'  # desuso
    self.conocimiento = {}  # desuso
    self.tablero_inicial = llave_tablero_inicial
    self.columnas = columnas
    self.filas = filas
    self.reglas = [lambda x: [], lambda x: []]
    self.victorias = [lambda x: True, lambda x: True]
    self.reiniciar()

  # reiniciar juego
  def reiniciar(self):
    self.jugador = 0  # desuso
    self.partida = [self.tablero_inicial]  # desuso
    self.llaves_jugadas_posibles = self.reglas[0](self.tablero_inicial)  # desuso

  # redefinir palabra segura (desuso)
  def cambiar_palabra_segura(self, palabra):
    self.palabra_segura = palabra

  # redefenir tamaño
  def cambiar_tablero(self, columnas, filas, llave_tablero_inicial):
    self.filas = filas
    self.columnas = columnas
    self.tablero_inicial = llave_tablero_inicial
    self.reiniciar()

  # redefinir reglas J1
  def cambiar_reglasJ1(self, regla):
    self.reglas = [regla] + self.reglas[1:]

  # redefinir reglas J2
  def cambiar_reglasJ2(self, regla):
    self.reglas = self.reglas[:1] + [regla]

  # redefinir condicion de victoria J1
  def cambiar_victoriaJ1(self, con_victoria):
    self.victorias = [con_victoria] + self.victorias[1:]

  # redefinir condicion de victoria J2
  def cambiar_victoriaJ2(self, con_victoria):
    self.victorias = self.victorias[:1] + [con_victoria]

  # saber si el juego acabo (desuso)
  def condicion_de_victoria(self):
    return self.victorias[1 - self.jugador](self.llave_tablero_actual())

  # guardar "i.a." (desuso)
  def agregar_conocimiento(self, conocimiento):
    self.conocimiento.update(conocimiento)

  # probabilidad (desuso)
  def conocimiento_tablero(self, llave):
    if not llave in self.conocimiento:
      return 0.5
    return self.conocimiento[llave]

  # acceder a turno actual (desuso)
  def llave_tablero_actual(self):
    return self.partida[-1]

  # redefinir turno (desuso)
  def retroceder_antes_del_turno(self, n):
    self.partida = self.partida[:n]
    self.jugador = n % 2 - 1
    self.llaves_jugadas_posibles = self.reglas[self.jugador](self.llave_tablero_actual())

    # agregar jugada (desuso)

  def agregar_jugada_manual(self, tablero_siguiente, llaves_tableros_siguientes):
    self.partida = self.partida + [tablero_siguiente]
    self.llaves_jugadas_posibles = llaves_tableros_siguientes
    self.jugador = 1 - self.jugador

    # avanzar en juego (desuso)

  def agregar_jugada_jugador(self, jugada):
    llave = jugada_a_llave(self.columnas, self.filas, self.llave_tablero_actual(), jugada)
    # print('jugada:',[llave])

    if llave in self.llaves_jugadas_posibles:  # checkear si es una jugada permitida
      self.partida = self.partida + [llave]  # agregar jugada a la partida
      self.jugador = 1 - self.jugador  # actualizar turno
      self.llaves_jugadas_posibles = self.reglas[self.jugador](llave)  # actualizar jugadas siguientes

  # juega "i.a." (desuso)
  def agregar_jugada_modelo(self, determinista=False):
    if len(self.llaves_jugadas_posibles) == 0:
      return
    jugada_siguiente = self.llaves_jugadas_posibles[0]  # iniciarlizado

    if determinista:  # juega la mejor jugada posible
      valor_aux = 0
      for llave in self.llaves_jugadas_posibles:
        valor_actual_aux = self.conocimiento_tablero(llave)
        if valor_actual_aux > valor_aux:  # checkear si es mejor de lo que ya tiene
          valor_aux = valor_actual_aux
          jugada_siguiente = llave
    else:  # elegir al azar
      u = np.random.random_sample()  # jugada
      u = u * sum([self.conocimiento_tablero(llave) for llave in self.llaves_jugadas_posibles])
      valor_aux = 0
      for llave in self.llaves_jugadas_posibles:  # invariante de entrada al loop: ninguna llave previa es la jugada seleccionada
        valor_aux += self.conocimiento_tablero(llave)
        if valor_aux > u:  # checkear si esta es la que salio sorteada
          jugada_siguiente = llave
          break

    self.partida = self.partida + [jugada_siguiente]
    self.jugador = 1 - self.jugador
    self.llaves_jugadas_posibles = self.reglas[self.jugador](jugada_siguiente)

  def jugar_turno(self, determinista=True):
    if self.condicion_de_victoria():
      print('partida finalizada')
      return
    jugador_aux = self.jugador
    while jugador_aux == self.jugador:
      jugada = input('jugada: ')
      if jugada == '':
        self.agregar_jugada_modelo(determinista)
        return
      if jugada == self.palabra_segura:
        print('partida suspendida')
        return
      self.agregar_jugada_jugador(jugada)

  def tablero_actual(self):
    # tablero = np.ndarray(shape=(self.filas,self.columnas),dtype=str)
    # for x in range(self.columnas):
    #  for y in range(self.filas):
    #    tablero[y,x] = self.llave_tablero_actual()[y*self.columnas + x]
    tablero = np.array(list(self.llave_tablero_actual())).reshape(self.filas, self.columnas)
    return tablero