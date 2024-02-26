# 0036 - Valid Sudoku
# Date: 2022-07-19
# Runtime: 203 ms, Memory: 14 MB
# Submission Id: 750353005


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        for idx in range(81):
            r, c = divmod(idx, 9)
            if board[r][c] == '.':
                continue
            val = int(board[r][c]) - 1
            pos = 1 << (int(board[r][c]) - 1)
            rc = (r//3) * 3 + c // 3
            
            if rows[r] & pos:
                return False
            if cols[c] & pos:
                return False
            if boxes[rc] & pos:
                return False
            
            rows[r] |= pos
            cols[c] |= pos
            boxes[rc] |= pos
            
        return True