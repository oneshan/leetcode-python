# 3337 - Count Substrings Starting and Ending with Given Character
# Date: 2024-03-17
# Runtime: 59 ms, Memory: 17.2 MB
# Submission Id: 1206129904


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        seen = ans = 0
        for idx, ch in enumerate(s):
            if ch == c:
                seen += 1
                ans += seen
        return ans