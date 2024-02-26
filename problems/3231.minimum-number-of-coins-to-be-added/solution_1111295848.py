# 3231 - Minimum Number of Coins to be Added
# Date: 2023-12-03
# Runtime: 606 ms, Memory: 30.3 MB
# Submission Id: 1111295848


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins = sorted(coins) + [target + 1]
        
        ans = curr = 0
        for coin in coins:
            while curr + 1 < coin:
                curr = 2 * curr + 1
                ans += 1
            curr += coin
            
        return ans