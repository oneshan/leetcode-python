# 1833 - Find the Highest Altitude
# Date: 2023-08-17
# Runtime: 42 ms, Memory: 16 MB
# Submission Id: 1024005042


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = curr = 0
        for diff in gain:
            curr += diff
            ans = max(ans, curr)
        return ans