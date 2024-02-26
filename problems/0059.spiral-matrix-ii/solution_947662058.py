# 0059 - Spiral Matrix II
# Date: 2023-05-10
# Runtime: 50 ms, Memory: 16.2 MB
# Submission Id: 947662058


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ans = [[0] * n for _ in range(n)]
        left, right, up, down = 0, n-1, 0, n-1
        
        idx = 1
        while left <= right and up <= down:
            
            # left to right
            for col in range(left, right+1):
                ans[up][col] = idx
                idx += 1
            up += 1
            
            # up to down
            for row in range(up, down+1):
                ans[row][right] = idx
                idx += 1
            right -= 1
            
            # right to left
            if up <= down:
                for col in range(right, left-1, -1):
                    ans[down][col] = idx
                    idx += 1
                down -= 1
            
            # down to up
            if left <= right:
                for row in range(down, up-1, -1):
                    ans[row][left] = idx
                    idx += 1
                left += 1
            
        return ans