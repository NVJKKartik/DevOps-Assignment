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
import random
import math
from tkinter import *
import numpy as np

size_of_board = 750
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
    def __init__(self, play_with_ai = False):
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
        self.canvas.pack()

        self.window.bind('<Button-1>', self.click)

        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))
        self.play_with_ai = play_with_ai

        #Player Initialisation
        self.human_X = HumanPlayer('X')
        if play_with_ai:
            self.opponent_O = SmartComputerPlayer('O')
        else:
            self.opponent_O = HumanPlayer('X')

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
    def is_winner(self, player):
        player = -1 if player == 'X' else 1
        for i in range(3):
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                return True
            if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                return True
        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
            return True
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

	# ------------------------------------------------------------------
    # author: Vinayak
    # Click -
    # ------------------------------------------------------------------

    def click(self, event):
        if not self.player_X_turns and self.play_with_ai:
            ai_move = self.opponent_O.get_move(self)
            if ai_move is not None:
                logical_position = [ai_move//3, ai_move % 3]
                self.board_status[logical_position[0]][logical_position[1]] = 1
                self.draw_O(logical_position)
                self.player_X_turns = not self.player_X_turns
                


                if self.is_gameover():
                    self.display_gameover()
            else:
                self.canvas.delete("all")
                self.play_again()
                self.reset_board = False
            return


        grid_position = [event.x,event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)
        if not self.reset_board:
            if self.player_X_turns:
                if not self.is_grid_occupied(logical_position):
                    self.draw_X(logical_position)
                    self.board_status[logical_position[0]] [logical_position[1]] = -1
                    self.player_X_turns = not self.player_X_turns
            else:
                if not self.is_grid_occupied(logical_position):
                    self.draw_O(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = 1
                    self.player_X_turns = not self.player_X_turns

                        #Check if game is concluded
            if self.is_gameover():
                self.display_gameover()

                            # print('Done')
        else: #play Again 
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False

	# ------------------------------------------------------------------
    # author: Priyesh Gupta
    # display game over
    # ------------------------------------------------------------------
    def display_gameover(self):

            if self.X_wins:
                self.X_score += 1
                text = 'Winner: Player 1 (X)'
                color = symbol_X_color
            elif self.O_wins:
                self.O_score += 1
                text = 'Winner: Player 2 (O)'
                color = symbol_O_color
            else:
                self.tie_score += 1
                text = 'Its a tie'
                color = 'gray'

            self.canvas.delete("all")
            self.canvas.create_text(size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=color, text=text)

            score_text = 'Scores \n'
            self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                    text=score_text)
            self.reset_board = True

            score_text = 'Player 1 (X) : ' + str(self.X_score) + '\n'
            score_text += 'Player 2 (O): ' + str(self.O_score) + '\n'
            score_text += 'Tie                    : ' + str(self.tie_score)
            self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                    text=score_text)
            self.reset_board = True

            score_text = 'Click to play again \n'
            self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="gray",
                                    text=score_text)
            
	# ------------------------------------------------------------------
    # author: N.V.J.K Kartik
    # Opponent types and logic for the AI move
    # ------------------------------------------------------------------


class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter


class SmartComputerPlayer:
    def __init__(self, letter):
        self.letter = letter
        self.opponent_letter = 'O' if letter == 'X' else 'X'

    def get_move(self, game):
        if game.is_winner(self.letter) or game.is_winner(self.opponent_letter) or game.is_tie():
            return None

        available_moves = [(r, c) for r in range(3) for c in range(3) if game.board_status[r][c] == 0]
        if len(available_moves) == 9:
            return random.choice(available_moves)[0] * 3 + random.choice(available_moves)[1]

        best_move = self.minimax(game, self.letter)['position']

        if best_move is None:
            return None
        return best_move[0] * 3 + best_move[1]

    def minimax(self, game, player):
        max_player = self.letter
        other_player = self.opponent_letter

        if game.is_winner(self.opponent_letter):
            return {'position': None, 'score': -1}
        elif game.is_winner(self.letter):
            return {'position': None, 'score': 1}
        elif game.is_tie():
            return {'position': None, 'score': 0}

        available_moves = [(r, c) for r in range(3) for c in range(3) if game.board_status[r][c] == 0]

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in available_moves:
            game.board_status[possible_move[0]][possible_move[1]] = -1 if player == 'X' else 1

            sim_score = self.minimax(game, other_player)

            game.board_status[possible_move[0]][possible_move[1]] = 0
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best

	# ------------------------------------------------------------------
    # author:N.V.J.K Kartik
    # Driver Code with Main menu
    # ------------------------------------------------------------------



def main_menu():
    while(True):
        print("Welcome to Tic Tac Toe Game!")
        print("1. Play against Human")
        print("2. Play against Computer")
        choice = input("Enter 1 or 2: ")
        if choice == '1':
            game = Tic_Tac_Toe(play_with_ai=False)
            game.mainloop()
            break
        elif choice == '2':
            game = Tic_Tac_Toe(play_with_ai=True)
            game.mainloop()
            break
        else:
            print('Invalid choice please select either 1 or 2!')


if __name__ == '__main__':
    main_menu()