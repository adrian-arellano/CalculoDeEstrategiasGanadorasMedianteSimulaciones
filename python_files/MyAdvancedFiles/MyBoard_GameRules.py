SEPARATOR = ''


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

  def n(self):
    return self.game_rules.n

  def m(self):
    return self.game_rules.m

  def mt_sym(self):
    return self.game_rules.mt_sym

  def p1_sym_lst(self):
    return self.game_rules.p1_sym_lst

  def p2_sym_lst(self):
    return self.game_rules.p2_sym_lst

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

  def get_current_sym_lst(self):
    if self.is_player1_turn():
      return self.game_rules.p1_sym_lst
    else:
      return self.game_rules.p2_sym_lst

  '''
  Returns a tuple (bool, i, j, sym)
  Where bool: is True iff 'other' is a posible next board
        i, j: are the coordinates where the difference resides
        sym : is the symbol which 'other' has in that coordinate. 
  '''
  def posible_next_board(self, other):
    report = "MyBoard.posible_next_board"
    if not isinstance(other, MyBoard):
      raise Exception(f"{report}: the given 'other' for comparison is not an instance of 'MyBoard'.\n"
                      f"Instead it is {other}.")
    out_i = out_j = out_sym = None
    cond = ((self.game_rules == other.game_rules)
            and (self.sym_count + 1 == other.sym_count))
    if not cond:
      return False, out_i, out_j, out_sym
    dif = 0
    for i in range(self.game_rules.n):
      for j in range(self.game_rules.m):
        cur_sym, new_sym = self.board(i, j), other.board(i, j)
        if cur_sym != new_sym:
          cond = ((cur_sym == self.game_rules.mt_sym)
                  and (new_sym in self.get_current_sym_lst()))
          if not cond:
            return False, out_i, out_j, out_sym
          else:
            dif += 1
            out_i, out_j, out_sym = i, j, new_sym
            if dif > 1:
              return False, out_i, out_j, out_sym
    return True, out_i, out_j, out_sym

  def get_winner(self):
    return self.game_rules.end_game_fun(self)

  @staticmethod
  def from_llave_to_MyBoard(llave, game_rules):
    print([[i * game_rules.m + j for j in range(game_rules.m)] for i in range(game_rules.n)])
    matrix_board = [[llave[i * game_rules.m + j] for j in range(game_rules.m)] for i in range(game_rules.n)]
    return MyBoard(game_rules=game_rules, matrix_board=matrix_board)


  def __str__(self):
    out = ''
    for lst in self.matrix_board:
      out += SEPARATOR
      for sym in lst:
        out += sym + SEPARATOR
      #out += "\n"
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


# -----------------------------------------------------------------------------------------------------------------------

from typing import Sequence, Callable


# from python_files.MyAdvancedFiles.MyBoard import MyBoard


class GameRules:
  def __init__(self, n, m, mt_sym, p1_sym_lst, p2_sym_lst, end_game_fun, name):
    self.verify_given_data(n, m, mt_sym, p1_sym_lst, p2_sym_lst, end_game_fun, name)

    self.n = n
    self.m = m
    self.mt_sym = mt_sym
    self.p1_sym_lst = frozenset(p1_sym_lst)
    self.p2_sym_lst = frozenset(p2_sym_lst)
    self.sym_lst = self.p1_sym_lst.union(self.p2_sym_lst)
    self.full_sym_lst = self.sym_lst.union([self.mt_sym])
    self.end_game_fun = end_game_fun
    self.name = name

  @staticmethod
  def valid_symbol(sym):
    return (isinstance(sym, str)) and (len(sym) == 1)

  @staticmethod
  def valid_symbol_list(sym_lst, mt_sym=None, full_sym_lst=None):
    if not isinstance(sym_lst, Sequence):
      return False
    for sym in sym_lst:
      cond = (GameRules.valid_symbol(sym)
              and ((mt_sym is None) or (sym != mt_sym))
              and ((full_sym_lst is None) or (sym in full_sym_lst)))
      if not cond:
        return False
    return True

  @staticmethod
  def verify_given_data(n, m, mt_sym, p1_sym_lst, p2_sym_lst, end_game_fun, name):
    report = "GameRules.__init__"
    # n
    if not ((isinstance(n, int)) and (n > 0)):
      raise Exception(f"{report}: given 'n' is not an integer greater than 0.\nInstead it is '{n}'.")
    # m
    if not ((isinstance(m, int)) and (m > 0)):
      raise Exception(f"{report}: given 'm' is not an integer greater than 0.\nInstead it is {m}'.")
    # mt_sym
    if not GameRules.valid_symbol(mt_sym):
      raise Exception(f"{report}: given 'mt_sym' is not a valid symbol.\nInstead it is '{mt_sym}'.")
    # p1_sym_lst
    if not GameRules.valid_symbol_list(p1_sym_lst, mt_sym=mt_sym):
      raise Exception(f"{report}: given 'p1_sym_lst' is not a collection, or one of the element in 'p1_sym_lst' is not "
                      f"a valid [non empty] symbol.\nInstead 'p1_sym_lst' is '{p1_sym_lst}'.")
    # p2_sym_lst
    if not GameRules.valid_symbol_list(p2_sym_lst, mt_sym=mt_sym):
      raise Exception(f"{report}: given 'p2_sym_lst' is not a collection, or one of the element in 'p2_sym_lst' is not "
                      f"a valid [non empty] symbol.\nInstead 'p2_sym_lst' is '{p2_sym_lst}'.")
    # end_game_fun
    if not isinstance(end_game_fun, Callable):
      raise Exception(f"{report}: given 'end_game_fun' is not a function.\nInstead it is "
                      f"'{end_game_fun}'.")
    # title
    if not isinstance(name, str):
      raise Exception(f"{report}: given 'name' is not a string.\nInstead it is '{name}'.")

  def valid_matrix_board(self, matrix_board):
    if not ((isinstance(matrix_board, Sequence)) and (len(matrix_board) == self.n)):
      return False
    for lst in matrix_board:
      if not (GameRules.valid_symbol_list(lst, full_sym_lst=self.full_sym_lst) and (len(matrix_board) == self.m)):
        return False
    return True

  def verify_matrix_board(self, matrix_board):
    report = "GameRules.verify_matrix_board"
    if not self.valid_matrix_board(matrix_board):
      raise Exception(f"{report}: given 'matrix_board' does not fulfill the current GameRules.\n"
                      f"Given Board is:\n{matrix_board}.\n\n And the GameRules are\n{self}.")

  def count_and_get_symbols(self, matrix_board):
    sym_count = 0
    sym_set = set()
    for i in range(self.n):
      for j in range(self.m):
        sym = matrix_board[i][j]
        if sym != self.mt_sym:
          sym_count += 1
          sym_set.add(sym)
    return sym_count, frozenset(sym_set)

  def valid_play(self, sym, board_sym, sym_count):
    if board_sym != self.mt_sym:
      return False
    if sym_count % 2 == 0:
      if not (sym in self.p1_sym_lst):
        return False
    else:
      if not (sym in self.p2_sym_lst):
        return False
    return True

  def empty_board(self):
    new_matrix_board = [[self.mt_sym for _ in range(self.m)] for _ in range(self.n)]
    return MyBoard(self, new_matrix_board, sym_count=0, symbols=frozenset(), trust=True)

  def __str__(self):
    return (f"<GameRulesType>:\n\tn = {self.n}\n\tm = {self.m}\n\tmt_sym = '{self.mt_sym}'\n\t"
            f"p1_sym_lst = {self.p1_sym_lst}\n\tp2_sym_lst = {self.p2_sym_lst}")

  def __eq__(self, other):
    if not isinstance(other, GameRules):
      return False

    return ((self.n == other.n)
            and (self.m == other.m)
            and (self.mt_sym == other.mt_sym)
            and (self.p1_sym_lst == other.p1_sym_lst)
            and (self.p2_sym_lst == other.p2_sym_lst))

  def __ne__(self, other):
    return not self.__eq__(other)

  def __hash__(self):
    return hash((self.n, self.m, self.mt_sym, self.p1_sym_lst, self.p2_sym_lst))
