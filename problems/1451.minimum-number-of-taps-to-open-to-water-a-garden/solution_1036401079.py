# 1451 - Minimum Number of Taps to Open to Water a Garden
# Date: 2023-08-31
# Runtime: 117 ms, Memory: 18 MB
# Submission Id: 1036401079


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        intervals = sorted((max(0, i-r), min(n, i+r)) for i, r in enumerate(ranges))
        len_r = len(ranges)
        idx = curr_end = max_end = ans = 0
        while curr_end < n:
            while idx < len_r and intervals[idx][0] <= curr_end:
                max_end = max(max_end, intervals[idx][1])
                idx += 1
            if curr_end == max_end:
                return -1
            curr_end = max_end
            ans += 1
        return ans