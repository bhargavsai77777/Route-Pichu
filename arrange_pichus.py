#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code in CSCI B551, Spring 2021
#


import sys


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]


# Count total # of pichus on board
def count_pichus(board):
    return sum([row.count('p') for row in board])


# Return a string with the board rendered in a human-pichuly format
def printable_board(board):
    return "\n".join(["".join(row) for row in board])

'''This function validates the index that the successors function gives to add_pichu.
 Furthur it checks,if we can add pichu at that particular position based on the below designed conditions. 
 This function returns a green signal to the add_pichu function  if all goes well with the below defined conditions(chceking if pichu can see other pichu)'''

def validate_position(board, R, C):
    check_dict = {'j': [0, 0, 0, 0]}
    for w in range(0, C):
        if (board[R][w] == 'p'): check_dict['j'][0] += 1
        if (board[R][w] == 'X' or board[R][w] == '@'): check_dict['j'][0] = 0

    for x in range(len(board[0]) - 1, C, -1):
        if (board[R][x] == 'p'): check_dict['j'][1] += 1
        if (board[R][x] == 'X' or board[R][x] == '@'): check_dict['j'][1] = 0

    for y in range(0, R):
        if (board[y][C] == 'p'): check_dict['j'][2] += 1
        if (board[y][C] == 'X' or board[y][C] == '@'): check_dict['j'][2] = 0

    for z in range(len(board) - 1, R, -1):
        if (board[z][C] == 'p'): check_dict['j'][3] += 1
        if (board[z][C] == 'X' or board[z][C] == '@'): check_dict['j'][3] = 0

    if sum(check_dict['j']) > 0: return False

    return True

# Add a pichu to the board at the given position, and return a new board (doesn't change original)
' In this function we are calling validate_position to check if we can add pichu at the given index'
def add_pichu(board, row, col):
    if validate_position(board,row,col)==True:return board[0:row] + [board[row][0:col] + ['p',] + board[row][col+1:]] + board[row+1:]
    else: return board


# Get list of successors of given board state
def successors(board):
    return [add_pichu(board, r, c) for r in range(0, len(board)) for c in range(0, len(board[0])) if board[r][c] == '.']


# check if board is a goal state
def is_goal(board, k):
    return count_pichus(board) == k


# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_map, success), where:
# - new_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
'''' In the below solve function, I have just made a small modification by adding a visiting_node_list, it checks if the successsor is already visited.
     Basically here we are using DFS, we know that it goes to infinite loop sometimes. To avoid these, i am not visiting alreday visited nodes.'''
def solve(initial_board, k):
    fringe = [initial_board]
    visiting_node_list = []
    while len(fringe) > 0:
        for s in successors( fringe.pop() ):
            if s not in visiting_node_list:
                if is_goal(s, k):
                    return(s,True)
                visiting_node_list.append(s)
                fringe.append(s)

    return ([],False)


# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])

    # This is K, the number of agents
    k = int(sys.argv[2])
    #k = 9
    print("Starting from initial board:\n" + printable_board(house_map) + "\n\nLooking for solution...\n")
    (newboard, success) = solve(house_map, k)
    print("Here's what we found:")
    print(printable_board(newboard) if success else "None")