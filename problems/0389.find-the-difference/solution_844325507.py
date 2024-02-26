# 0389 - Find the Difference
# Date: 2022-11-16
# Runtime: 55 ms, Memory: 13.9 MB
# Submission Id: 844325507


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for ch in s:
            ans ^= ord(ch)
        for ch in t:
            ans ^= ord(ch)
        return chr(ans)