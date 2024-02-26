# 1683 - Maximum Number of Coins You Can Get
# Date: 2023-11-24
# Runtime: 536 ms, Memory: 28.8 MB
# Submission Id: 1105329214


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        
        ans = 0
        left, right = 0, n-1
        while left < right:
            left += 1
            right -= 1
            ans += piles[right]
            right -= 1
        return ans