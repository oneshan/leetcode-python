# 0036 - Valid Sudoku
# Date: 2022-11-23
# Runtime: 254 ms, Memory: 13.8 MB
# Submission Id: 848583725


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        col = [0] * 9
        block = [0] * 9
        
        for idx in range(81):
            r, c = divmod(idx, 9)
            b = (r // 3) * 3 + (c // 3)
            
            if board[r][c] == '.':
                continue
            mask = 1 << (int(board[r][c])-1)
            if row[r] & mask or col[c] & mask or block[b] & mask:
                return False
            row[r] |= mask
            col[c] |= mask
            block[b] |= mask

        return True