# 0782 - Jewels and Stones
# Date: 2022-07-17
# Runtime: 72 ms, Memory: 13.8 MB
# Submission Id: 749247503


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        return sum(stone in jewels for stone in stones)            