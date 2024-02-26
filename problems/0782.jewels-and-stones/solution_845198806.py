# 0782 - Jewels and Stones
# Date: 2022-11-17
# Runtime: 60 ms, Memory: 13.9 MB
# Submission Id: 845198806


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        return sum(stone in jewels for stone in stones)