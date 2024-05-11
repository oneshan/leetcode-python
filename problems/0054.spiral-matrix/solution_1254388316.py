# 0054 - Spiral Matrix
# Date: 2024-05-10
# Runtime: 42 ms, Memory: 16.6 MB
# Submission Id: 1254388316


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        len_r, len_c = len(matrix), len(matrix[0])
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        current_d = 0
        
        ans = [matrix[0][0]]
        matrix[0][0] = 'x'

        row = col = 0
        size = len_r * len_c
        while len(ans) < size:
            next_row = row + direction[current_d][0]
            next_col = col + direction[current_d][1]
            if 0 <= next_row < len_r and 0 <= next_col < len_c and matrix[next_row][next_col] != 'x':
                row, col = next_row, next_col
                ans.append(matrix[row][col])
                matrix[row][col] = 'x'
            else:
                current_d = (current_d + 1) % 4

        return ans