from MyBoard import MyBoard, GameRules
from python_files.MyAdvancedFiles.MyGUI import MyGUI


'''
    Returns 0 if none has won
    If someone won, returns 1 if the player that did the last movement won.
                    returns 2 if the other player won.  
'''
def end_game(board):
  for i in range(board.n()):
    for j in range(board.m()):
      if board.board(i, j) == board.mt_sym():
        return 0
  return 1

GatoGameRules = GameRules(3, 3, ' ', ['X'], ['O'], end_game, name="Gato")

board1 = [[' ', 'X', 'O'],
          ['X', 'O', ' '],
          ['O', 'X', ' ']]

board2 = [['X', 'X', 'O'],
          ['X', 'O', ' '],
          ['O', 'X', ' ']]

board3 = [['O', 'X', 'O'],
          ['X', 'O', ' '],
          ['O', 'X', ' ']]

myBoard1 = MyBoard(GatoGameRules, board1)
myBoard2 = MyBoard(GatoGameRules, board2)
myBoard3 = MyBoard(GatoGameRules, board3)

# print(myBoard1.posible_next_board(myBoard2))
# print(myBoard1.posible_next_board(myBoard3))

# print(isinstance(end_game, Callable))

def my_fun(board):
  for i in range(board.n()):
    for j in range(board.m()):
      if board.board(i, j) == board.mt_sym():
        sym = 'X' if board.is_player1_turn() else 'O'
        new_board = board.create_next_board(i, j, sym)
        return new_board




# print(isinstance(GatoGameRules, GameRules))

a = MyGUI(GatoGameRules, my_fun)
a.turn_fun = my_fun

# a.run_solo_play(100)
a.run()