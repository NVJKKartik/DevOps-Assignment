'''
TODO: Tic Tac Toe Game
-> class Tic_Tac_Toe():
     def __init__(self): Added by @PlatJack
     def mainloop(self): Added by @PlatJack
     def initialize_board(self): Added by @PlatJack
     def play_again(self):
     
     Drawing Functions
      def draw_O(self, logical_position):
      def draw_X(self, logical_position):
      def display_gameover(self):
      def convert_logical_to_grid_position(self, logical_position):
      def convert_grid_to_logical_position(self, grid_position):
      def is_grid_occupied(self, logical_position):
      def is_winner(self, player):
      def is_tie(self):
      def is_gameover(self):
      def click(self, event):
      
Contribution Guidlines:
Format for adding author name =>

#Author Name
#What does this function do?
def function():

USE TABS AND NOT SPACES FOR INDENTATION

'''

from tkinter import *
import numpy as np

size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
symbol_X_color = '#EE4035'
symbol_O_color = '#0492CF'
Green_color = '#7BC043'


class Tic_Tac_Toe():
	# ------------------------------------------------------------------
	# author: PlatJack
	# Game Initialization Functions - 
	# ------------------------------------------------------------------
	def _init_(self):
		self.window = Tk()
		self.window.title('Tic-Tac-Toe')
		self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
		self.canvas.pack()
		self.window.bind('<Button-1>', self.click)
		
		self.initialize_board()
		self.player_X_turns = True
		self.board_status = np.zeros(shape=(3, 3))
		
		self.player_X_starts = True
		self.reset_board = False
		self.gameover = False
		self.tie = False
		self.X_wins = False
		self.O_wins = False
		
		self.X_score = 0
		self.O_score = 0
		self.tie_score = 0
	
	# ------------------------------------------------------------------
	# author: PlatJack
	# Window Looping Function - 
	# ------------------------------------------------------------------
	def mainloop(self):
		self.window.mainloop()
	
	# ------------------------------------------------------------------
	# author: PlatJack
	# Board Initialization Function - 
	# ------------------------------------------------------------------
	def initialize_board(self):
		for i in range(2):
			self.canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)
		for i in range(2):
			self.canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)
