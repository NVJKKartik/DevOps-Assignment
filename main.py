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


class Tic_Tac_Toe:
    # ------------------------------------------------------------------
    # author: PlatJack
    # Game Initialization Functions -
    # ------------------------------------------------------------------
    def __init__(self):
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
            self.canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

    # ------------------------------------------------------------------
    # author: Aryan T N
    # Draw O -
    # ------------------------------------------------------------------
    def draw_O(self, logical_position):
        logical_position = np.array(logical_position)
        # logical_position = grid value on the board
        # grid_position = actual pixel values of the center of the grid
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                 grid_position[0] + symbol_size, grid_position[1] + symbol_size,
                                 width=symbol_thickness, outline=symbol_O_color)

    # ------------------------------------------------------------------
    # author: Rohan Chidri
    # Draw X -
    # ------------------------------------------------------------------
    def draw_X(self, logical_position):
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                 grid_position[0] + symbol_size, grid_position[1] + symbol_size,
                                 width=symbol_thickness, fill=symbol_X_color)
        self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                 grid_position[0] + symbol_size, grid_position[1] - symbol_size,
                                 width=symbol_thickness, fill=symbol_X_color)

	# ------------------------------------------------------------------
    # author: Vivaan Sharma
    # is_tie and is_gameover
    # ------------------------------------------------------------------
    def is_tie(self):
        r, c = np.where(self.board_status == 0)
        tie = False
        if len(r) == 0:
           tie = True
        return tie

    def is_gameover(self):
		# Either someone wins or all grid occupied
        self.X_wins = self.is_winner('X')
        if not self.X_wins:  
              self.O_wins = self.is_winner('O')

        if not self.O_wins:
              self.tie = self.is_tie()

        gameover = self.X_wins or self.O_wins or self.tie

        if self.X_wins:
              print('X wins')
        if self.O_wins:
              print('O wins') 
        if self.tie:
              print('It\'s a tie')

        return gameover
	# author: Gacha76 (Sharan)
	# Conversion from Logical to Grid Position - 
	# ------------------------------------------------------------------
    def convert_logical_to_grid_position(self, logical_position):
        logical_position = np.array(logical_position, dtype=int)
        return (size_of_board / 3) * logical_position + size_of_board / 6

	# ------------------------------------------------------------------
	# author: Gacha76 (Sharan)
	# Conversion from Grid to Logical Position - 
	# ------------------------------------------------------------------
    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (size_of_board / 3), dtype=int)

	# ------------------------------------------------------------------
	# author: Gacha76 (Sharan)
	# Function to check if grid is occupied or not - 
	# ------------------------------------------------------------------
    def is_grid_occupied(self, logical_position):
        if self.board_status[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True

	
	# ------------------------------------------------------------------
	# author: ShravyaBhat
	# Added Function to check for winner by looking at 3 consecutive rows, columns or diagonals to be same
	# ------------------------------------------------------------------
	def is_winner(self,player):
		player = -1 if player =='X' else 1
		for i in range(3):
			if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2]==player:
				return True
			if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
				return True
			if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
				retur True
			if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
				return True
		return False

        
	# ------------------------------------------------------------------
    # author: Aayushi Padia
    # Play Again -
    # ------------------------------------------------------------------
    def play_again(self):
        self.initialize_board()
        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = np.zeros(shape=(3,3))

