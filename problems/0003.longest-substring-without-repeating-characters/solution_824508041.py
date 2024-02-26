# 0003 - Longest Substring Without Repeating Characters
# Date: 2022-10-17
# Runtime: 60 ms, Memory: 13.9 MB
# Submission Id: 824508041


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        
        left, ans = -1, 0
        for right, ch in enumerate(s):
            if ch in pos:
                left = max(left, pos[ch])
            pos[ch] = right
            ans = max(ans, right-left)
        return ans