# clase estimador
from python_files.Tablero import Tablero


class Estimador:
  def __init__(self, checkpoint=None, separador=' '):
    self.separador = separador
    self.tableros = {}
    if checkpoint != None:
      self.leer_checkpoint(checkpoint)

  # leer checkpoint
  def leer_checkpoint(self, checkpoint):
    for llave in checkpoint:
      if not self.conoce_a(llave):
        self.tableros[llave] = Tablero(llave, [])
    for llave in checkpoint:
      if checkpoint[llave][1] != '':
        self.tableros[llave].agregar_jugadas(
          [self.tablero(vecino) for vecino in checkpoint[llave][1].split(self.separador)])
      self.tableros[llave].cambiar_valor(checkpoint[llave][0])

  # crear manualmente
  def agregar_tablero(self, llave_tablero, jugadas_siguientes):
    # if self.conoce_a(llave_tablero):
    #  return
    self.tablero(llave_tablero).agregar_jugadas([self.tablero(llave) for llave in jugadas_siguientes])
    self.tablero(llave_tablero).actualizar_tableros_viables(True)

  # crear checkpoint
  def crear_checkpoint(self):
    checkpoint = {}
    for llave in self.tableros:
      checkpoint[llave] = [self.valor(llave), self.separador.join(self.jugadas_viables(llave))]
    return checkpoint

  # revisar si un estado ya fue visitado
  def conoce_a(self, llave):
    return llave in self.tableros

  # retorna estado
  def tablero(self, llave):
    if not self.conoce_a(llave):
      self.tableros[llave] = Tablero(llave, [])
    return self.tableros[llave]

  # retorna valor
  def valor(self, llave):
    return self.tablero(llave).valor
    # if llave not in self.tableros:
    #   self.tableros[llave] = Tablero(llave,[])
    # return self.tableros[llave].valor

  # retorna vecinos importantes
  def jugadas_viables(self, llave):
    return self.tablero(llave).llaves_jugadas_posibles_viables()
    # if llave not in self.tableros:
    #   self.tableros[llave] = Tablero(llave,[])
    # return self.tableros[llave].llaves_jugadas_posibles_viables()

  # actualizar tableros viables
  def actualizar_tableros_viables(self, llave, actualizar_valores=False):
    self.tablero(llave).actualizar_tableros_viables(actualizar_valores)

  # actualizar valores
  def actualizar_valor(self, llave):
    self.tablero(llave).actualizar_valor()
