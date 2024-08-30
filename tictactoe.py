# Description: A simple tic-tac-toe game in Python.
board = [" " for _ in range(9)] # create a list of 9 empty spaces

def print_board():  # function to print the board
    print("")
    print("       |       |     ")
    print(f"   {board[0]}   |   {board[1]}   |   {board[2]}   ")
    print("       |       |     ")
    print("----------------------")
    print("       |       |     ")
    print(f"   {board[3]}   |   {board[4]}   |   {board[5]}   ")
    print("       |       |     ")
    print("----------------------")
    print("       |       |     ")
    print(f"   {board[6]}   |   {board[7]}   |   {board[8]}   ")
    print("       |       |     ")
    print("")

def check_winner():   # function to check if there is a winner
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True

    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True

    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True

    return False


def play_game():  # function to play the game
    current_player = "X"  # set the current player to X
    game_over = False # set the game_over to False

    while not game_over:        # while the game is not over
        print_board()           # print the board

        move = input(f"Player {current_player}, enter your move (1-9): ")                   # take input from the player


        if not move.isdigit() or int(move) < 1 or int(move) > 9 or board[int(move)-1] != " ":               # check if the input is valid
            print("Invalid move. Try again.")
            continue


        board[int(move)-1] = current_player


        if check_winner():                  #   check if there is a winner
            print_board()
            print(f"Player {current_player} wins!")
            game_over = True
        elif " " not in board:              # check if it's a tie
            print_board()
            print("It's a tie!")
            game_over = True

        current_player = "O" if current_player == "X" else "X"      # switch players


play_game()     #   call the play_game function