from textwrap import dedent

import pytest

from sudoku.grid import Grid, Cell


@pytest.fixture
def grid() -> Grid:
    return Grid([Cell(cell_number) for cell_number in range(81)])


def test_grid_errors_unless_81_cells():
    cell = Cell(None)

    with pytest.raises(ValueError):
        Grid([cell] * 80)
        Grid([cell] * 82)
    Grid([cell] * 81)


def test_duplicate_value_in_row_throws_exception():
    with pytest.raises(ValueError):
        Grid.from_string("""
            1 1 . . . . . . .
            . . . . . . . . .
            . . . . . . . . .
            . . . . . . . . .
            . . . . . . . . .
            . . . . . . . . .
            . . . . . . . . .
            . . . . . . . . .
            . . . . . . . . .
        """)



def test_grid_returns_cells_in_row(grid: Grid):
    assert grid.get_row(0) == [Cell(0), Cell(1), Cell(2), Cell(3), Cell(4), Cell(5), Cell(6), Cell(7), Cell(8)]
    assert grid.get_row(1) == [Cell(9), Cell(10), Cell(11), Cell(12), Cell(13), Cell(14), Cell(15), Cell(16), Cell(17)]
    assert grid.get_row(8) == [Cell(72), Cell(73), Cell(74), Cell(75), Cell(76), Cell(77), Cell(78), Cell(79), Cell(80)]


def test_grid_returns_cells_in_column(grid: Grid):
    assert grid.get_column(0) == [Cell(0), Cell(9), Cell(18), Cell(27), Cell(36), Cell(45), Cell(54), Cell(63), Cell(72)]
    assert grid.get_column(1) == [Cell(1), Cell(10), Cell(19), Cell(28), Cell(37), Cell(46), Cell(55), Cell(64), Cell(73)]
    assert grid.get_column(8) == [Cell(8), Cell(17), Cell(26), Cell(35), Cell(44), Cell(53), Cell(62), Cell(71), Cell(80)]


def test_grid_returns_cells_in_box(grid: Grid):
    assert grid.get_box(0, 0) == [
        Cell(0), Cell(1), Cell(2),
        Cell(9), Cell(10), Cell(11),
        Cell(18), Cell(19), Cell(20),
    ]

    assert grid.get_box(2, 0) == [
        Cell(6), Cell(7), Cell(8),
        Cell(15), Cell(16), Cell(17),
        Cell(24), Cell(25), Cell(26),
    ]

    assert grid.get_box(2, 2) == [
        Cell(60), Cell(61), Cell(62),
        Cell(69), Cell(70), Cell(71),
        Cell(78), Cell(79), Cell(80),
    ]


def test_grid_from_string():
    grid = Grid.from_string(
        '''
        1 2 . 4 5 6 7 . 9
        1 2 3 4 5 6 7 8 9
        . 2 3 4 5 6 7 8 9
        1 2 3 4 5 6 7 8 9
        1 2 3 4 5 6 7 8 9
        1 2 3 4 5 6 7 8 9
        . 2 3 4 5 6 7 8 9
        1 2 3 4 5 6 7 8 9
        1 2 3 4 5 6 7 8 9
        '''
    )

    assert grid.get_row(0) == [Cell(1), Cell(2), Cell(None), Cell(4), Cell(5), Cell(6), Cell(7), Cell(None), Cell(9)]
    assert grid.get_column(0) == [Cell(1), Cell(1), Cell(None), Cell(1), Cell(1), Cell(1), Cell(None), Cell(1), Cell(1)]


def test_grid_to_string():
    cells = [
        Cell(1), Cell(2), Cell(3), Cell(4), Cell(5), Cell(6), Cell(None), Cell(8), Cell(9),
        Cell(1), Cell(2), Cell(3), Cell(4), Cell(5), Cell(6), Cell(7), Cell(8), Cell(9),
        Cell(1), Cell(2), Cell(3), Cell(4), Cell(5), Cell(6), Cell(7), Cell(8), Cell(9),
        Cell(1), Cell(2), Cell(3), Cell(4), Cell(5), Cell(6), Cell(7), Cell(8), Cell(9),
        Cell(1), Cell(2), Cell(3), Cell(4), Cell(None), Cell(6), Cell(7), Cell(8), Cell(9),
        Cell(1), Cell(2), Cell(3), Cell(4), Cell(5), Cell(6), Cell(7), Cell(8), Cell(9),
        Cell(1), Cell(2), Cell(3), Cell(4), Cell(5), Cell(6), Cell(7), Cell(8), Cell(9),
        Cell(1), Cell(2), Cell(3), Cell(4), Cell(5), Cell(6), Cell(7), Cell(8), Cell(9),
        Cell(1), Cell(2), Cell(None), Cell(4), Cell(5), Cell(6), Cell(7), Cell(8), Cell(9)
    ]

    grid = Grid(cells)

    assert grid.to_string() == dedent("""
        1 2 3 4 5 6 . 8 9
        1 2 3 4 5 6 7 8 9
        1 2 3 4 5 6 7 8 9
        1 2 3 4 5 6 7 8 9
        1 2 3 4 . 6 7 8 9
        1 2 3 4 5 6 7 8 9
        1 2 3 4 5 6 7 8 9
        1 2 3 4 5 6 7 8 9
        1 2 . 4 5 6 7 8 9""").lstrip("\n")
