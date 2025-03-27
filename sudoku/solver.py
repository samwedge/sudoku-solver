import logging

from sudoku.constants import GRID_WIDTH
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
                cell = self._grid.get_cell(row_number, column_number)
                if cell.value is None:
                    row_candidates = Rules.find_row_candidates(self._grid, row_number, column_number)
                    column_candidates = Rules.find_column_candidates(self._grid, row_number, column_number)
                    box_candidates = Rules.find_box_candidates(self._grid, row_number, column_number)

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
