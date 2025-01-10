import time
import numpy as np
from random import randint

def tic_tac_toe():
    cord = []

    mat = np.full((3, 3), " ") # this the board generator


    winning_combinations = [
        # Rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    def print_stylish_welcome_message():
        print("\n")
        print("***************************************")
        print("*                                     *")
        print("*      WELCOME TO TIC-TAC-TOE         *")
        print("*                                     *")
        print("***************************************")
        print("**     Let's Play and Have Fun!   **")
        print("***************************************")

    def cordinate_generator(cord):   # this is cordinated generator
        for row in range(0,3):
            for col in range(0,3):
                li = (row, col)
                cord.append(li)
        # print(cord)


    def check_winner(user):
        for combination in winning_combinations:
            if all(cordinate in user for cordinate in combination):
                return True
        return False


    def user_appending(index):
        if index:
            user.append(index)
            cord.remove(index)
            # print("users index = ", select_cord)
            # print('users', user)
            # print('cord', cord)
            mat[index[0], index[1]] = "X"
            print(mat)


    def computer_appending(index2):
        if index2:
            computer.append(index2)
            cord.remove(index2)
            # print("computer index = ", android)
            # print('computer', computer)
            # print('cord', cord)
            mat[index2[0], index2[1]] = "O"
            time.sleep(3)
            print(mat)


    run = True
    user = []
    computer = []
    cordinate_generator(cord)

    print_stylish_welcome_message()
    print('\n',mat, '\n')
    print("welcome to the tic-tac-toe game!!")
    option = input("You want to play this game? (y/n): ")
    if option == "y":
        sign = input("\n what sign you want to choose(X/O) note(O is for hard mode): ")

    while run:
        if option == "y":   # option for yes or no to start the game

            if sign.upper() == "X":     # sign to choose for play

                print("\n You are first player")
                selectcord = int(input(f"\n Enter the number of cell,"
                                       f" you want to mark (select between 0 to {len(cord)-1})")) # user choosing number
                select_cord = selectcord-1

                if len(cord)-1 < select_cord:
                    print("list is not that long",len(cord)-1)
                    print(cord)
                else:
                    index = cord[int(select_cord)]
                    user_appending(index)
                    if check_winner(user):
                        # print(user)
                        print("user win!!")
                        break

                    # android making choice for the number
                    if cord == []:
                        print("GAME IS DRAW!!!")
                        run = False
                    else:
                        print("\n Android is making his choice...")
                        android = randint(0, len(cord) - 1)
                        index2 = cord[android]
                        computer_appending(index2)
                        if check_winner(computer):
                            # print(computer)
                            print("computer wins!!")
                            break

            elif sign.upper() == "O":

                print("\n You are second to play first will android will be playing ")
                # android making choice for the number
                if cord == []:
                    print("GAME IS DRAW!!")
                    run = False
                else:
                    print("Android is making his choice...")
                    android = randint(0, len(cord) - 1)
                    index2 = cord[android]
                    computer_appending(index2)
                    if check_winner(computer):
                        # print(computer)
                        print("computer wins!!!")
                        break

                if cord != []:
                    selectcord = int(input(f"\n Enter the number of cell,"
                                           f" you want to mark (select between 0 to {len(cord)-1})")) # user choosing number
                    select_cord = selectcord-1
                    if len(cord) - 1 < select_cord:
                        print("list is not that long", len(cord) - 1)
                        print("\n You have selected out of range number,"
                              " so android will be playing, your chance will be gone.")
                    else:
                        index = cord[int(select_cord)]
                        user_appending(index)
                        if check_winner(user):
                            # print(user)
                            print("user wins!!")
                            break

                else:
                    run = False
            else:
                print("you have chosen invalid option so you are exited.")
                run = False
        else:
            print("You have exited the game.")
            run = False



tic_tac_toe()
playagain = input("want to play again?")
if playagain == "y":
    tic_tac_toe()
elif playagain == "n":
    print("Thank you for playing.")