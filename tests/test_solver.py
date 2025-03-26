from textwrap import dedent

from sudoku.grid import Grid
from sudoku.solver import Solver


SOLVED_GRID = dedent("""
        5 7 4 9 1 2 8 3 6
        3 6 1 7 4 8 2 5 9
        9 2 8 5 3 6 1 7 4
        4 9 2 3 8 1 7 6 5
        6 3 5 2 7 4 9 1 8
        8 1 7 6 9 5 3 4 2
        7 8 9 4 6 3 5 2 1
        2 4 3 1 5 9 6 8 7
        1 5 6 8 2 7 4 9 3""").lstrip("\n")


def test_row_rule():
    grid = Grid.from_string("""
    5 7 4 9 1 2 8 3 .
    3 6 1 7 4 8 2 5 .
    9 2 8 5 3 6 1 7 .
    4 9 2 3 8 1 7 6 .
    6 3 5 2 7 4 9 1 .
    8 1 7 6 9 5 3 4 .
    7 8 9 4 6 3 5 2 .
    2 4 3 1 5 9 6 8 .
    1 5 6 8 2 7 4 9 .
    """)

    solver = Solver(grid)
    result = solver.solve()

    assert result.to_string() == SOLVED_GRID


def test_column_rule():
    grid = Grid.from_string("""
    . . . . . . . . .
    3 6 1 7 4 8 2 5 9
    9 2 8 5 3 6 1 7 4
    4 9 2 3 8 1 7 6 5
    6 3 5 2 7 4 9 1 8
    8 1 7 6 9 5 3 4 2
    7 8 9 4 6 3 5 2 1
    2 4 3 1 5 9 6 8 7
    1 5 6 8 2 7 4 9 3
    """)

    solver = Solver(grid)
    result = solver.solve()

    assert result.to_string() == SOLVED_GRID


def test_combination_of_row_column_and_box_rules_where_rules_can_be_applied_iteratively():
    grid = Grid.from_string("""
    . . 4 9 1 2 8 3 .
    3 6 1 7 4 8 2 5 .
    9 2 8 5 3 6 1 7 4
    4 9 2 3 8 1 7 6 5
    6 3 5 2 7 4 9 1 8
    8 1 7 6 9 5 3 4 2
    7 8 9 4 6 3 5 2 1
    2 4 3 1 5 9 6 8 7
    . 5 6 8 2 7 4 9 .
    """)

    solver = Solver(grid)
    result = solver.solve()

    assert result.to_string() == SOLVED_GRID


def test_combination_of_row_column_and_box_rules_where_rules_must_be_applied_together():
    grid = Grid.from_string("""
    5 7 4 9 1 2 8 . .
    3 6 1 7 4 8 2 . .
    9 2 8 5 3 6 1 7 4
    4 9 2 3 8 1 7 6 5
    6 3 5 2 7 4 9 1 8
    8 1 7 6 9 5 3 4 2
    7 8 9 4 6 3 5 2 1
    2 4 3 1 5 9 6 8 7
    1 5 6 8 2 7 4 9 3
    """)

    solver = Solver(grid)
    result = solver.solve()

    assert result.to_string() == SOLVED_GRID


def test_on_easy_sudoku():
    grid = Grid.from_string("""
        4 8 1 3 . . . 7 .
        5 . 7 9 8 2 . . .
        3 . . 1 . . . 6 8
        . 3 . . . . 1 8 5
        . 9 . . 2 5 . . 4
        . 7 . 4 . 3 . . 9
        . . . 2 9 . 8 . .
        6 1 2 . . . 4 . .
        . . 8 . 4 7 2 1 .
    """)

    solver = Solver(grid)
    result = solver.solve()

    solution = dedent("""
        4 8 1 3 5 6 9 7 2
        5 6 7 9 8 2 3 4 1
        3 2 9 1 7 4 5 6 8
        2 3 4 7 6 9 1 8 5
        1 9 6 8 2 5 7 3 4
        8 7 5 4 1 3 6 2 9
        7 4 3 2 9 1 8 5 6
        6 1 2 5 3 8 4 9 7
        9 5 8 6 4 7 2 1 3""").lstrip("\n")

    assert result.to_string() == solution
