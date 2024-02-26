# 0003 - Longest Substring Without Repeating Characters
# Date: 2024-02-22
# Runtime: 46 ms, Memory: 16.7 MB
# Submission Id: 1182689540


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        ans = left = 0
        for right, ch in enumerate(s):
            if table.get(ch, -1) >= left:
                left = table[ch] + 1
            table[ch] = right
            ans = max(ans, right-left+1)
        return ans