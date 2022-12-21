from GameRules import GameRules

SEPARATOR = '|'

def tuple_mat(mat):
  return tuple(tuple(lst) for lst in mat)


class MyBoard:
  def __init__(self, game_rules, matrix_board, sym_count=None, symbols=None, trust=False):
    if not trust:
      self.verify_game_rules(game_rules)
      game_rules.verify_matrix_board(matrix_board)

    self.game_rules = game_rules
    self.matrix_board = tuple_mat(matrix_board)

    if trust and (sym_count is not None) and (symbols is not None):
      self.sym_count, self.symbols = sym_count, symbols
    else:
      self.sym_count, self.symbols = self.game_rules.count_and_get_symbols(matrix_board)

  @staticmethod
  def verify_game_rules(game_rules):
    if not isinstance(game_rules, GameRules):
      raise Exception(f"The given argument 'game_rules', is not a GameRules\nInstead it is {game_rules}")

  def board(self, i, j):
    return self.matrix_board[i][j]

  def copy_board(self):
    return [[sym for sym in lst] for lst in self.matrix_board]

  def is_player1_turn(self):
    return self.sym_count % 2 == 0

  def verify_play(self, i, j, sym):
    report = "MyBoard.create_next_board"
    if sym == self.game_rules.mt_sym:
      raise Exception(f"{report}: the given symbol is an empty symbol '{sym}'.")
    if self.board(i, j) != self.game_rules.mt_sym:
      raise Exception(f"{report}: the given position ({i}, {j}), already has a [non empty] symbol"
                      f"'{self.board(i, j)}'.")
    if self.is_player1_turn():
      if not (sym in self.game_rules.p1_sym_lst):
        raise Exception(f"{report}: is the player's 1 turn, and (s)he can't play the symbol '{sym}'.")
    else:
      if not (sym in self.game_rules.p2_sym_lst):
        raise Exception(f"{report}: is the player's 2 turn, and (s)he can't play the symbol '{sym}'.")

  def create_next_board(self, i, j, sym):
    self.verify_play(i, j, sym)
    new_board = self.copy_board()
    new_board[i][j] = sym
    new_sym_count = self.sym_count + 1
    new_symbols = self.symbols.union([sym])
    return MyBoard(self.game_rules, tuple_mat(new_board), sym_count=new_sym_count, symbols=new_symbols, trust=True)

  def __str__(self):
    out = ''
    for lst in self.matrix_board:
      out += SEPARATOR
      for sym in lst:
        out += sym + SEPARATOR
      out += "\n"
    return out

  def __eq__(self, other):
    if not isinstance(other, MyBoard):
      return False

    return ((self.game_rules == other.game_rules)
            and (self.matrix_board == other.matrix_board))

  def __ne__(self, other):
    return not self.__eq__(other)

  def __hash__(self):
    return hash((self.game_rules, self.matrix_board))
