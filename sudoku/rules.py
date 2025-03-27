from sudoku.constants import BOX_SIZE
from sudoku.grid import Cell, Grid

FULL_SET = {1, 2, 3, 4, 5, 6, 7, 8, 9}


class Rules:

    @staticmethod
    def _missing_from_full_set(cells: list[Cell]) -> set[int]:
        values = {cell.value for cell in cells}
        return FULL_SET - values

    @classmethod
    def find_row_candidates(cls, grid: Grid, row_number, column_number) -> set[int]:
        cell = grid.get_cell(row_number, column_number)

        if cell.value is not None:
            return {cell.value}

        row = grid.get_row(row_number)
        return cls._missing_from_full_set(row)

    @classmethod
    def find_column_candidates(cls, grid: Grid, row_number, column_number) -> set[int]:
        cell = grid.get_cell(row_number, column_number)

        if cell.value is not None:
            return {cell.value}

        column = grid.get_column(column_number)
        return cls._missing_from_full_set(column)

    @classmethod
    def find_box_candidates(cls, grid: Grid, row_number, column_number) -> set[int]:
        horizontal = int((column_number - column_number % BOX_SIZE) / 3)
        vertical = int((row_number - row_number % BOX_SIZE) / 3)
        box = grid.get_box(horizontal, vertical)

        cell = grid.get_cell(row_number, column_number)

        if cell.value is not None:
            return {cell.value}

        return cls._missing_from_full_set(box)
