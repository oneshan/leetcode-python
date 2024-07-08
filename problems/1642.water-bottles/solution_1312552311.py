# 1642 - Water Bottles
# Date: 2024-07-07
# Runtime: 33 ms, Memory: 16.5 MB
# Submission Id: 1312552311


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            ans += (numBottles // numExchange)
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)
        return ans