# 0036 - Valid Sudoku
# Date: 2022-07-19
# Runtime: 224 ms, Memory: 13.9 MB
# Submission Id: 750347745


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for idx in range(81):
            r, c = divmod(idx, 9)
            if board[r][c] == '.':
                continue
            for i in range(9):
                if i != r and board[i][c] == board[r][c]:
                    return False
                if i != c and board[r][i] == board[r][c]:
                    return False
                nr, nc = divmod(i, 3)
                new_r = nr + r - r % 3
                new_c = nc + c - c % 3
                if (new_r, new_c) != (r,c) and board[new_r][new_c] == board[r][c]:
                    return False
        return True