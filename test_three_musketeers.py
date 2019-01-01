import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M    
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    #eventually add at least one more exception test and two more
    #test with correct inputs
    assert (0,0) == string_to_location('A1')
    assert (1,2) == string_to_location('B3')
    assert (3,4) == string_to_location('D5')
    assert (4,1) == string_to_location('E2')
    assert (2,2) == string_to_location('C3')
    
    
def test_location_to_string():
    assert 'A1' == location_to_string((0,0))
    assert 'B3' == location_to_string((1,2))
    assert 'D5' == location_to_string((3,4))
    assert 'E2' == location_to_string((4,1))
    assert 'C3' == location_to_string((2,2))

def test_at():
    assert 'M' == at((0,3))
    assert 'M' == at((1,3))
    assert 'R' == at((3,1))
    assert '-' == at((4,0))
    assert '-' == at((4,4))

def test_all_locations():
    assert [(0,0),(0,1),(0,2),(0,3),(0,4),
            (1,0),(1,1),(1,2),(1,3),(1,4),
            (2,0),(2,1),(2,2),(2,3),(2,4),
            (3,0),(3,1),(3,2),(3,3),(3,4),
            (4,0),(4,1),(4,2),(4,3),(4,4)] == all_locations()

def test_adjacent_location():
    assert (0,2) == adjacent_location((0,3), 'left')
    assert (1,3) == adjacent_location((1,2), 'right')
    assert (1,2) == adjacent_location((2,2), 'up')
    assert (4,1) == adjacent_location((3,1), 'down')
    
def test_is_legal_move_by_musketeer():
    assert is_legal_move_by_musketeer((1,3), 'left')
    assert is_legal_move_by_musketeer((2,2), 'left')
    assert is_legal_move_by_musketeer((2,2), 'right')
    assert not is_legal_move_by_musketeer((0,3), 'left')
    assert not is_legal_move_by_musketeer((1,3), 'right')
    
def test_is_legal_move_by_enemy():
    assert is_legal_move_by_enemy((1,2), 'left')
    assert is_legal_move_by_enemy((2,1), 'left')
    assert is_legal_move_by_enemy((4,3), 'up')
    assert not is_legal_move_by_enemy((1,2), 'right')
    assert not is_legal_move_by_enemy((2,1), 'down')

def test_is_legal_move():
    assert is_legal_move((1,2), 'left')
    assert is_legal_move((2,2), 'left')
    assert is_legal_move((1,3), 'left')
    assert not is_legal_move((0,3), 'left')
    assert not is_legal_move((2,1), 'down')

def test_can_move_piece_at():
    assert can_move_piece_at((1,3))
    assert can_move_piece_at((1,2))
    assert can_move_piece_at((3,1))
    assert not can_move_piece_at((0,3))
    assert not can_move_piece_at((4,1))

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board
    set_board([ [_, _, _, _, _],
                [_, _, _, _, _],
                [_, _, _, _, _],
                [M, M, _, _, _],
                [R, M, _, _, _] ] )
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == False

def test_possible_moves_from():
    assert [] == possible_moves_from((0,0))
    assert ['left', 'up'] == possible_moves_from((1,2))
    assert ['left', 'right', 'up'] == possible_moves_from((2,2))
    assert ['left', 'right', 'down'] == possible_moves_from((3,1))
    assert ['left', 'down'] == possible_moves_from((1,3))

def test_is_legal_location():
    assert is_legal_location((2,4))
    assert is_legal_location((1,3))
    assert is_legal_location((2,1))
    assert not is_legal_location((-1,4))
    assert not is_legal_location((2,5))
    assert not is_legal_location((5,0))

def test_is_within_board():
    set_board(board1)
    assert is_within_board((1,1), 'right') == True

def test_all_possible_moves_for():
    set_board([ [_, _, R, M, R],
                [_, _, _, M, M],
                [_, _, _, _, _],
                [_, _, _, _, _],
                [_, _, _, _, _] ] )
    assert [((0,2), 'left'),((0,2), 'down')] == all_possible_moves_for('R')
    assert [((0,3), 'left'),((0,3), 'right'), ((1,4), 'up')] == all_possible_moves_for('M')


def test_make_move():
    make_move((0,3),'left')
    assert at((0,3)) == '-'
    assert at((0,2)) == 'M'
    make_move((4,3),'up')
    assert at((4,3)) == '-'
    assert at((3,3)) == 'R'
        
def test_choose_computer_move():
    set_board([ [_, _, R, M, R],
                [_, _, M, _, M],
                [_, _, _, _, _],
                [_, _, _, _, _],
                [R, _, _, _, _] ] )
        # The computer chooses randomly, so each test will be different
    assert choose_computer_move('R') in [((0,2),'left'), ((4,0), 'up'), ((4,0), 'right')]
    assert choose_computer_move('R') in [((0,2),'left'), ((4,0), 'up'), ((4,0), 'right')]
    assert choose_computer_move('R') in [((0,2),'left'), ((4,0), 'up'), ((4,0), 'right')]
    assert choose_computer_move('R') in [((0,2),'left'), ((4,0), 'up'), ((4,0), 'right')]
    assert choose_computer_move('R') in [((0,2),'left'), ((4,0), 'up'), ((4,0), 'right')]
    assert choose_computer_move('R') in [((0,2),'left'), ((4,0), 'up'), ((4,0), 'right')]
        
    set_board([ [R, _, _, _, R],
                [_, R, M, _, M],
                [_, _, R, _, _],
                [_, _, _, _, _],
                [M, _, _, _, _] ] )
    assert choose_computer_move('M') in [((1,4),'up'), ((1,2),'left'), ((1,2),'down')]
    assert choose_computer_move('M') in [((1,4),'up'), ((1,2),'left'), ((1,2),'down')]
    assert choose_computer_move('M') in [((1,4),'up'), ((1,2),'left'), ((1,2),'down')]
    assert choose_computer_move('M') in [((1,4),'up'), ((1,2),'left'), ((1,2),'down')]
    assert choose_computer_move('M') in [((1,4),'up'), ((1,2),'left'), ((1,2),'down')]
    assert choose_computer_move('M') in [((1,4),'up'), ((1,2),'left'), ((1,2),'down')]

def test_is_enemy_win():
    set_board([ [_, _, R, M, R],
                [_, _, _, M, M],
                [_, _, _, _, _],
                [_, _, _, _, _],
                [_, _, _, _, _] ] )
    assert not is_enemy_win()
    set_board([ [_, _, R, M, R],
                [_, _, _, M, _],
                [_, _, _, M, _],
                [_, _, _, _, _],
                [_, _, _, _, _] ] )
    assert is_enemy_win()
    set_board([ [_, _, R, _, R],
                [_, _, M, M, M],
                [_, _, _, _, _],
                [_, _, _, _, _],
                [_, _, _, _, _] ] )
    assert is_enemy_win()
    set_board([ [_, _, R, _, R],
                [_, _, _, _, M],
                [_, _, _, _, M],
                [_, _, _, _, M],
                [_, _, _, _, _] ] )
    assert is_enemy_win()

