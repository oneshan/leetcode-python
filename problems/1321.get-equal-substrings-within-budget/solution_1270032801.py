# 1321 - Get Equal Substrings Within Budget
# Date: 2024-05-28
# Runtime: 63 ms, Memory: 17.3 MB
# Submission Id: 1270032801


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)

        ans = 0
        left = curr = 0
        for right in range(n):
            curr += abs(ord(s[right]) - ord(t[right]))
            while curr > maxCost:
                curr -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right-left+1)
        return ans