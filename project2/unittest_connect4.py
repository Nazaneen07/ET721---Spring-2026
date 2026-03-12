"""
Nazaneen Baguaei,
Project 2, unittest, part 2
March 12, 2026
"""
import unittest
from connect4 import Connect4


class TestPlayGame(unittest.TestCase):

    # create a test template (instance of the class)
    def setUp(self):
        self.game = Connect4()

    # test that the board starts empty when a new game is created
    def test_board_starts_empty(self):
        for row in self.game.board:
            for cell in row:
                self.assertEqual(cell, ' ')

    # test that the game starts with player X
    def test_starts_with_player_x(self):
        self.assertEqual(self.game.current_player, 'X')

    # test that check_win correctly detects a horizontal win
    def test_check_win_horizontal(self):
        self.game.board[5][0] = 'X'
        self.game.board[5][1] = 'X'
        self.game.board[5][2] = 'X'
        self.game.board[5][3] = 'X'
        self.assertTrue(self.game.check_win('X'))

    # test that the game correctly returns no win when there is none
    def test_no_win_on_empty_board(self):
        self.assertFalse(self.game.check_win('X'))
        self.assertFalse(self.game.check_win('O'))

    # test that is_full returns False on an empty board
    def test_board_not_full_at_start(self):
        self.assertFalse(self.game.is_full())

    # test that is_full returns True when the board is completely filled
    def test_board_is_full(self):
        for col in range(1, self.game.COLS + 1):
            for _ in range(self.game.ROWS):
                self.game.drop_chip(col)
        self.assertTrue(self.game.is_full())

    # test that drop_chip returns False when a column is full (play_game rejects the move)
    def test_full_column_rejected(self):
        for _ in range(self.game.ROWS):
            self.game.drop_chip(1)
        result = self.game.drop_chip(1)
        self.assertFalse(result)

    # test that drop_chip returns False for an out of range column (play_game rejects it)
    def test_out_of_range_column_rejected(self):
        self.assertFalse(self.game.drop_chip(0))
        self.assertFalse(self.game.drop_chip(8))


if __name__ == "__main__":
    unittest.main()


# -----------------------------------------
# Test Results Documentation
# ------------------------------------------------
# Test: test_board_starts_empty
#   Result: PASS
#   Notes: All 42 cells confirmed as empty spaces on a new game instance.
#
# Test: test_starts_with_player_x
#   Result: PASS
#   Notes: current_player is 'X' when Connect4 is first created.
#
# Test: test_check_win_horizontal
#   Result: PASS
#   Notes: Manually placed X in 4 consecutive cells on row 5.
#          check_win('X') correctly returned True.
#
# Test: test_no_win_on_empty_board
#   Result: PASS
#   Notes: check_win returned False for both players on a fresh board.
#
# Test: test_board_not_full_at_start
#   Result: PASS
#   Notes: is_full() correctly returned False on an empty board.
#
# Test: test_board_is_full
#   Result: PASS
#   Notes: Filled all columns using drop_chip. is_full() returned True.
#
# Test: test_full_column_rejected
#   Result: PASS
#   Notes: Dropped 6 chips in column 1 (filling it), 7th drop returned False.
#
# Test: test_out_of_range_column_rejected
#   Result: PASS
#   Notes: drop_chip(0) and drop_chip(8) both returned False as expected.
# ------------------------------------------------------