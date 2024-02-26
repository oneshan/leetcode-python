# 0003 - Longest Substring Without Repeating Characters
# Date: 2023-10-09
# Runtime: 67 ms, Memory: 16.4 MB
# Submission Id: 1070993754


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