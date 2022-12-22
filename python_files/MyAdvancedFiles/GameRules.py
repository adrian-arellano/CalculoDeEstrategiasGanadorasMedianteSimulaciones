# from typing import Sequence
#
# from python_files.MyAdvancedFiles.MyBoard import MyBoard
#
#
# class GameRules:
#   def __init__(self, n, m, mt_sym, p1_sym_lst, p2_sym_lst):
#     self.verify_given_data(n, m, mt_sym, p1_sym_lst, p2_sym_lst)
#
#     self.n = n
#     self.m = m
#     self.mt_sym = mt_sym
#     self.p1_sym_lst = frozenset(p1_sym_lst)
#     self.p2_sym_lst = frozenset(p2_sym_lst)
#     self.sym_lst = self.p1_sym_lst.union(self.p2_sym_lst)
#     self.full_sym_lst = self.sym_lst.union([self.mt_sym])
#
#
#   @staticmethod
#   def valid_symbol(sym):
#     return (isinstance(sym, str)) and (len(sym) == 1)
#
#   @staticmethod
#   def valid_symbol_list(sym_lst, mt_sym=None, full_sym_lst=None):
#     if not isinstance(sym_lst, Sequence):
#       return False
#     for sym in sym_lst:
#       cond = (GameRules.valid_symbol(sym)
#               and ((mt_sym is None) or (sym != mt_sym))
#               and ((full_sym_lst is None) or (sym in full_sym_lst)))
#       if not cond:
#         return False
#     return True
#
#   @staticmethod
#   def verify_given_data(n, m, mt_sym, p1_sym_lst, p2_sym_lst):
#     report = "GameRules.__init__"
#     # n
#     if not ((isinstance(n, int)) and (n > 0)):
#       raise Exception(f"{report}: given 'n' is not an integer greater than 0.\nInstead it is '{n}'.")
#     # m
#     if not ((isinstance(m, int)) and (m > 0)):
#       raise Exception(f"{report}: given 'm' is not an integer greater than 0.\nInstead it is {m}'.")
#     # mt_sym
#     if not GameRules.valid_symbol(mt_sym):
#       raise Exception(f"{report}: given 'mt_sym' is not a valid symbol.\nInstead it is '{mt_sym}'.")
#     # p1_sym_lst
#     if not GameRules.valid_symbol_list(p1_sym_lst, mt_sym=mt_sym):
#       raise Exception(f"{report}: given 'p1_sym_lst' is not a collection, or one of the element in 'p1_sym_lst' is not "
#                       f"a valid [non empty] symbol.\nInstead 'p1_sym_lst' is '{p1_sym_lst}'.")
#     # p2_sym_lst
#     if not GameRules.valid_symbol_list(p2_sym_lst, mt_sym=mt_sym):
#       raise Exception(f"{report}: given 'p2_sym_lst' is not a collection, or one of the element in 'p2_sym_lst' is not "
#           f"a valid [non empty] symbol.\nInstead 'p2_sym_lst' is '{p2_sym_lst}'.")
#
#   def valid_matrix_board(self, matrix_board):
#     if not ((isinstance(matrix_board, Sequence)) and (len(matrix_board) == self.n)):
#       return False
#     for lst in matrix_board:
#       if not (GameRules.valid_symbol_list(lst, full_sym_lst=self.full_sym_lst) and (len(matrix_board) == self.m)):
#         return False
#     return True
#
#   def verify_matrix_board(self, matrix_board):
#     report = "GameRules.verify_matrix_board"
#     if not self.valid_matrix_board(matrix_board):
#       raise Exception(f"{report}: given 'matrix_board' does not fulfill the current GameRules.\n"
#                       f"Given Board is:\n{matrix_board}.\n\n And the GameRules are\n{self}.")
#
#   def count_and_get_symbols(self, matrix_board):
#     sym_count = 0
#     sym_set = set()
#     for i in range(self.n):
#       for j in range(self.m):
#         sym = matrix_board[i][j]
#         if sym != self.mt_sym:
#           sym_count += 1
#           sym_set.add(sym)
#     return sym_count, frozenset(sym_set)
#
#   def valid_play(self, sym, board_sym, sym_count):
#     if board_sym != self.mt_sym:
#       return False
#     if sym_count % 2 == 0:
#       if not (sym in self.p1_sym_lst):
#         return False
#     else:
#       if not (sym in self.p2_sym_lst):
#         return False
#     return True
#
#   def empty_board(self):
#     new_matrix_board = [[self.mt_sym for _ in range(self.m)] for _ in range(self.n)]
#     return MyBoard(self, new_matrix_board, sym_count=0, symbols=frozenset(), trust=True)
#
#   def __str__(self):
#     return (f"<GameRulesType>:\n\tn = {self.n}\n\tm = {self.m}\n\tmt_sym = '{self.mt_sym}'\n\t"
#             f"p1_sym_lst = {self.p1_sym_lst}\n\tp2_sym_lst = {self.p2_sym_lst}")
#
#   def __eq__(self, other):
#     if not isinstance(other, GameRules):
#       return False
#
#     return ((self.n == other.n)
#             and (self.m == other.m)
#             and (self.mt_sym == other.mt_sym)
#             and (self.p1_sym_lst == other.p1_sym_lst)
#             and (self.p2_sym_lst == other.p2_sym_lst))
#
#   def __ne__(self, other):
#     return not self.__eq__(other)
#
#   def __hash__(self):
#     return hash((self.n, self.m, self.mt_sym, self.p1_sym_lst, self.p2_sym_lst))