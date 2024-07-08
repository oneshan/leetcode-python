# 1460 - Number of Substrings Containing All Three Characters
# Date: 2024-06-02
# Runtime: 111 ms, Memory: 16.8 MB
# Submission Id: 1274358346


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos = [-1] * 3
        ans = 0
        for idx, ch in enumerate(s):
            pos[ord(ch)-ord('a')] = idx
            ans += 1 + min(pos)
        return ans