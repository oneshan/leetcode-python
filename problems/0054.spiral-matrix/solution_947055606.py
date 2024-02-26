# 0054 - Spiral Matrix
# Date: 2023-05-09
# Runtime: 51 ms, Memory: 16.4 MB
# Submission Id: 947055606


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        len_r, len_c = len(matrix), len(matrix[0])
        
        left, right, up, down = 0, len_c-1, 0, len_r-1
        while len(ans) < len_r * len_c:
            
            # left to right
            for c in range(left, right+1):
                ans.append(matrix[up][c])
                
            # up to down
            for r in range(up+1, down+1):
                ans.append(matrix[r][right])
            
            # right to left
            if up != down:
                for c in range(right-1, left-1, -1):
                    ans.append(matrix[down][c])
                
            # down to up
            if left != right:
                for r in range(down-1, up, -1):
                    ans.append(matrix[r][left])
                
            left += 1
            right -= 1
            up += 1
            down -= 1
        
        return ans
                