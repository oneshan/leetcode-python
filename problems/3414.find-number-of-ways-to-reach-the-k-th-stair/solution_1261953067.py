# 3414 - Find Number of Ways to Reach the K-th Stair
# Date: 2024-05-19
# Runtime: 37 ms, Memory: 16.5 MB
# Submission Id: 1261953067


class Solution:
    def waysToReachStair(self, k: int) -> int:
        
        ans = 0
        for jump in range(40):
            curr_stairs = 1 << jump
            if curr_stairs >= k:
                ans += math.comb(jump + 1, curr_stairs - k)
        return ans