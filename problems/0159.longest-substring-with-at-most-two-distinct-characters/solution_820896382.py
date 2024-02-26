# 0159 - Longest Substring with At Most Two Distinct Characters
# Date: 2022-10-12
# Runtime: 525 ms, Memory: 14.8 MB
# Submission Id: 820896382


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n
        
        table = {}
        left, ans = -1, 2
        for right, ch in enumerate(s):
            table[ch] = right
            if len(table) == 3:
                idx = min(table.values())
                table.pop(s[idx])
                left = idx
            ans = max(ans, right - left)
        return ans