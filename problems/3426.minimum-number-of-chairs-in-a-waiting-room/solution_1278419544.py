# 3426 - Minimum Number of Chairs in a Waiting Room
# Date: 2024-06-05
# Runtime: 29 ms, Memory: 16.2 MB
# Submission Id: 1278419544


class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = count = 0
        for ch in s:
            if ch == 'E':
                count += 1
            else:
                count -= 1
            ans = max(ans, count)
        return ans