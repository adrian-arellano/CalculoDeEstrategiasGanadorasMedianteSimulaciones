from MyBoard_GameRules import GameRules
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

GatoGameRules = GameRules(3, 3, ' ', ['X'], ['O'], end_game, name="Gato")


def my_fun(board):
  for i in range(board.n()):
    for j in range(board.m()):
      if board.board(i, j) == board.mt_sym():
        sym = 'X' if board.is_player1_turn() else 'O'
        new_board = board.create_next_board(i, j, sym)
        return new_board


a = MyGUI(GatoGameRules, my_fun)

a.run()
