# 0054 - Spiral Matrix
# Date: 2022-07-13
# Runtime: 43 ms, Memory: 13.9 MB
# Submission Id: 746059101


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        current_d = 0
        changed = 0
        
        row = col = 0
        ans = [matrix[row][col]]
        matrix[row][col] = 'x'

        while changed < 2:
            while True:
                next_row = row + direction[current_d][0]
                next_col = col + direction[current_d][1]
                if not (0 <= next_row < rows):
                    break
                if not (0 <= next_col < cols):
                    break
                if matrix[next_row][next_col] == 'x':
                    break
                changed = 0
                row, col = next_row, next_col
                ans.append(matrix[row][col])
                matrix[row][col] = 'x'
            current_d = (current_d + 1) % 4
            changed += 1
        return ans