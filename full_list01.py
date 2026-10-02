row1 = ["~","~","~"]
row2 = ["~","~","~"]
row3 = ["~","~","~"]
col1 = [row1[0], row2[0], row3[0]]
col2 = [row1[1], row2[1], row3[1]]
col3 = [row1[2], row2[2], row3[2]]

def display_board():
     print(row1)
     print(row2)
     print(row3)
display_board()

def player1():
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
player1()

def player2():
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
player2()

def check_for_winner():
     while True:
          if row1 == ["x","x","x"] or row2 == ["x","x","x"] or row3 == ["x","x","x"]:
               print("Player 1 won!")
               break
          elif row1 == ["y","y","y"] or row2 == ["y","y","y"] or row3 == ["y","y","y"]:
               print("Player 2 won!")
               break
          if col1 == ["x","x","x"] or col2 == ["x","x","x"] or col3 == ["x","x","x"]:
               print("Player 1 won!")
               break
          elif col1 == ["y","y","y"] or col2 == ["y","y","y"] or col3 == ["y","y","y"]:
               print("Player 2 won!")
               break
          if row1[0] == "x" and row2[1] == "x" and row3[2] == "x":
              print("Player 1 won!")
          elif row1[0] == "y" and row2[1] == "y" and row3[2] == "y":
              print("Player 2 won!") 