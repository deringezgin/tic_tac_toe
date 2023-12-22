from os import system


def clear():
    """Function for clearing the screen"""
    _ = system("clear")


def clear_board(lines):
    """Function for clearing the game board"""
    lines.clear()
    for i in range(3):
        lines.append(["-", "-", "-"])


def print_lines(lines):
    """Function for printing the lines of the game board"""
    print("-------------------------")
    for line in lines:
        text = "   |   ".join(line)
        print(f"|   {text}   |")
        print("-------------------------")


def take_input(user, lines):
    """Function for taking user input and checking if it's between correct range, type. If so changes the tile"""
    x = input("\nPlease enter the row you'd like to place your tile (1..3): ")
    y = input("Please enter the column you'd like to place your tile (1..3): ")

    while not ((x.isdigit() and y.isdigit()) and (0 < int(x) < 4) and (0 < int(y) < 4) and (lines[int(x) - 1][int(y) - 1] == "-")):
        print("\nInvalid input please enter again: ")
        x = input("\nPlease enter the row you'd like to place your tile (1...3): ")
        y = input("Please enter the column you'd like to place your tile (1...3): ")

    x = int(x)
    y = int(y)

    if user % 2 == 0:
        lines[x-1][y-1] = "O"
    elif user % 2 == 1:
        lines[x-1][y-1] = "X"


def check_win(lines):
    """Checking if there is any win combinations in the current board"""
    for i in range(3):
        if lines[i][0] == lines[i][1] == lines[i][2] != "-":
            return False
        elif lines[0][i] == lines[1][i] == lines[2][i] != "-":
            return False
        elif lines[0][0] == lines[1][1] == lines[2][2] != "-":
            return False
        elif lines[0][2] == lines[1][1] == lines[2][0] != "-":
            return False
    return True


def check_availability(lines):
    """Checking if there is any available tiles in the game-board"""
    for i in range(3):
        for a in range(3):
            if lines[i][a] == "-":
                return True
    return False


# Variable declarations
game_lines = []
turn = 0
cont_game = True
score_1 = 0
score_2 = 0
round = 1

while cont_game:   # General Game loop
    clear_board(game_lines)

    while check_win(game_lines):   # Single Game Loop
        print("--- TIC TAC TOE GAME ---")
        print(f"Round: {round}\n")

        if not check_availability(game_lines):
            break

        if turn % 2 == 0:
            print("Turn of player 1: O")
        elif turn % 2 != 0:
            print("Turn of player 2: X")

        print_lines(game_lines)
        take_input(turn, game_lines)

        clear()
        turn += 1

    if not check_availability(game_lines):
        print("No Slots Are Available to Continue")
        print("No One Won")
    else:
        if turn % 2 == 0:
            print("Player 2, X Won")
            score_2 += 1
            round += 1
        elif turn % 2 != 0:
            print("Player 1, O Won")
            score_1 += 1
            round += 1

    another_round = input("Would you like to play another round? Yes or no: ").lower()

    while another_round not in ["yes", "no"]:
        print("\nInvalid input please enter again: ")
        another_round = input("Would you like to play another round? Yes or No: ").lower()

    if another_round == "yes":
        cont_game = True
        clear()
    elif another_round == "no":
        cont_game = False
        clear()

clear()


print("--- TIC TAC TOE GAME ---\n")
print("Game Ended\n")

print(f"Player 1 Score: {score_1}")
print(f"Player 2 Score: {score_2}\n")

if score_1 > score_2:
    print("Player 1 Won!")
elif score_2 > score_1:
    print("Player 2 Won!")
elif score_1 == score_2:
    print("It's Draw")
