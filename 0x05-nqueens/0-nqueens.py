#!/usr/bin/python3
"""N queens Solution"""


import sys


def is_safe(board, row, col):
    """Checks if placing a queen at a given position is safe

    Args:
        board (int): The chess board
        row (int): the given row
        col (int): the given column
    Returns:
        False if checks fail, True otherwise
    """
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                    return False
    return True


def solve_nqueens(N):
    """Use helper function"""
    def solve(row):
        """Helper function"""
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1)

    solutions = []
    board = [-1] * N
    solve(0)
    return solutions


def print_solutions(solutions):
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(len(solution))]
        print(formatted_solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
