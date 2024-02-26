# 1240 - Stone Game II
# Date: 2023-05-26
# Runtime: 693 ms, Memory: 20.1 MB
# Submission Id: 957724467


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        @cache
        def dp(p, i, m):
            if i == n:
                return 0

            curr = 0
            ans = 1000000 if p == 1 else -1
            for j in range(min(2*m, n-i)):
                curr += piles[i+j]
                if p == 0:
                    ans = max(ans, curr + dp(1, i+j+1, max(m, j+1)))
                else:
                    ans = min(ans, dp(0, i+j+1, max(m, j+1)))
            return ans
        
        return dp(0, 0, 1)