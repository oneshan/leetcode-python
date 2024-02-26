# 0782 - Jewels and Stones
# Date: 2023-08-23
# Runtime: 43 ms, Memory: 16.2 MB
# Submission Id: 1029644467


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        return sum(stone in jewels for stone in stones)