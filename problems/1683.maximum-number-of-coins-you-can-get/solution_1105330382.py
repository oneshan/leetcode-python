# 1683 - Maximum Number of Coins You Can Get
# Date: 2023-11-24
# Runtime: 527 ms, Memory: 28.9 MB
# Submission Id: 1105330382


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        
        ans = 0
        for i in range(n//3, n, 2):
            ans += piles[i]
        return ans