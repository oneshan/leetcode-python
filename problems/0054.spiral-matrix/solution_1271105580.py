# 0054 - Spiral Matrix
# Date: 2024-05-29
# Runtime: 45 ms, Memory: 16.4 MB
# Submission Id: 1271105580


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        len_r, len_c = len(matrix), len(matrix[0])
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        current_d = 0
        
        ans = [matrix[0][0]]
        seen = {(0, 0)}

        r = c = d = 0
        count = len_r * len_c - 1
        while count:
            nr, nc = r + direction[d][0], c + direction[d][1]
            if 0 <= nr < len_r and 0 <= nc < len_c and (nr, nc) not in seen:
                r, c = nr, nc
                ans.append(matrix[r][c])
                seen.add((r, c))
                count -= 1
            else:
                d = (d+1) % 4

        return ans