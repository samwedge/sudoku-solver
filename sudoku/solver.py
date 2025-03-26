from sudoku.constants import GRID_WIDTH, BOX_SIZE
from sudoku.grid import Grid
from sudoku.rules import Rules


class Solver:
    def __init__(self, grid: Grid):
        self._grid = grid

    def solve(self) -> Grid:
        progressing = True
        while progressing:
            progressing = self._iterate()

        return self._grid

    def _iterate(self) -> bool:
        progressing = False

        for row_number in range(GRID_WIDTH):
            for column_number in range(GRID_WIDTH):
                row = self._grid.get_row(row_number)
                column = self._grid.get_column(column_number)

                horizontal = int((column_number - column_number % BOX_SIZE) / 3)
                vertical = int((row_number - row_number % BOX_SIZE) / 3)
                box = self._grid.get_box(horizontal, vertical)

                cell = row[column_number]
                if cell.value is None:
                    row_candidates = Rules.missing_from_full_set(row)
                    column_candidates = Rules.missing_from_full_set(column)
                    box_candidates = Rules.missing_from_full_set(box)

                    if len(row_candidates) == 1:
                        cell.value = list(row_candidates)[0]
                        progressing = True
                    if len(column_candidates) == 1:
                        cell.value = list(column_candidates)[0]
                        progressing = True
                    if len(box_candidates) == 1:
                        cell.value = list(box_candidates)[0]
                        progressing = True

        return progressing
