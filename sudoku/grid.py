from __future__ import annotations

from dataclasses import dataclass

from sudoku.constants import GRID_WIDTH, BOX_SIZE

NULL_CHARACTER = "."


@dataclass
class Cell:
    value: int | None


class Grid:
    def __init__(self, cells: list[Cell]):
        self._cells = cells
        self._validate_number_of_cells()
        self._validate_no_duplicates_in_rows()
        self._validate_no_duplicates_in_columns()
        self._validate_no_duplicates_in_boxes()

    @classmethod
    def from_string(cls, string) -> Grid:
        cells = []

        for s_number in string.replace('\n', ' ').split(' '):
            if s_number != '':
                if s_number == NULL_CHARACTER:
                    cells.append(Cell(None))
                else:
                    cells.append(Cell(int(s_number)))

        return Grid(cells)

    def to_string(self) -> str:
        row_strings = []
        for row_number in range(GRID_WIDTH):
            row_numbers_as_strings = []
            for cell in self.get_row(row_number):
                if cell.value is None:
                    row_numbers_as_strings.append(NULL_CHARACTER)
                else:
                    row_numbers_as_strings.append(str(cell.value))
            row_strings.append(' '.join(row_numbers_as_strings))

        return '\n'.join(row_strings)

    def get_row(self, row_number: int) -> list[Cell]:
        start_offset = GRID_WIDTH * row_number
        end_offset = GRID_WIDTH
        return self._cells[start_offset:start_offset + end_offset]

    def get_column(self, column_number: int) -> list[Cell]:
        start_offset = GRID_WIDTH * column_number
        end_offset = GRID_WIDTH ** 2 + column_number
        step_size = GRID_WIDTH
        return self._cells[column_number:start_offset + end_offset:step_size]

    def get_box(self, horizontal: int, vertical: int) -> list[Cell]:
        row_1 = self.get_row(vertical * BOX_SIZE)
        row_2 = self.get_row(vertical * BOX_SIZE + 1)
        row_3 = self.get_row(vertical * BOX_SIZE + 2)

        cells_in_row_1 = row_1[horizontal * BOX_SIZE:horizontal * BOX_SIZE + BOX_SIZE]
        cells_in_row_2 = row_2[horizontal * BOX_SIZE:horizontal * BOX_SIZE + BOX_SIZE]
        cells_in_row_3 = row_3[horizontal * BOX_SIZE:horizontal * BOX_SIZE + BOX_SIZE]

        return cells_in_row_1 + cells_in_row_2 + cells_in_row_3

    def _validate_number_of_cells(self):
        if len(self._cells) != GRID_WIDTH ** 2:
            raise ValueError(f"Invalid grid size: {len(self._cells)}. Should be 81")

    def _validate_no_duplicates_in_rows(self):
        for row_number in range(GRID_WIDTH):
            cells = self.get_row(row_number)
            values_in_row = [cell.value for cell in cells if cell.value is not None]

            if len(set(values_in_row)) != len(values_in_row):
                raise ValueError(f"Duplicate values found in row: {row_number}")

    def _validate_no_duplicates_in_columns(self):
        for column_number in range(GRID_WIDTH):
            cells = self.get_column(column_number)
            values_in_column = [cell.value for cell in cells if cell.value is not None]

            if len(set(values_in_column)) != len(values_in_column):
                raise ValueError(f"Duplicate values found in column: {column_number}")

    def _validate_no_duplicates_in_boxes(self):
        for horizontal in range(BOX_SIZE):
            for vertical in range(BOX_SIZE):
                cells = self.get_box(horizontal, vertical)
                values_in_box = [cell.value for cell in cells if cell.value is not None]

                if len(set(values_in_box)) != len(values_in_box):
                    raise ValueError(f"Duplicate values found in box: {horizontal}, {vertical}")

