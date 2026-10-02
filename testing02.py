row1 = ["~","~","~"]
row2 = ["~","~","~"]
row3 = ["~","~","~"]
col1 = [row1[0], row2[0], row3[0]]
col2 = [row1[1], row2[1], row3[1]]
col3 = [row1[2], row2[2], row3[2]]
move = False
def display_board():
     """Prints the board"""
     print(row1)
     print(row2)
     print(row3)
display_board()

def player1():
    """Grabs player 1's selected spot"""
    while True:
        print("Player 1's turn!")
        play1row = int(input("Enter the row of your choice: "))
        play1col = int(input("Enter the column of your choice that is 1 to 3: "))
        if play1row == 1:
            row1[play1col - 1] = "x"
            display_board()
            break
        elif play1row == 2:
            row2[play1col - 1] = "x"
            display_board()
            break
        elif play1row == 3:
            row3[play1col - 1] = "x"
            display_board()
            break
        else:
            print("Enter a number 1 - 3 next time")

def player2():
    """Grabs player 2's selected spot"""
    while True:
        print("Player 2's turn!")
        play2row = int(input("Enter the row of your choice: "))
        play2col = int(input("Enter the column of your choice: "))
        if play2row == 1:
            row1[play2col - 1] = "o"
            display_board()
            break
        elif play2row == 2:
            row2[play2col - 1] = "o"
            display_board()
            break
        elif play2row == 3:
            row3[play2col - 1] = "o"
            display_board()
            break
        else:
            print("Enter a number 1 - 3 next time")

def check_for_winner():
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

def running_middle():
    while True:
        player1()
        check_for_winner()
        if move:
            break
        else:
            player2()
            check_for_winner
            if move:
                break
            else:
                running_middle()
running_middle()