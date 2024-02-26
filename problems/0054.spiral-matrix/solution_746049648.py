# 0054 - Spiral Matrix
# Date: 2022-07-13
# Runtime: 48 ms, Memory: 13.8 MB
# Submission Id: 746049648


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        left, right, up, down = 0, cols-1, 0, rows-1
        
        ans = []
        while left <= right and up <= down:
            
            # left to right
            for col in range(left, right+1):
                ans.append(matrix[up][col])
            up += 1
            
            # up to down
            for row in range(up, down+1):
                ans.append(matrix[row][right])
            right -= 1
            
            # right to left
            if up <= down:
                for col in range(right, left-1, -1):
                    ans.append(matrix[down][col])
                down -= 1
            
            # down to up
            if left <= right:
                for row in range(down, up-1, -1):
                    ans.append(matrix[row][left])
                left += 1
            
        return ans