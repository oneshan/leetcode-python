# 0003 - Longest Substring Without Repeating Characters
# Date: 2022-07-17
# Runtime: 105 ms, Memory: 14.1 MB
# Submission Id: 749256889


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        ans, start = 0, 0
        for idx, ch in enumerate(s):
            if ch in pos and pos[ch] >= start:
                start = pos[ch] + 1
            ans = max(ans, idx - start + 1)
            pos[ch] = idx
        return ans