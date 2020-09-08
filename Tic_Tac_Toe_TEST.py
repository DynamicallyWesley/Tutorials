# Wesley Rivera
# 9/6/2020
# Tic Tac Toe

import random

#function to display the board for tic tac toe
def display_board(board):
	# clear the board
	# print('\n'*100)
	# Format printing to make sure the marker is always in the middle
	# {0 = index : ^ = center 3 = number of characters}
	print(f'   |   |   ')
	print('{0:^3}|{1:^3}|{2:^3}'.format(board[7],board[8],board[9]))
	print(f'   |   |   ')
	print('------------')
	print(f'   |   |   ')
	print('{0:^3}|{1:^3}|{2:^3}'.format(board[4],board[5],board[6]))
	print(f'   |   |   ')
	print('------------')
	print(f'   |   |   ')
	print('{0:^3}|{1:^3}|{2:^3}'.format(board[1],board[2],board[3]))
	print(f'   |   |   ')

def player_input():
	# For the while loop
	choice = False
	
	# holders for the markers

	while choice == False:
		player1 = input("\nPlayer one please enter your marker (X or O): ").upper()

		if player1 == 'X' or player1 == 'x':
			player2 = 'O'
			print('\n')
			print(f"Player 1 is marker {player1}")
			print(f"Player 2 is marker {player2}")
			return (player1, player2)
			choice = True


		elif player1 == 'O' or player1 == 'o':
			player2 = 'X'
			print('\n')
			print(f"Player 1 is marker {player1}")
			print(f"Player 2 is marker {player2}")
			return (player1, player2)
			choice = True

		else:
			print('\nYou chose an incorrect marker please try again (X or O)')
			choice = False

def place_marker(board,marker,position):
	board[position] = marker

# Possible combinations of win
def win_check(board,mark):
	if (# Straight row
        (board[1] == board[2] == board[3] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[7] == board[8] == board[9] == mark) or
        #Diagonal
        (board[1] == board[5] == board[9] == mark) or
        (board[3] == board[5] == board[7] == mark) or
        # Straight columns
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[3] == board[6] == board[9] == mark)):
		return True

def choose_first():
	order = random.randint(1,2)
	if order == 1:
		return 'Player 1'

	elif order == 2:
		return 'Player 2'

def space_check(board, position):
	return board[position] == ' '

def full_board_check(board):
# This is a better solution form the Udemy course that uses the space_check function
	for i in range(1,10):
		if space_check(board,i):
			return False
	return True

def player_choice(board):
	#This is a better solution form the Udemy course that uses the space_check function
	position = 0
	# Checks position if it is in within your number pad 1-9
	# Also checks if the position is not empty
	while position not in range(1,10) or not space_check(board,position):
		position = int(input("\nWhat position will your next marker go? Choose a number (1-9): "))
		if position not in range(1,10):
			print('You did not type a valid position please try again.')
		elif space_check(board,position) == False:
			print('This space is already taken, please try again')
	return position

def replay():
	x = input("Do you want to play again? (Y or N): ")
	if x == 'Y' or x == 'y':
		return True
	elif x == 'N' or x == 'n':
		return False

######################################################################
print("\nWelcome to Wesley's Tic Tac Toe game!")
print("The way you insert your marker (X or O) onto the board is as follows")
print(f'   |   |   ')
print('{0:^3}|{1:^3}|{2:^3}'.format('7','8','9'))
print(f'   |   |   ')
print('------------')
print(f'   |   |   ')
print('{0:^3}|{1:^3}|{2:^3}'.format('4','5','6'))
print(f'   |   |   ')
print('------------')
print(f'   |   |   ')
print('{0:^3}|{1:^3}|{2:^3}'.format('1','2','3'))
print(f'   |   |   ')

while True:
# SET UP THE BOARD, WHO GOES FIRST AND MARKER
	board = [' ']*10

	# Tuple unpacking for the markers
	(player1_marker, player2_marker) = player_input()
	print('\n')
	# Who will go first
	turn = choose_first()
	print(turn + ' will go first')

	# asks the player if they want to play
	play_game = input('Ready to play?: (Y or N): ').upper()
	if play_game == 'Y':
		game_on = True
	else:
		game_on = False

	# The game will now commence
	while game_on:
		# Player 1 turn
		if turn == 'Player 1':
			print("\nPlayer 1's turn")
			# Display the board
			display_board(board)
			# asks player1 where they want to put their marker
			pos1 = player_choice(board)
            # Will allow the player1 to place the marker in the position
			place_marker(board,player1_marker,pos1)

            # Check if they won
			if win_check(board,player1_marker):
				display_board(board)
				print('Player 1 has won!!!')
				game_on = False
           	# Check if tie
			else:
				if full_board_check(board):
					display_board(board)
					print('The game is a tie!')
					game_on = False
				else:
            		# No win or tie? Next player goes
					turn = 'Player 2'
                

        # Player 2 turn
		else:
			print("\nPlayer 2's turn")
        	# Display the board
			display_board(board)
            # asks player1 where they want to put their marker
			pos2 = player_choice(board)
            # Will allow the player2 to place the marker in the position
			place_marker(board,player2_marker,pos2)

            # Check if they won
			if win_check(board,player2_marker):
				display_board(board)
				print('Player 2 has won!!!')
				game_on = False
           	# Check if tie
			else: 
				if full_board_check(board):
					display_board(board)
					print('The game is a tie!')
					game_on = False
				else:
            		# No win or tie? Next player goes
					turn = 'Player 1'
    
	if not replay():
		break