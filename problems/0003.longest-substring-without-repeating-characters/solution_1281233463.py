# 0003 - Longest Substring Without Repeating Characters
# Date: 2024-06-08
# Runtime: 53 ms, Memory: 16.6 MB
# Submission Id: 1281233463


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}

        ans = left = 0
        for right, ch in enumerate(s):
            if last_seen.get(ch, -1) >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            ans = max(ans, right-left+1)
        return ans