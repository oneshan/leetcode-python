# 0387 - First Unique Character in a String
# Date: 2022-07-17
# Runtime: 135 ms, Memory: 14.2 MB
# Submission Id: 748891543


class Solution:
    def firstUniqChar(self, s: str) -> int:
        last_seen = {}
        for idx in range(len(s)):
            last_seen[s[idx]] = idx
            
        for idx, ch in enumerate(s):
            if last_seen.get(ch) == idx:
                return idx
            last_seen.pop(ch, None)
        return -1