# 1833 - Find the Highest Altitude
# Date: 2023-06-19
# Runtime: 43 ms, Memory: 16.4 MB
# Submission Id: 974541957


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = curr_h = 0
        for diff in gain:
            curr_h += diff
            ans = max(ans, curr_h)
        return ans