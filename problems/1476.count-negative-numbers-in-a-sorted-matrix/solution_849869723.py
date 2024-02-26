# 1476 - Count Negative Numbers in a Sorted Matrix
# Date: 2022-11-26
# Runtime: 155 ms, Memory: 14.9 MB
# Submission Id: 849869723


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        ans = 0
        
        r, c = 0, len_c-1
        while r < len_r and c >= 0:
            if grid[r][c] < 0:
                ans += len_r - r
                c -= 1
            else:
                r += 1
        return ans