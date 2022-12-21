# guardar partidas
class Partida:
  def __init__(self, tablero_inicial):
    self.tableros = []
    self.agregar_jugada(tablero_inicial)

  # agrega el tablero resultante de una jugada
  def agregar_jugada(self, tablero_siguiente):
    self.tableros.append(tablero_siguiente)

  # regresar al turno
  def retroceder_antes_del_turno(self, n):
    self.tableros = self.tableros[:n]

  def reiniciar(self):
    self.tableros = self.tableros[:1]

  # en que van
  def tablero_actual(self):
    return self.tableros[-1]

  # tablero en turno n
  def tablero_en_turno(self, n):
    return self.tableros[n]

  # turno actual
  def turno_actual(self):
    return len(self.tableros) - 1

  # actualizar desde turno n (desuso)
  def actualizar_hacia_atras_turno(self, n):
    for turno in range(n - 1, -1, -1):
      self.tableros[turno].actualizar_tableros_viables(True)

  # cambiar valor (desuso)
  def cambiar_valor_turno(self, n, valor):
    self.tableros[n].cambiar_valor(valor)
    self.actualizar_hacia_atras_turno(n)