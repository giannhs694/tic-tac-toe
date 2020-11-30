import numpy as np
import re

"""tic tac toe"""

table = np.empty([3, 3], dtype='str')
turn = ['x', 'o']


def play_turn():
    while True:
        try:
            print(table)
            move = input(F"{turn[0]},  it's your turn: ")  # takes in x,y
            move = re.split('; |,|, | ', move)
            move = list(map(int, move))
            if len(move) != 2:
                raise ValueError
            break
        except ValueError:
            print("You have to choose a box from 0, 0 to 2, 2")
    print(move)
    if table[move[0], move[1]] == '':
        table[move[0], move[1]] = turn[0]
        turn[0], turn[1] = turn[1], turn[0]
    else:
        print("Try again, box already taken")


def check_for_winner():
    # Searches for winner in each row, each column, and diagonally
    winner = None
    for j in range(3):
        y = 0
        if table[j, y] == table[j, y + 1] == table[j, y + 2] and table[j, y] != '':
            winner = table[j, y]
        if table[y, j] == table[y + 1, j] == table[y + 2, j] and table[y, j] != '':
            winner = table[y, j]
    if (table[1, 1] == table[0, 0] == table[2, 2] and table[j, j] != '') or (
            table[1, 1] == table[0, 2] == table[2, 0] and table[j, j] != ''):
        winner = table[j, j]
    if winner:
        return winner
    else:
        return None


# Game takes place, Up to 9 turns
for i in range(10):
    # Player can only win if he has already played 3 times
    if i >= 4:
        winner = check_for_winner()
        if winner:
            print(f"The winner is {winner}")
            break
    if i == 9:
        winner = check_for_winner()
        if winner:
            print(f"The winner is {winner}")
        else:
            print("It's a tie")
        break
    play_turn()
check_for_winner()
