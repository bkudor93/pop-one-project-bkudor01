# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

import random
import os


def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    assert s[0] >= 'A' and s[0] <= 'E'
    assert s[1] >= '1' and s[1] <= '5'
    dic_row_sl = {'A':0, 'B':1, 'C':2, 'D': 3,'E':4}
    dic_column_sl = {'1':0, '2':1, '3':2, '4':3, '5':4}
    location = (dic_row_sl[s[0]], dic_column_sl[s[1]])
    return location

def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    assert location[0] >= 0 and location[0] <= 4
    assert location[1] >= 0 and location[1] <= 4
    dic_row_ls = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
    dic_column_ls = {0:'1', 1:'2', 2:'3', 3:'4', 4:'5'}
    string = dic_row_ls[location[0]] + dic_column_ls[location[1]]
    return string

def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""
    list_all = []
    for i in range(0,5):
        for n in range(0,5):
          list_all.append((i,n))
    return list_all

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    (row, column) = location
    if direction == 'left':
        location = (row, column - 1)
    if direction == 'right':
        location = (row, column + 1)
    if direction == 'up':
        location = (row - 1, column)
    if direction == 'down':
        location = (row + 1, column)
    return location

 

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    assert at(location) == 'M'
    return at(location) == 'M' and is_within_board(location, direction) and at(adjacent_location(location, direction)) == 'R'


def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    assert at(location) == 'R'
    return at(location) == 'R' and is_within_board(location, direction) and at(adjacent_location(location, direction)) == '-'

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""
    if at(location) == 'M':
        return is_legal_move_by_musketeer(location, direction)
    if at(location) == 'R':
        return is_legal_move_by_enemy(location, direction)

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range.
    You can assume that input will always be in correct range."""
    directions = ['left','right','up','down']
    for each_direction in directions:
        if is_legal_move(location, each_direction):
            return True
    return False


def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    if all_possible_moves_for(who):
        return True
    return False

def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    list_direction = []
    directions = ['up','down','left','right']
    for each_direction in directions:
        if is_legal_move(location, each_direction):
            list_direction.append(each_direction)
    return list_direction

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will always be a pair of integers."""
    if 0 <= location[0] <= 4 and 0 <= location[1] <= 4:
        return True
    else:
        return False
    
def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    if is_legal_location(adjacent_location(location,direction)):
        return True
    else:
        return False
    
def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    list_all_possible = []
    for each_location in all_locations():
        if at(each_location) == player:
            for each_direction in possible_moves_from(each_location):
                list_all_possible.append((each_location, each_direction))
    return list_all_possible


def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    global board
    new_location = adjacent_location(location, direction)
    board[new_location[0]][new_location[1]] = at(location)
    board[location[0]][location[1]]= '-'

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    possible_moves = all_possible_moves_for(who)    
    return random.choice(possible_moves)


def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    for i in range(0,5):
        for n in range(0,3):
            if at((i,n)) == at((i,n+1)) == at((i,n+2)) == 'M':
                return True
    for k in range(0,3):
        for l in range(0,5):
            if at((k,l)) == at((k+1,l)) == at((k+2,l)) == 'M':
                return True
    return False


#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def save():
	f = open('save.txt','w')
	f.write("\n".join((str(board), str(users_side))))
	f.close()
	
def load():
	f = open('save.txt','r')
	print(f)

def main():
    os.system('clear')
    print("Welcome to the Three Muskateers game!")
    option = input("Key s to start a new game and l to load existing game.")
    if option == 's':
        start()
    else:
        load()
        

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()


def print_instructions():
    print()
    print ("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print ("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print ("You can't move there!")
            return move_enemy(users_side)
    else: #Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print (who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    os.system('clear')
    print("Welcome to the Three Muskateers game!")
    option = input("Key s to start a new game and l to load existing game.")
    if option == 's':
        users_side = choose_users_side()
        create_board()
    else:
        f = open('save.txt','r')
        data = f.readlines()
        f.close()
        users_side = data[1]
        import ast
        create_board()
        global board
        board = ast.literal_eval(data[0])
    print_instructions()
    print_board()
        
    while True:
        if has_some_legal_move_somewhere('M'):
            ask_to_save = input("To continue press c, if you would like to save press s")
            if ask_to_save == 's':
                board1 = str(get_board())
                f = open('save.txt','w')
                f.write("\n".join((str(board1), str(users_side))))
                f.close()
                exit()
            
            move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print ("Cardinal Richleau's men win!")
                break
        else:
            print ("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            move_enemy(users_side)
            print_board()
        else:
            print ("The Musketeers win!")
            break

start()

