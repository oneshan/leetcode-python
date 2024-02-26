# 0003 - Longest Substring Without Repeating Characters
# Date: 2022-10-12
# Runtime: 153 ms, Memory: 14.2 MB
# Submission Id: 820898151


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        left, ans = -1, 0
        for right, ch in enumerate(s):
            if ch in table:
                left = max(left, table[ch])
            table[ch] = right
            ans = max(ans, right-left)
        return ans