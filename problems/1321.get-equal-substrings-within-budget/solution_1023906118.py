# 1321 - Get Equal Substrings Within Budget
# Date: 2023-08-17
# Runtime: 81 ms, Memory: 17.2 MB
# Submission Id: 1023906118


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        
        ans = left = curr = 0
        for right in range(n):
            curr += abs(ord(s[right]) - ord(t[right]))
            while curr > maxCost:
                curr -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans