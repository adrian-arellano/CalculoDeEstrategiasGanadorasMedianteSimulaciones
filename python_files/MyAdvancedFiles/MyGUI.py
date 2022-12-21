from collections.abc import Callable, Sequence
from tkinter import *
from tkinter import ttk

b_height = 1
b_width = 2

SOLO_MODE = 1
VS_MACHINE_MODE = 2


class MyGUI:
  def __init__(self, n, m, sym_lst, end_game_fun, turn_fun=None, mt_sym=" "):
    # Saving given data
    self.n = n
    self.m = m
    self.sym_lst = sym_lst
    self.mt_sym = mt_sym
    self.end_game_fun = end_game_fun

    self.verify_given_data()

    # Other
    self.turn_fun = turn_fun
    self.game_ended = False
    self.mode = False
    self.delay = None

    # Creating important Matrices
    self.button_matrix = [[None for _ in range(m)] for _ in range(n)]
    self.board = self.empty_board()

    # Building Window
    self.root = Tk()

    self.super_frm = ttk.Frame(self.root, padding=20)
    self.super_frm.grid()

    self.upper_text = Label(self.super_frm, text="Hello", font=("Arial", 20))
    self.upper_text.grid(column=0, row=0)

    self.frm = ttk.Frame(self.super_frm, padding=20)
    self.frm.grid(column=0, row=1)
    self.frm.grid()

    self.build_buttons()

    self.frm2 = ttk.Frame(self.super_frm, padding=20)
    self.frm2.grid(column=0, row=2)
    self.frm2.grid()

    self.sub_frm2 = ttk.Frame(self.frm2, padding=20)
    self.sub_frm2.grid(column=0, row=0)
    self.sub_frm2.grid()

    self.p1 = Label(self.sub_frm2, text="Player 1")
    self.p1.grid(column=0, row=0)

    self.p2b = Button(self.sub_frm2, text="Machine", height=b_height, width=self.n * b_width)
    self.p2b.grid(column=0, row=1)

    self.p2b2 = Button(self.sub_frm2, text="You", height=b_height, width=self.n * b_width)
    self.p2b2.grid(column=0, row=2)

    self.p2 = Label(self.sub_frm2, text="Player 2")
    self.p2.grid(column=2, row=0)

    self.p2b = Button(self.sub_frm2, text="Machine", height=b_height, width=self.n * b_width)
    self.p2b.grid(column=2, row=1)

    self.p2b2 = Button(self.sub_frm2, text="You 2", height=b_height, width=self.n * b_width)
    self.p2b2.grid(column=2, row=2)

    self.vs = Label(self.sub_frm2, text=" vs ")
    self.vs.grid(column=1, row=1)

    self.start_game_button = Button(self.frm2, text="Reset Button", command=self.reset_board, height=b_height, width=2 * self.n * b_width)
    self.start_game_button.grid(column=0, row=1)

  def update_text(self, new_text):
    self.upper_text["text"] = new_text

  def button(self, i, j):
    return self.button_matrix[i][j]

  def empty_board(self):
    return [[self.mt_sym for _ in range(self.m)] for _ in range(self.n)]

  def copy_board(self):
    return [[self.board[i][j] for j in range(self.m)] for i in range(self.n)]

  def verify_given_data(self):
    # n
    if not ((isinstance(self.n, int)) and (self.n > 0)):
      raise Exception("MyGUI.__init__: given 'n' is not an integer greater than 0.\nInstead it is "
                      f"'{self.n}'.")
    # m
    if not ((isinstance(self.m, int)) and (self.m > 0)):
      raise Exception("MyGUI.__init__: given 'm' is not an integer greater than 0.\nInstead it is "
                      f"'{self.m}'.")
    # sym_lst
    if not isinstance(self.sym_lst, Sequence):
      raise Exception("MyGUI.__init__: given 'sym_lst' is not a collection.\nInstead it is "
                      f"'{self.sym_lst}'.")
    else:
      for c in self.sym_lst:
        if not ((isinstance(c, str)) and (len(c) == 1)):
          raise Exception("MyGUI.__init__: one of the given variables inside collection 'sym_lst' is not "
                          f"just a character.\nInstead it is '{c}'.")
    # mt_sym
    if not ((isinstance(self.mt_sym, str)) and (len(self.mt_sym) == 1)):
      raise Exception("MyGUI.__init__: given 'mt_sym' is not just a character.\nInstead it is "
                      f"'{self.mt_sym}'.")
    # end_game_fun
    if not isinstance(self.end_game_fun, Callable):
      raise Exception("MyGUI.__init__: given 'end_game_fun' is not a function.\nInstead it is "
                      f"'{self.end_game_fun}'.")

  def verify_turn_function(self):
    if self.turn_fun is None:
      raise Exception("MyGUI.play_a_turn: no 'turn_fun' has benn given.")

    if not isinstance(self.turn_fun, Callable):
      raise Exception("MyGUI.play_a_turn: given 'turn_fun' is not a function.\nInstead it is "
                      f"'{self.turn_fun}'.")

  def build_buttons(self):
    for i in range(self.n):
      for j in range(self.m):
        # noinspection PyTypeChecker
        self.button_matrix[i][j] = Button(self.frm, text=self.mt_sym, command=self.command_for(i, j),
                                          height=b_height, width=b_width)
        self.button(i, j).grid(column=i, row=j)

  def command_for(self, i, j):
    return lambda: self.alternatives_window_for(i, j)

  def alternatives_window_for(self, i, j):
    root_2 = Toplevel(self.root)
    root_2.grab_set()  # No permite que se use la ventana principal.
    frm_2 = ttk.Frame(root_2, padding=20)
    frm_2.grid()
    for n, sym in enumerate(self.sym_lst):
      Button(frm_2, text=sym, command=self.select_sym(root_2, i, j, sym), height=b_height, width=b_width).grid(
        column=0, row=n)
    self.root.wait_window(root_2)
    if self.mode == VS_MACHINE_MODE:
      self.root.update()
      self.root.after(self.delay, self.play_a_turn())

  def select_sym(self, other_root, i, j, sym):
    def aux_fun():
      self.update_box(i, j, sym)
      other_root.destroy()

    return aux_fun

  # Returns the amount of updates that were made
  # noinspection PyTypeChecker
  def update_box(self, i, j, sym):
    if not ((sym in self.sym_lst) or (sym is self.mt_sym)):
      raise Exception("MyGUI.update_box: given 'sym' is not a character from 'sym_lst', neither 'mt_sym' "
                      f"character.\nInstead it is '{sym}'.")
    # do nothing
    elif self.board[i][j] == sym:
      return 0

    but = self.button(i, j)
    but["text"] = sym
    if sym is self.mt_sym:  # deactivate
      but["state"] = "active"
      but["bg"] = "#F0F0F0"
    else:  # activate
      but["state"] = "disable"
      but["bg"] = "#CBCBCB"
    self.board[i][j] = sym
    return 1

  def verify_board(self, board, fun_name):
    if not ((isinstance(board, Sequence)) and (len(board) == self.n)):
      raise Exception(f"MyGUI.{fun_name}: given 'board' is not a collection of length equals to {self.n}.\n"
                      f"Instead it is '{board}'.")
    else:
      for lst in board:
        if not ((isinstance(lst, Sequence)) and (len(lst) == self.m)):
          raise Exception(f"MyGUI.{fun_name}: one of the given variables inside the collection 'board' is not a "
                          f"collection of length equals to {self.m}.\nInstead it is '{lst}'.")
        else:
          for sym in lst:
            if not ((sym in self.sym_lst) or (sym is self.mt_sym)):
              raise Exception(f"MyGUI.{fun_name}: given variable inside the matrix 'board' is not a "
                              "character from 'sym_lst', neither 'mt_sym' character.\nInstead it is "
                              f"'{sym}'.")

  def play_a_turn(self):
    copied_board = self.copy_board()
    cond = self.end_game_fun(copied_board)
    if cond == 0:
      result_board = self.turn_fun(copied_board)
      if self.update_board(result_board) != 1:
        raise Exception("MyGUI.play_a_turn: given 'turn_fun' played more than one time or didn't played at "
                        f"all.\n Please revise {self.turn_fun} function.")
    else:
      self.game_ended = True
      if cond == 1:
        self.update_text("Player 1 Wins")
      elif cond == 2:
        self.update_text("Player 2 Wins")
    return cond

  # Returns the amount of updates that were made
  def update_board(self, board):
    self.verify_board(board, "update_board")
    box_updated = 0
    for i in range(self.n):
      for j in range(self.m):
        box_updated += self.update_box(i, j, board[i][j])
    return box_updated

  def reset_board(self):
    self.update_board(self.empty_board())
    self.update_text("Hello Again")
    if (self.mode == SOLO_MODE) and self.game_ended:
      self.root.after(self.delay, self.my_fun_extension())
    self.game_ended = False

  def my_fun_extension(self):
    def aux_fun():
      if self.play_a_turn() == 0:
        self.root.after(self.delay, self.my_fun_extension())

    return aux_fun

  def run(self):
    self.root.mainloop()

  def run_solo_play(self, delay):
    self.mode = SOLO_MODE
    self.delay = delay
    self.root.after(self.delay, self.my_fun_extension())
    self.root.mainloop()

  def run_vs_machine(self, delay):
    self.mode = VS_MACHINE_MODE
    self.delay = delay
    self.root.mainloop()


def my_fun(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == " ":
        board[i][j] = "O"
        return board


'''
    Returns 0 if none has won
    If someone won, returns 1 if the player that did the last movement won.
                    returns 2 if the other player won.  
'''


def end_game(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == " ":
        return 0
  return 1


# print(isinstance(end_game, Callable))


a = MyGUI(7, 10, ['X', 'O', "h"], end_game)
a.turn_fun = my_fun

# a.run_solo_play(100)
a.run_vs_machine(500)
