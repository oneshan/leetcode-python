# 0003 - Longest Substring Without Repeating Characters
# Date: 2023-08-23
# Runtime: 58 ms, Memory: 16.4 MB
# Submission Id: 1029648534


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        left = ans = 0
        for right, ch in enumerate(s):
            if ch in pos and pos[ch] >= left:
                left = pos[ch] + 1
            ans = max(ans, right - left + 1)
            pos[ch] = right
        return ans