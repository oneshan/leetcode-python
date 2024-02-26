# 0387 - First Unique Character in a String
# Date: 2024-02-05
# Runtime: 70 ms, Memory: 16.7 MB
# Submission Id: 1166345182


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for idx, ch in enumerate(s):
            if ch not in seen:
                seen[ch] = idx
            else:
                seen[ch] = -1

        for ch in seen:
            if seen[ch] != -1:
                return seen[ch]
        return -1