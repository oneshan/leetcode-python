# 0003 - Longest Substring Without Repeating Characters
# Date: 2024-01-26
# Runtime: 51 ms, Memory: 16.7 MB
# Submission Id: 1157383695


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        ans = left = 0
        for right, ch in enumerate(s):
            if ch in pos and pos[ch] >= left:
                left = pos[ch] + 1
            ans = max(ans, right - left + 1)
            pos[ch] = right
        return ans