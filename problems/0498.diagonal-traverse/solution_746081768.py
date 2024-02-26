# 0498 - Diagonal Traverse
# Date: 2022-07-13
# Runtime: 316 ms, Memory: 17.6 MB
# Submission Id: 746081768


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        if not mat or not mat[0]:
            return []
        
        rows, cols = len(mat), len(mat[0])
        
        ans, sub = [], []
        for layer in range(rows+cols-1):
            col = layer if layer < cols else cols-1
            row = 0 if layer < cols else layer-cols+1
            while row < rows and col > -1:
                sub.append(mat[row][col])
                row += 1
                col -= 1
            
            if layer & 1:
                ans += sub
            else:
                ans += sub[::-1]
            sub = []
        
        return ans