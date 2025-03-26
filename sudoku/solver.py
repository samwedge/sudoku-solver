import logging

from sudoku.constants import GRID_WIDTH, BOX_SIZE
from sudoku.grid import Grid
from sudoku.rules import Rules


logger = logging.getLogger(__name__)


class Solver:
    def __init__(self, grid: Grid):
        self._grid = grid

    def solve(self) -> Grid:
        progressing = True
        n_iterations = 0
        while progressing:
            progressing = self._iterate()
            n_iterations += 1

        logger.info(f"Finished progressing after {n_iterations} iterations")
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

                    candidates = row_candidates & column_candidates & box_candidates

                    if len(candidates) == 1:
                        cell.value = list(candidates)[0]
                        progressing = True

        return progressing


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    result = Solver(Grid.from_string("""
        4 8 1 3 . . . 7 .
        5 . 7 9 8 2 . . .
        3 . . 1 . . . 6 8
        . 3 . . . . 1 8 5
        . 9 . . 2 5 . . 4
        . 7 . 4 . 3 . . 9
        . . . 2 9 . 8 . .
        6 1 2 . . . 4 . .
        . . 8 . 4 7 2 1 .
        """)).solve()

    logger.info(result.to_string())
