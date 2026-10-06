row1 = ["~","~","~"]
row2 = ["~","~","~"]
row3 = ["~","~","~"]
move = False
def display_board():
     """Prints the board"""
     print(row1)
     print(row2)
     print(row3)
display_board()


def player_turn(playernum, symbol):
    """Grabs player 1's selected spot"""
    while True:
        print(f"Player {playernum}'s turn!")
        play1row = int(input("Enter the row of your choice: "))
        play1col = int(input("Enter the column of your choice that is 1 to 3: "))
        if play1row == 1:
            selected_spot = row1[play1col - 1]
        elif play1row == 2:
            selected_spot = row2[play1col - 1]
        elif play1row == 3:
            selected_spot = row3[play1col - 1]
        else:
            print("Enter a number 1 - 3 next time")
            continue
        if selected_spot == "x" or selected_spot == "o":
            print("That spot is already taken!")
            continue
        if play1row == 1:
            row1[play1col - 1] = symbol
        elif play1row == 2:
            row2[play1col - 1] = symbol
        elif play1row == 3:
            row3[play1col - 1] = symbol
        display_board()
        break

def check_for_winner():
    """Checks for the winner"""
    move = False
    col1 = [row1[0], row2[0], row3[0]]
    col2 = [row1[1], row2[1], row3[1]]
    col3 = [row1[2], row2[2], row3[2]]
    wins = [
        row1, row2, row3,
        col1, col2, col3,
        [row1[0], row2[1], row3[2]],
        [row1[2], row2[1], row3[0]]]
    for win in wins:
        if win == ["x"]*3:
            print("Player 1 won!")
            move = True
            break
        elif win == ["o"]*3:
            print("Player 2 won!")
            move = True
            break
    if row1.count("~") == 0 and row2.count("~") == 0 and row3.count("~") == 0:
        print("It's a tie!")
        move = True
    return move

def run_through():
    """Runs through the player's turns and checks if there is a winner"""
    while True:
        player_turn(1,"x")
        move = check_for_winner()
        if move:
            break
        else:
            player_turn(2,"o")
            move = check_for_winner()
            if move:
                break

run_through()

def loop():
    """Decides if the program will be ran again"""
    global row1, row2, row3
    while True:
        play_again = input("Enter y to play again, n to quit: ")
        if play_again == "y":
            row1 = ["~","~","~"]
            row2 = ["~","~","~"]
            row3 = ["~","~","~"]
            display_board()
            run_through()
            loop()
        elif play_again == "n":
            break
        else:
            print("Enter a y or n")
loop()