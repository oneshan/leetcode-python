# 3328 - Apply Operations to Make Sum of Array Greater Than or Equal to k
# Date: 2024-03-24
# Runtime: 206 ms, Memory: 16.6 MB
# Submission Id: 1212167309


class Solution:
    def minOperations(self, k: int) -> int:
        
        ans = k
        for n in range(k+1):
            m = floor((k-1) / (1 + n))
            if (1 + n) * (1 + m) >= k:
                ans = min(ans, m+n)
        return ans