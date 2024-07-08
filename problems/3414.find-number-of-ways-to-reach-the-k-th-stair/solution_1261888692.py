# 3414 - Find Number of Ways to Reach the K-th Stair
# Date: 2024-05-19
# Runtime: 126 ms, Memory: 18.4 MB
# Submission Id: 1261888692


class Solution:
    def waysToReachStair(self, k: int) -> int:
        if k == 0:
            return 2
        
        @cache
        def dp(j, jump, first):
            if j >= k+2:
                return 0
            
            res, next_jump = 0, 2 ** jump            
            if j == k:
                res += 1
            if j >= 1 and not first:
                res += dp(j-1, jump, True)
            if j + next_jump < k + 2:
                res += dp(j + next_jump, jump+1, False)
            return res


        return dp(1, 0, False)