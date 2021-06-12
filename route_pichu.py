#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code provided in CSCI B551, Spring 2021.


import sys
import json


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]


# Return a string with the board rendered in a human/pichu-readable format
def printable_board(board):
    return "\n".join(["".join(row) for row in board])


# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    return 0 <= pos[0] < n and 0 <= pos[1] < m


# Find the possible moves from position (row, col)
def moves(map, row, col, Direction):
    moves = ((row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1))
    moves_list = []  # To attach the direction to the valid moves and return to the search function
    valid_moves_list = []  # local list it gives moves which are valid.

    for move in moves:
        if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@"):
            valid_moves_list.append(move)

    # in the below code we are just adding D if going down by a step. similarly for up, Right and Left.
    # we are doing this to only valid moves as we are storing them in valid_moves_list
    for i in valid_moves_list:
        if (i[0] == row + 1) and (i[1] == col):
            k = [i[0], i[1], Direction + 'D']
            moves_list.append(k)
        elif (i[0] == row - 1) and (i[1] == col):
            k = [i[0], i[1], Direction + 'U']
            moves_list.append(k)
        elif (i[0] == row) and (i[1] == col - 1):
            k = [i[0], i[1], Direction + 'L']
            moves_list.append(k)
        elif (i[0] == row) and (i[1] == col + 1):
            k = [i[0], i[1], Direction + 'R']
            moves_list.append(k)

    # Return only moves that are within the board and legal (i.e. go through open space ".")
    return (moves_list)


# Perform search on the map
#
# This function MUST take a single parameter as input -- the hose map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)
# In the below code, they have given a stack. since it is going to infinite state , changed fringe to queue by  inserting at 0 position in the fringe.
def search(house_map):
    # Find pichu start position
    pichu_loc = [(row_i, col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if
                 house_map[row_i][col_i] == "p"][0]
    fringe = [(pichu_loc, '', 0)]
    visited_node_list = []  # To avoid alreday visiting nodes. it reduces the time complexity and it hinders the infinite loops.

    while fringe:
        (curr_move, path_string, curr_dist) = fringe.pop()
        visited_node_list.append(curr_move)

        for move in moves(house_map, *curr_move, path_string):
            move = tuple(move)

            # only if is not in visting_node_list we are going to compare and add to fringe
            if (move[0:2] not in visited_node_list):

                if house_map[move[0]][move[1]] == "@":
                    return (curr_dist + 1, move[2])
                else:
                    fringe.insert(0, (move[0:2], move[2], curr_dist + 1))

    return (-1, '')


# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])
    # print(moves(house_map,2,2))
    print("Routing in this board:\n" + printable_board(house_map) + "\n")
    print("Shhhh... quiet while I navigate!")
    solution = search(house_map)
    print("Here's the solution I found:")
    print(str(solution[0]) + " " + str(solution[1]))