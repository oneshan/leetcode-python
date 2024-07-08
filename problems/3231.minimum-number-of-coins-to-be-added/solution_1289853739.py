# 3231 - Minimum Number of Coins to be Added
# Date: 2024-06-16
# Runtime: 538 ms, Memory: 30.4 MB
# Submission Id: 1289853739


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()

        extra = curr = 0
        for coin in coins:
            while curr < coin-1:
                curr = 2 * curr + 1
                extra += 1
            curr += coin

        while curr < target:
            curr = 2 * curr + 1
            extra += 1
        
        return extra