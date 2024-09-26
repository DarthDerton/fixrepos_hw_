from typing import List


"""
function tic_tac_toe_checker that takes a list of board lists representing the Tic-Tac-Toe board and returns
a string indicating the winner or tie.

to check rows, columns, and diagonals, we define three internal functions: check_rows, check_columns,
and check_diagonals.Each of these functions checks the corresponding rows, columns, or diagonals for a winner
and returns a row with a message about the winner, if there is one, or an empty string otherwise.
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