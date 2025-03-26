from sudoku.grid import Cell
from sudoku.rules import Rules


def test_missing_from_full_set():
    cells = [Cell(1), Cell(2), Cell(3), Cell(4), Cell(5), Cell(None), Cell(7), Cell(None), Cell(9)]

    candidates = Rules.missing_from_full_set(cells)

    assert candidates == {6, 8}
