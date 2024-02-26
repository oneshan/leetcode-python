# 0389 - Find the Difference
# Date: 2022-09-16
# Runtime: 36 ms, Memory: 14 MB
# Submission Id: 801307609


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for ch in s:
            ans ^= ord(ch)
        for ch in t:
            ans ^= ord(ch)
        return chr(ans)