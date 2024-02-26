# 0498 - Diagonal Traverse
# Date: 2022-07-13
# Runtime: 370 ms, Memory: 18.2 MB
# Submission Id: 746075601


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        if not mat or not mat[0]:
            return []
        
        rows, cols = len(mat), len(mat[0])
        
        d = {}
        for row in range(rows):
            for col in range(cols):
                d.setdefault(row+col, [])
                d[row+col].append(mat[row][col])
        
        ans = []
        for layer, sub in d.items():
            if layer & 1:
                ans += sub
            else:
                ans += sub[::-1]
        
        return ans