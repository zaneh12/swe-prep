from typing import List
from collections import defaultdict

class Solution:
    """
    Validates a partially filled 9x9 Sudoku board.
    Ensures each row, column, and 3x3 sub-box contains unique digits (1-9).
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Returns True if the board is valid. Empty cells are marked as '.'.
        Time: O(1) since the board size is fixed at 9x9.
        reviewed at 5/14 to know the // // trick. and also its a set not list so we can do O(1) lookups.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)  # key = (row // 3, col // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if (val in rows[r] or
                    val in cols[c] or
                    val in boxes[(r // 3, c // 3)]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)

        return True


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "1", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(sol.isValidSudoku(board))  # Expected: False
