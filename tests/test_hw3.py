import pytest
from typing import List


"""
in this test, we use the @pytest.mark.parametrize decorator to define several test cases.
Each test case is a tuple of two elements: board and expected_result.
We then call the tic_tac_toe_checker function with each board and check that the result matches expected_result.
"""


def tic_tac_toe_checker(board: List[List]) -> str:
    def check_rows() -> str:
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != '-':
                return f"{row[0]} wins!"
        return ''

    def check_columns() -> str:
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '-':
                return f"{board[0][i]} wins!"
        return ''

    def check_diagonals() -> str:
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
            return f"{board[0][0]} wins!"
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
            return f"{board[0][2]} wins!"
        return ''

    for check_func in [check_rows, check_columns, check_diagonals]:
        result = check_func()
        if result:
            return result

    if '-' in [cell for row in board for cell in row]:
        return 'unfinished'
    else:
        return 'draw!'


@pytest.mark.parametrize("board, expected_result", [
    ([['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']], 'X wins!'),
    ([['O', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'X']], 'draw!'),
    ([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']], 'unfinished'),
    ([['O', 'O', 'O'], ['-', '-', '-'], ['-', '-', '-']], 'O wins!'),
    ([['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']], 'X wins!'),
    ([['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']], 'X wins!'),
])
def test_tic_tac_toe_checker(board, expected_result):
    assert tic_tac_toe_checker(board) == expected_result