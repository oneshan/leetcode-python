# 3379 - Score of a String
# Date: 2024-06-01
# Runtime: 36 ms, Memory: 16.4 MB
# Submission Id: 1273790055


class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            ans += abs(ord(s[i]) - ord(s[i-1]))
        return ans