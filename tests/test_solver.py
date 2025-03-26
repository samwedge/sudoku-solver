"""
Example solved grid:
    5 7 4 9 1 2 8 3 6
    3 6 1 7 4 8 2 5 9
    9 2 8 5 3 6 1 7 4
    4 9 2 3 8 1 7 6 5
    6 3 5 2 7 4 9 1 8
    8 1 7 6 9 5 3 4 2
    7 8 9 4 6 3 5 2 1
    2 4 3 1 5 9 6 8 7
    1 5 6 8 2 7 4 9 3
"""
from textwrap import dedent

from sudoku.grid import Grid
from sudoku.solver import Solver


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

    expected_result = dedent("""
        5 7 4 9 1 2 8 3 6
        3 6 1 7 4 8 2 5 9
        9 2 8 5 3 6 1 7 4
        4 9 2 3 8 1 7 6 5
        6 3 5 2 7 4 9 1 8
        8 1 7 6 9 5 3 4 2
        7 8 9 4 6 3 5 2 1
        2 4 3 1 5 9 6 8 7
        1 5 6 8 2 7 4 9 3""").lstrip("\n")

    assert result.to_string() == expected_result


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

    expected_result = dedent("""
        5 7 4 9 1 2 8 3 6
        3 6 1 7 4 8 2 5 9
        9 2 8 5 3 6 1 7 4
        4 9 2 3 8 1 7 6 5
        6 3 5 2 7 4 9 1 8
        8 1 7 6 9 5 3 4 2
        7 8 9 4 6 3 5 2 1
        2 4 3 1 5 9 6 8 7
        1 5 6 8 2 7 4 9 3""").lstrip("\n")

    assert result.to_string() == expected_result


def test_box_rule():
    grid = Grid.from_string("""
    . . 4 9 1 2 8 3 .
    3 6 1 7 4 8 2 5 9
    9 2 8 5 3 6 1 7 4
    4 9 2 3 8 1 7 6 5
    6 3 5 2 7 4 9 1 8
    8 1 7 6 9 5 3 4 2
    7 8 9 4 6 3 5 2 1
    . . 3 1 5 9 6 8 .
    . . 6 8 2 7 4 9 .
    """)

    solver = Solver(grid)
    result = solver.solve()

    expected_result = dedent("""
        . . 4 9 1 2 8 3 6
        3 6 1 7 4 8 2 5 9
        9 2 8 5 3 6 1 7 4
        4 9 2 3 8 1 7 6 5
        6 3 5 2 7 4 9 1 8
        8 1 7 6 9 5 3 4 2
        7 8 9 4 6 3 5 2 1
        . . 3 1 5 9 6 8 .
        . . 6 8 2 7 4 9 .""").lstrip("\n")

    assert result.to_string() == expected_result


def test_combination_of_row_column_and_box_rules():
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

    expected_result = dedent("""
        5 7 4 9 1 2 8 3 6
        3 6 1 7 4 8 2 5 9
        9 2 8 5 3 6 1 7 4
        4 9 2 3 8 1 7 6 5
        6 3 5 2 7 4 9 1 8
        8 1 7 6 9 5 3 4 2
        7 8 9 4 6 3 5 2 1
        2 4 3 1 5 9 6 8 7
        1 5 6 8 2 7 4 9 3""").lstrip("\n")

    assert result.to_string() == expected_result
