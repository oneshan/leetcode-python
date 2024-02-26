# 1630 - Count Odd Numbers in an Interval Range
# Date: 2023-02-13
# Runtime: 36 ms, Memory: 13.8 MB
# Submission Id: 896969697


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low & 1 == 0:
            low += 1
        if high & 1 == 0:
            high -= 1
        if low > high:
            return 0
        return 1 + (high - low) // 2