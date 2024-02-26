# 0686 - Repeated String Match
# Date: 2023-10-28
# Runtime: 39 ms, Memory: 16.3 MB
# Submission Id: 1085870982


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = len(b) // len(a)
        for i in range(3):
            if b in a * (count + i):
                return count + i
        return -1