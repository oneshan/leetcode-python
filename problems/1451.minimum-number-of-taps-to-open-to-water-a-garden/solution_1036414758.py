# 1451 - Minimum Number of Taps to Open to Water a Garden
# Date: 2023-08-31
# Runtime: 125 ms, Memory: 16.7 MB
# Submission Id: 1036414758


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        max_reach = [0] * (n+1)
        for idx, radius in enumerate(ranges):
            _from, _to = max(0, idx-radius), min(n, idx+radius)
            max_reach[_from] = max(max_reach[_from], _to)
            
        ans = curr_end = max_end = 0
        for i in range(n+1):
            if i > max_end:
                return -1
            if i > curr_end:
                ans += 1
                curr_end = max_end
            max_end = max(max_end, max_reach[i])
        return ans