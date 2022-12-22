from MyBoard_GameRules import GameRules
from python_files.MyAdvancedFiles.MyGUI import MyGUI

'''
    Returns 0 if none has won
    If someone won, returns 1 if the player that did the last movement won.
                    returns 2 if the other player won.
                    returns 3 if no one won.  
'''
def end_game(board):
  out = lambda aux: (1 if aux == 'X' else 2)
  for i in range(3):
    r = board.board(i, 0)
    if (r != board.mt_sym()) and (r == board.board(i, 1)) and (r == board.board(i, 2)):
      return out(r)
    c = board.board(0, i)
    if (c != board.mt_sym()) and (c == board.board(1, i)) and (c == board.board(2, i)):
      return out(c)
  d = board.board(1, 1)
  if ((d != board.mt_sym()) and
          (((d == board.board(0, 0)) and (d == board.board(2, 2))) or
           ((d == board.board(0, 2)) and (d == board.board(2, 0))))):
    return out(d)
  if board.sym_count == 9:
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
