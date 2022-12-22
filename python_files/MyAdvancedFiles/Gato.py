from MyBoard_GameRules import GameRules
from python_files.GPI import GPI
from python_files.Juego import Juego
from python_files.MyAdvancedFiles.MyGUI import MyGUI

def str_sum(iterable):
  out = ''
  for s in iterable:
    out += s
  return out


'''
    Returns 0 if none has won
    If someone won, returns 1 if the player that did the last movement won.
                    returns 2 if the other player won.
                    returns 3 if no one won.  
'''
def end_game(board):
  win1 = "XXX"
  win2 = "OOO"

  # columns
  for i in range(board.n()):
    word = str_sum(board.board(i, j) for j in range(board.m()))
    if win1 in word:
      return 1
    elif win2 in word:
      return 2
  # rows
  for j in range(board.m()):
    word = str_sum(board.board(i, j) for i in range(board.n()))
    if win1 in word:
      return 1
    elif win2 in word:
      return 2

  aux = lambda i, j: (board.board(i, j) if ((0 <= i < board.n()) and (0 <= j < board.m())) else '')
  # diagonals 1
  for i in range(board.n()):
    word1 = str_sum(aux(i + j, j) for j in range(board.m()))
    if win1 in word1:
      return 1
    elif win2 in word1:
      return 2
    word2 = str_sum(aux(i - j, j) for j in range(board.m()))
    if win1 in word2:
      return 1
    elif win2 in word2:
      return 2

  # diagonals 2
  for j in range(board.m()):
    word1 = str_sum(aux(i, j + i) for i in range(board.n()))
    if win1 in word1:
      return 1
    elif win2 in word1:
      return 2
    word2 = str_sum(aux(i, j - i) for i in range(board.n()))
    if win1 in word2:
      return 1
    elif win2 in word2:
      return 2

  if board.sym_count == board.n() * board.m():
    return 3
  return 0

GatoGameRules = GameRules(3, 3, ' ', ['x'], ['o'], end_game, name="Gato")

# GIT
# oraculo de reglas
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

# Entrenar

Gato = Juego(3,3,' '*9)
Gato.cambiar_reglasJ1(ReglasGatoJugador1)
Gato.cambiar_reglasJ2(ReglasGatoJugador2)
Gato.cambiar_victoriaJ1(CondicionVictoriaGatoJ1)
Gato.cambiar_victoriaJ2(CondicionVictoriaGatoJ2)

figGato = {}

Demo2 = GPI(Gato)


def my_fun(board):
  # for i in range(board.n()):
  #   for j in range(board.m()):
  #     if board.board(i, j) == board.mt_sym():
  #       sym = 'X' if board.is_player1_turn() else 'O'
  #       new_board = board.create_next_board(i, j, sym)
  #       return new_board
  return Demo2.play_a_board(board)


a = MyGUI(GatoGameRules, my_fun)

a.run()
