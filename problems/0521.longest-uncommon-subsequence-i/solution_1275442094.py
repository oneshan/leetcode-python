# 0521 - Longest Uncommon Subsequence I
# Date: 2024-06-02
# Runtime: 35 ms, Memory: 16.4 MB
# Submission Id: 1275442094


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))