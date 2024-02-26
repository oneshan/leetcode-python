# 1476 - Count Negative Numbers in a Sorted Matrix
# Date: 2022-11-26
# Runtime: 222 ms, Memory: 15 MB
# Submission Id: 849866809


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        ans = 0
        for r in range(len_r):
            if grid[r][-1] >= 0:
                continue
            left, right = 0, len_c-1
            while left < right:
                mid = (left+right) // 2
                if grid[r][mid] >= 0:
                    left = mid + 1
                else:
                    right = mid
            ans += (len_c - left)
        return ans