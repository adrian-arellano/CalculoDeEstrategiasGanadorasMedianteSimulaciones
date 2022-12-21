# modelo
import numpy as np

from python_files.Estimador import Estimador
from python_files.MonteCarlo import MonteCarlo
from python_files.Partida import Partida


class GPI:
  def __init__(self, juego, separador='&'):
    self.jugador = 0
    self.juego = juego
    self.estimador = Estimador(separador=separador)
    self.partida = Partida(self.estimador.tablero(self.juego.tablero_inicial))

  # simular un turno
  def jugar_turno(self, u, llave_tablero):
    # greedy: se sabe que todas las jugadas viables tienen la misma utilidad
    distribucion = np.array([1] * len(self.estimador.jugadas_viables(llave_tablero)))
    distribucion = distribucion / sum(distribucion)  # estandarizar
    eleccion = MonteCarlo(u, distribucion)

    jugada = self.estimador.jugadas_viables(llave_tablero)[eleccion]

    self.partida.agregar_jugada(self.estimador.tablero(jugada))
    self.jugador = 1 - self.jugador

  # simular resto de una partida
  def simular_partida(self, U, actualizar=False):
    estado_actual = self.partida.tablero_actual().llave
    turno = self.partida.turno_actual()

    # verificar si se puede jugar
    # if len(self.estimador.jugadas_viables(estado_actual)) == 0:
    if not self.estimador.tablero(estado_actual).visitado:

      # guardar que se revisó
      self.estimador.tablero(estado_actual).visitado = True

      # verificar si es porque el jugador anterior ganó
      if self.juego.victorias[1 - self.jugador](estado_actual):
        if actualizar:
          self.estimador.tablero(estado_actual).cambiar_valor(1)
        return

      # intentar actualizar
      jugadas_siguientes = self.juego.reglas[self.jugador](estado_actual)
      self.estimador.agregar_tablero(estado_actual, jugadas_siguientes)

    # si sigue vacio: no se puede seguir jugando
    if len(self.estimador.jugadas_viables(estado_actual)) == 0:
      return

    self.jugar_turno(U[turno], estado_actual)
    self.simular_partida(U, True)  # continuar jugando

  def Iteracion(self, u, U):
    largo_de_la_partida = self.partida.turno_actual()
    perdedor = self.jugador
    if self.partida.tablero_actual().valor < 1:
      # greedy: darle la oportunidad a quien no gana
      perdedor = 1 - perdedor
    lista_jugadas_posibles = []

    # greedy: elegir solo jugadas del perdedor para asegurar que termine en otra partida
    for turno in range(perdedor, largo_de_la_partida + 1, 2):
      llave_tablero_en_turno = self.partida.tablero_en_turno(turno).llave
      lista_jugadas_posibles.append(self.estimador.jugadas_viables(llave_tablero_en_turno))

    # greedy: últimos turnos son más probables
    beta = 1
    distribucion_turno = 1 - np.exp(-beta * (
      np.array([(turno + 1) * len(lista_jugadas_posibles[turno]) for turno in range(len(lista_jugadas_posibles))])))
    # este jugador tiene mejores jugadas
    if sum(distribucion_turno) > 0:
      distribucion_turno = distribucion_turno / sum(distribucion_turno)  # estandarizar
      turno_elegido = perdedor + 2 * MonteCarlo(u, distribucion_turno)
      self.partida.retroceder_antes_del_turno(turno_elegido + 1)
      self.jugador = perdedor
      # print('cambiar:',turno_elegido,'para que juege ',self.jugador)

    # for tablero in self.partida.tableros:
    #  print([tablero.llave],':',tablero.llaves_jugadas_posibles_viables())

    self.simular_partida(U, actualizar=True)

    estado = self.partida.tablero_actual().llave
    # jugador = self.partida.turno_actual()%2

    # if self.juego.victorias[1-jugador]:
    # self.partida.tablero_actual().cambiar_valor(1)
    self.actualizar(estado)

  def actualizar(self, llave):
    lista_por_actualizar = set(self.estimador.tablero(llave).tableros_de_origen)
    while len(lista_por_actualizar) > 0:
      lista_aux = []
      for tablero in lista_por_actualizar:
        # print(tablero.llave,'actualizado')
        tablero.actualizar_tableros_viables()
        lista_aux += tablero.tableros_de_origen
      lista_por_actualizar = set(lista_aux)
