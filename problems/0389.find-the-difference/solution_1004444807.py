# 0389 - Find the Difference
# Date: 2023-07-26
# Runtime: 62 ms, Memory: 16.4 MB
# Submission Id: 1004444807


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for ch in s:
            ans ^= ord(ch)
        for ch in t:
            ans ^= ord(ch)
        return chr(ans)