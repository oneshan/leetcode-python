# 0036 - Valid Sudoku
# Date: 2024-02-21
# Runtime: 102 ms, Memory: 16.6 MB
# Submission Id: 1181612527


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        blocks = [0] * 9
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                b = (r // 3) * 3 + (c // 3)
                mask = 1 << int(board[r][c])
                if rows[r] & mask or cols[c] & mask or blocks[b] & mask:
                    return False
                rows[r] |= mask
                cols[c] |= mask
                blocks[b] |= mask
        return True