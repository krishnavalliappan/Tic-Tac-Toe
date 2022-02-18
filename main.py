import random as rd
import re
from replit import clear

element = ["X", "O"]
elements = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_result():
    game_print = f" {elements[0][0]} | {elements[0][1]} | {elements[0][2]}\n" \
                 f"----------- \n" \
                 f" {elements[1][0]} | {elements[1][1]} | {elements[1][2]}\n" \
                 f"----------- \n" \
                 f" {elements[2][0]} | {elements[2][1]} | {elements[2][2]}\n" \
                 f"----------- \n"
    print(game_print)


def check_data():
    #     row wise checking
    for ele in elements:
        if set(ele) == {"X"} or set(ele) == {"O"}:
            return set(ele).pop()
    #     column wise checking
    for i in range(0, 3):
        new_list = []
        for j in range(0, 3):
            new_list.append(elements[j][i])
        if set(new_list) == {"X"} or set(new_list) == {"O"}:
            return set(new_list).pop()
    #     Diagonal wise checking
    right_diag_list = []
    for i in range(0, 3):
        right_diag_list.append(elements[i][i])
    if set(right_diag_list) == {"X"} or set(right_diag_list) == {"O"}:
        return set(right_diag_list).pop()
    left_diag_list = []
    for i in range(0, 3):
        column_index_list = [2, 1, 0]
        left_diag_list.append(elements[i][column_index_list[i]])
    if set(left_diag_list) == {"X"} or set(left_diag_list) == {"O"}:
        return set(left_diag_list).pop()


def add_data(player_symbl: str, player_name):
    if not player_name == "Computer":
        while True:
            selection = re.findall("[0-9]+", input(
                f"{player_name}: Select where to place your symbol {player_symbl} in board in row and column wise: "))
            if elements[int(selection[0]) - 1][int(selection[1]) - 1] == " ":
                elements[int(selection[0]) - 1][int(selection[1]) - 1] = player_symbl
                break
            else:
                print("Already data Entered")
    else:
        go_on = input("Generate Computer Move:")
        while True:
            row = rd.randint(1, 3)
            column = rd.randint(1, 3)
            if elements[row - 1][column - 1] == " ":
                elements[row - 1][column - 1] = player_symbl
                print(f"Symbol added in ({row}, {column})")
                break
    clear()
    print_result()
    win_symbol = check_data()
    if win_symbol:
        print(f"{player_name} won the Game")
        return True
    if tie_checker():
        return True
    return False


def player_shot(sym, player_name):
    try:
        return add_data(sym, player_name)
    except IndexError as err:
        print(err)
        return add_data(sym, player_name)


def check_function(data, cond: list):
    if data in cond:
        return True


def input_play_game():
    while True:
        game_on = input("Do you want to play the Tic-Tac-Toe Game[Y/N]:").lower()
        if check_function(game_on, ["y", 'n']):
            break
        else:
            print("Error, please type 'Y' or 'N'")
    if game_on == "y":
        return True
    else:
        return False


def input_player():
    while True:
        players_count = int(input('How many players are playing?[1 or 2]:'))
        if check_function(players_count, [1, 2]):
            break
        else:
            print("Error, please type '1' or '2' ")
    return players_count


def input_symbol():
    while True:
        player_1_symbol = input(f"player_1 Choose your Symbol {element}:")
        if check_function(player_1_symbol, element):
            break
        else:
            print("Error, please type only 'X' or 'O'")
    return player_1_symbol


def tie_checker():
    rows = 0
    for ele in elements:
        if " " not in set(ele):
            rows += 1
    if rows == 3:
        print("Game was ended in Tie")
        return True


play_game = input_play_game()

if play_game:
    no_players = input_player()
    player_1_sym = input_symbol()
    while True:
        if no_players == 2:
            player_2_name = "Player-2"
        else:
            player_2_name = "Computer"
            # Player-2 symbol selection
        if player_1_sym == "X":
            player_2_sym = "O"
        else:
            player_2_sym = "X"
        if player_shot(player_1_sym, "Player-1"):
            break
        if player_shot(player_2_sym, player_2_name):
            break
