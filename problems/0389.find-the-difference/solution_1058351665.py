# 0389 - Find the Difference
# Date: 2023-09-25
# Runtime: 46 ms, Memory: 16.3 MB
# Submission Id: 1058351665


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for ch in s:
            ans ^= ord(ch)
        for ch in t:
            ans ^= ord(ch)
        return chr(ans)