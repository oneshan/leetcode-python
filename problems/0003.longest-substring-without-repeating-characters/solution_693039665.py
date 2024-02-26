# 0003 - Longest Substring Without Repeating Characters
# Date: 2022-05-04
# Runtime: 79 ms, Memory: 14 MB
# Submission Id: 693039665


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        ans = start = 0
        for idx, ch in enumerate(s):
            if ch in pos and pos[ch] >= start:
                start = pos[ch] + 1
            ans = max(ans, idx - start + 1)
            pos[ch] = idx
        return ans