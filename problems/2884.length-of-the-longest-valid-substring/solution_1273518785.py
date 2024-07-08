# 2884 - Length of the Longest Valid Substring
# Date: 2024-06-01
# Runtime: 1299 ms, Memory: 35.4 MB
# Submission Id: 1273518785


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        ans = left = 0

        for right in range(len(word)):
            for i in range(max(left, right-9), right+1):
                if word[i:right+1] in forbidden:
                    left = i + 1
            ans = max(ans, right - left + 1)
        return ans