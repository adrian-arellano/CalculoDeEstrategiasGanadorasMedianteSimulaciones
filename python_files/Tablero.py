# guardar las posibles jugadas dado un tablero
class Tablero:
  def __init__(self, llave_tablero, tableros_siguientes_posibles=[]):
    self.llave = llave_tablero
    self.tableros_de_origen = []
    self.jugadas_posibles = list(tableros_siguientes_posibles)
    for tablero in tableros_siguientes_posibles:
      tablero.tableros_de_origen.append(self)
    self.valor = 0
    # self.valor = 0.5
    self.visitado = False  # no testeado
    self.actualizar_tableros_viables()

  # guardar viabilidad
  def actualizar_tableros_viables(self, actualizar_valores=False):
    jugadas_posibles_aux = []
    valor_aux = -1
    # valor_aux = 0

    # checkear las mejores jugadas
    for T in self.jugadas_posibles:
      if T.valor < valor_aux:
        continue
      if T.valor > valor_aux:
        jugadas_posibles_aux = []
        valor_aux = T.valor
      jugadas_posibles_aux.append(T)

    self.jugadas_posibles_viables = jugadas_posibles_aux

    if len(jugadas_posibles_aux) == 0:
      return
    if actualizar_valores:
      self.valor = -valor_aux
      # self.valor = 1.0-valor_aux

  # guardar puntaje
  def actualizar_valor(self):
    if len(self.jugadas_posibles_viables) == 0:
      return
    self.valor = -self.jugadas_posibles_viables[0].valor
    # self.valor = 1.0-self.jugadas_posibles_viables[0].valor

  # guardar nuevas posibilidades
  def agregar_jugadas(self, tableros):
    self.jugadas_posibles = self.jugadas_posibles + tableros
    for tablero in tableros:
      tablero.tableros_de_origen.append(self)

  # cambiar valor
  def cambiar_valor(self, valor):
    self.valor = valor

  # recuperar llaves
  def llaves_jugadas_posibles(self):
    return [tablero.llave for tablero in self.jugadas_posibles]

  # recuperar llaves viables
  def llaves_jugadas_posibles_viables(self):
    return [tablero.llave for tablero in self.jugadas_posibles_viables]