from GameRules import GameRules
from MyBoard import MyBoard

GatoGameRules = GameRules(3, 3, ' ', ['X'], ['O'])

board1 = [[' ', 'X', 'O'],
          ['X', 'O', ' '],
          ['O', 'X', ' ']]

myBoard1 = MyBoard(GatoGameRules, board1)

print(myBoard1)
