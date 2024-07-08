# 1930 - Maximum Number of Consecutive Values You Can Make
# Date: 2024-06-16
# Runtime: 554 ms, Memory: 22.2 MB
# Submission Id: 1289844749


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()

        curr = 0
        for coin in coins:
            if curr < coin-1:
                break
            curr += coin
        return curr + 1