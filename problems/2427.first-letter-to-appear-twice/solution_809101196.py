# 2427 - First Letter to Appear Twice
# Date: 2022-09-26
# Runtime: 42 ms, Memory: 13.8 MB
# Submission Id: 809101196


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)