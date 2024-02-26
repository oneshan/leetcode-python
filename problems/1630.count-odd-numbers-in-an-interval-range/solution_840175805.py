# 1630 - Count Odd Numbers in an Interval Range
# Date: 2022-11-10
# Runtime: 24 ms, Memory: 13.8 MB
# Submission Id: 840175805


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low & 1 == 0:
            low += 1
        if high & 1 == 0:
            high -= 1
        return 1 + (high-low) // 2