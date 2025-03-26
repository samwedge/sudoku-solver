from sudoku.grid import Cell

FULL_SET = {1, 2, 3, 4, 5, 6, 7, 8, 9}


class Rules:

    @staticmethod
    def missing_from_full_set(cells: list[Cell]) -> set[int]:
        values = {cell.value for cell in cells}
        return FULL_SET - values
