# 1630 - Count Odd Numbers in an Interval Range
# Date: 2022-11-10
# Runtime: 41 ms, Memory: 13.9 MB
# Submission Id: 840175102


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        if low & 1:
            low += 1
            ans += 1
        if high & 1:
            high -= 1
            ans += 1
        return ans + (high-low) // 2