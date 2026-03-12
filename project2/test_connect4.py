"""
Nazaneen Baguaei,
Project 2, pytest, part 2
March 12, 2026
"""
import pytest
from connect4 import Connect4


# test that switch_player switches from X to O
def test_switch_player_x_to_o():
    game = Connect4()
    game.switch_player()
    assert game.current_player == 'O'


# test that switch_player switches from O back to X
def test_switch_player_o_to_x():
    game = Connect4()
    game.current_player = 'O'
    game.switch_player()
    assert game.current_player == 'X'


# test that switch_player toggles correctly multiple times
def test_switch_player_multiple_times():
    game = Connect4()
    game.switch_player()  # X -> O
    game.switch_player()  # O -> X
    game.switch_player()  # X -> O
    assert game.current_player == 'O'


# test that switch_player does not affect the board
def test_switch_player_does_not_change_board():
    game = Connect4()
    board_before = [row[:] for row in game.board]
    game.switch_player()
    assert game.board == board_before


# parametrized test: starting player, number of switches, expected player
@pytest.mark.parametrize(
    "start_player, switches, expected",
    [
        ('X', 1, 'O'),
        ('X', 2, 'X'),
        ('O', 1, 'X'),
        ('O', 2, 'O'),
    ]
)
def test_switch_player_parametrized(start_player, switches, expected):
    game = Connect4()
    game.current_player = start_player
    for _ in range(switches):
        game.switch_player()
    assert game.current_player == expected


# --------------------------------------------
# Test Results Documentation
# -----------------------------------------------
# Test: test_switch_player_x_to_o
#   Result: PASS
#   Notes: switch_player() correctly changed current_player from X to O.
#
# Test: test_switch_player_o_to_x
#   Result: PASS
#   Notes: Set current_player to O manually, switch_player() returned X.
#
# Test: test_switch_player_multiple_times
#   Result: PASS
#   Notes: Called switch_player 3 times from X, ended at O as expected.
#
# Test: test_switch_player_does_not_change_board
#   Result: PASS
#   Notes: Board state was identical before and after calling switch_player.
#
# Test: test_switch_player_parametrized
#   Result: PASS (all 4 cases)
#   Notes: Parametrized test confirmed correct toggling for all combinations.
# -----------------------------------------------------