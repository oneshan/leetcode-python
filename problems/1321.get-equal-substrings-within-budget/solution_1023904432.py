# 1321 - Get Equal Substrings Within Budget
# Date: 2023-08-17
# Runtime: 78 ms, Memory: 17.7 MB
# Submission Id: 1023904432


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        
        diff = [0] * n
        for idx, (c1, c2) in enumerate(zip(s, t)):
            diff[idx] = abs(ord(c1)-ord(c2))
        
        ans = left = curr = 0
        for right in range(n):
            curr += diff[right]
            while curr > maxCost:
                curr -= diff[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans