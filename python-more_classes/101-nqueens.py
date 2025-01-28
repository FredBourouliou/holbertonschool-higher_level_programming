#!/usr/bin/python3
"""
N queens puzzle solution.
The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard.
"""

import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed on board[row][col].

    Args:
        board (list): The current state of the board.
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the board.

    Returns:
        bool: True if a queen can be placed on board[row][col].
    """
    # Check this row on left side
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                   range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1),
                   range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n, solutions):
    """Solve the N queens puzzle using backtracking.

    Args:
        board (list): The current state of the board.
        col (int): The current column being processed.
        n (int): The size of the board.
        solutions (list): List to store all solutions.

    Returns:
        bool: True if a solution is found.
    """
    # Base case: If all queens are placed, return True
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    # Consider this column and try placing this queen in all rows one by one
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Make recursive call to place rest of the queens
            res = solve_nqueens(board, col + 1, n, solutions) or res

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0

    return res


def print_solutions(n):
    """Print all solutions to the N queens puzzle.

    Args:
        n (int): The size of the board.
    """
    # Initialize the chessboard
    board = [[0 for x in range(n)] for y in range(n)]

    solutions = []
    solve_nqueens(board, 0, n, solutions)

    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    print_solutions(n)