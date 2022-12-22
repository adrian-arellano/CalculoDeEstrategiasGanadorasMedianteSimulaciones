from collections.abc import Callable
from tkinter import *
from tkinter import ttk

b_height = 1
b_width = 2

NOT_DECIDED = 0
MACHINE = 1
USER = 2

PRESS_COLOR = "#CBCBCB"
NORMAL_COLOR = "#F0F0F0"


class MyGUI:
  def __init__(self, game_rules, turn_fun):
    # Saving given data
    self.game_rules = game_rules
    self.turn_fun = turn_fun

    self.verify_given_data()

    # Other
    self.game_ended = False
    self.player1 = NOT_DECIDED
    self.player2 = NOT_DECIDED
    self.current_turn = 1
    self.delay = None

    # Creating important Matrices
    self.button_matrix = [[None for _ in range(self.m())] for _ in range(self.m())]
    self.my_board = self.game_rules.empty_board()

    # Building Window
    self.root = Tk()
    self.root.title(self.game_rules.name)

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

    Label(self.sub_frm2, text="Player 1").grid(column=0, row=0)
    Label(self.sub_frm2, text=" vs ").grid(column=1, row=1)
    Label(self.sub_frm2, text="Player 2").grid(column=2, row=0)

    self.mb1 = Button(self.sub_frm2, text="Machine", command=self.mb1_fun, height=b_height, width=self.n() * b_width)
    self.mb1.grid(column=0, row=1)

    self.pb1 = Button(self.sub_frm2, text="You", command=self.pb1_fun, height=b_height, width=self.n() * b_width)
    self.pb1.grid(column=0, row=2)

    self.mb2 = Button(self.sub_frm2, text="Machine", command=self.mb2_fun, height=b_height, width=self.n() * b_width)
    self.mb2.grid(column=2, row=1)

    self.pb2 = Button(self.sub_frm2, text="You 2", command=self.pb2_fun, height=b_height, width=self.n() * b_width)
    self.pb2.grid(column=2, row=2)

    self.start_game_button = Button(self.frm2, text="Start Game", command=self.reset_board, height=b_height,
                                    width=2 * self.n() * b_width)
    self.start_game_button.grid(column=0, row=1)

  def mb1_fun(self):
    self.player1 = MACHINE
    self.mb1["bg"] = PRESS_COLOR
    self.pb1["bg"] = NORMAL_COLOR

  def mb2_fun(self):
    self.player2 = MACHINE
    self.mb2["bg"] = PRESS_COLOR
    self.pb2["bg"] = NORMAL_COLOR

  def pb1_fun(self):
    self.player1 = USER
    self.mb1["bg"] = NORMAL_COLOR
    self.pb1["bg"] = PRESS_COLOR

  def pb2_fun(self):
    self.player2 = USER
    self.mb2["bg"] = NORMAL_COLOR
    self.pb2["bg"] = PRESS_COLOR

  def set_state_lower_buttons(self, state):
    self.mb1["state"] = state
    self.mb2["state"] = state
    self.pb1["state"] = state
    self.pb2["state"] = state
    self.start_game_button["state"] = state

  def n(self):
    return self.game_rules.n

  def m(self):
    return self.game_rules.m

  def mt_sym(self):
    return self.game_rules.mt_sym

  def board(self, i, j):
    return self.my_board.board(i, j)

  def next_board(self, i, j, sym):
    self.my_board = self.my_board.create_next_board(i, j, sym)

  def update_text(self, new_text):
    self.upper_text["text"] = new_text

  def button(self, i, j):
    return self.button_matrix[i][j]

  def get_turn_owner(self):
    if self.current_turn == 1:
      return self.player1
    if self.current_turn == 2:
      return self.player2
    else:
      raise Exception(f"MyGUI.get_turn_owner: the 'self.current_turn' parameter is not 1 neither 2.\n"
                      f"Instead it is {self.current_turn}")

  def verify_given_data(self):
    report = "MyGUI.__init__"
    # game_rules [This works badly]
    # if not isinstance(self.game_rules, GameRules):
    #   raise Exception(f"{report}: given 'game_rules' is not an instance of 'GameRules'.\nInstead it is "
    #                   f"'{self.game_rules}'.")
    # # end_game_fun
    # if not isinstance(self.end_game_fun, Callable):
    #   raise Exception(f"{report}: given 'end_game_fun' is not a function.\nInstead it is "
    #                   f"'{self.end_game_fun}'.")
    # turn_fun
    if not isinstance(self.turn_fun, Callable):
      raise Exception(f"{report}: given 'turn_fun' is not a function.\nInstead it is "
                      f"'{self.turn_fun}'.")

  def build_buttons(self):
    for i in range(self.n()):
      for j in range(self.m()):
        # noinspection PyTypeChecker
        self.button_matrix[i][j] = Button(self.frm, text=self.mt_sym(), command=self.command_for(i, j),
                                          height=b_height, width=b_width)
        self.button(i, j).grid(column=i, row=j)

  def command_for(self, i, j):
    return lambda: self.alternative_window_for(i, j)

  def alternative_window_for(self, i, j):
    if self.get_turn_owner() != USER:
      return
    root_2 = Toplevel(self.root)
    root_2.grab_set()  # No permite que se use la ventana principal.
    frm_2 = ttk.Frame(root_2, padding=20)
    frm_2.grid()

    sym_lst = self.my_board.get_current_sym_lst()

    for n, sym in enumerate(sym_lst):
      Button(frm_2, text=sym, command=self.select_sym(root_2, i, j, sym), height=b_height, width=b_width).grid(
        column=0, row=n)
    self.root.wait_window(root_2)

  def select_sym(self, other_root, i, j, sym):
    def aux_fun():
      self.update_box(i, j, sym)
      other_root.destroy()
      self.next_turn()

    return aux_fun

  def update_box(self, i, j, sym):
    self.next_board(i, j, sym)
    self.press_button(i, j, sym)

  def verify_winner(self):
    cond = self.my_board.get_winner()
    if cond == 0:
      return
    else:
      self.game_ended = True
      self.set_state_lower_buttons("active")
      if cond == 1:
        self.update_text("Player 1 Wins")
      elif cond == 2:
        self.update_text("Player 2 Wins")
      elif cond == 3:
        self.update_text("Tie: No one Wins")

  def next_turn(self):
    if self.current_turn == 1:
      self.current_turn = 2
      self.update_text("Player 2 turn")
    elif self.current_turn == 2:
      self.current_turn = 1
      self.update_text("Player 1 turn")
    else:
      raise Exception(f"MyGUI.next_turn: the 'self.current_turn' parameter is not 1 neither 2.\n"
                      f"Instead it is {self.current_turn}")

    self.verify_winner()
    if not self.game_ended and (self.get_turn_owner() == MACHINE):
      self.root.update()
      self.root.after(self.delay, self.play_a_turn)

  # noinspection PyTypeChecker
  def press_button(self, i, j, sym):
    but = self.button(i, j)
    but["text"] = sym
    but["state"] = "disable"
    but["bg"] = PRESS_COLOR

  # noinspection PyUnresolvedReferences
  def reset_buttons(self):
    for but_lst in self.button_matrix:
      for but in but_lst:
        if but["text"] != self.mt_sym():
          but["text"] = self.mt_sym()
          but["state"] = "active"
          but["bg"] = NORMAL_COLOR

  def play_a_turn(self):
    report = "MyGUI.play_a_turn"
    cur_board = self.my_board
    result_board = self.turn_fun(cur_board)
    cond, i, j, sym = cur_board.posible_next_board(result_board)
    if not cond:
      raise Exception(f"{report}: given 'turn_fun' played illegally.\nThe board was:\n{cur_board}\n"
                      f"And 'turn_fun' returned:\n{result_board}")
    self.update_box(i, j, sym)
    self.next_turn()

  def reset_board(self):
    if (self.player1 is NOT_DECIDED) or (self.player2 is NOT_DECIDED):
      return
    self.my_board = self.game_rules.empty_board()
    self.reset_buttons()
    self.current_turn = 1
    self.update_text("Player 1 turn")
    self.game_ended = False
    self.set_state_lower_buttons("disable")

    if self.get_turn_owner() == MACHINE:
      self.root.update()
      self.root.after(self.delay, self.play_a_turn)

  def run(self, delay=300):
    self.delay = delay
    self.root.mainloop()
