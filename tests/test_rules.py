from textwrap import dedent

from sudoku.grid import Cell, Grid
from sudoku.rules import Rules


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


def test_find_row_candidates():
    grid = Grid.from_string("""
        . . 4 9 1 2 8 3 6
        3 . 1 7 4 8 2 5 9
        9 2 8 5 3 6 1 7 4
        4 9 2 3 8 1 7 6 5
        6 3 5 2 7 4 9 1 8
        8 1 7 6 9 5 3 4 2
        7 8 9 4 6 3 5 2 1
        2 4 3 1 5 9 6 8 7
        1 5 6 8 2 7 4 9 3
        """)

    assert Rules.find_row_candidates(grid, 0, 0) == {5, 7}
    assert Rules.find_row_candidates(grid, 0, 1) == {5, 7}
    assert Rules.find_row_candidates(grid, 1, 0) == {3}
    assert Rules.find_row_candidates(grid, 1, 1) == {6}


def test_find_column_candidates():
    grid = Grid.from_string("""
        . . 4 9 1 2 8 3 6
        3 . 1 7 4 8 2 5 9
        9 2 8 5 3 6 1 7 4
        4 9 2 3 8 1 7 6 5
        6 3 5 2 7 4 9 1 8
        8 1 7 6 9 5 3 4 2
        7 8 9 4 6 3 5 2 1
        2 4 3 1 5 9 6 8 7
        1 5 6 8 2 7 4 9 3
        """)

    assert Rules.find_column_candidates(grid, 0, 0) == {5}
    assert Rules.find_column_candidates(grid, 0, 1) == {6, 7}
    assert Rules.find_column_candidates(grid, 1, 0) == {3}
    assert Rules.find_column_candidates(grid, 1, 1) == {6, 7}


def test_find_box_candidates():
    grid = Grid.from_string("""
        . . 4 9 1 2 8 3 6
        3 . 1 7 4 8 2 5 9
        9 2 8 5 3 6 1 7 4
        4 9 2 3 8 1 7 6 5
        6 3 5 2 7 4 9 1 8
        8 1 7 6 9 5 3 4 2
        7 8 9 4 6 3 5 2 1
        2 4 3 1 5 9 6 8 7
        1 5 6 8 2 7 4 9 3
        """)

    assert Rules.find_box_candidates(grid, 0, 0) == {5, 6, 7}
    assert Rules.find_box_candidates(grid, 0, 1) == {5, 6, 7}
    assert Rules.find_box_candidates(grid, 1, 0) == {3}
    assert Rules.find_box_candidates(grid, 1, 1) == {5, 6, 7}