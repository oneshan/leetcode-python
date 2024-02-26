# 0387 - First Unique Character in a String
# Date: 2024-02-05
# Runtime: 77 ms, Memory: 16.7 MB
# Submission Id: 1166343191


class Solution:
    def firstUniqChar(self, s: str) -> int:
        first_seen = {}
        last_seen = {}

        for idx, ch in enumerate(s):
            if ch not in first_seen:
                first_seen[ch] = idx
            last_seen[ch] = idx

        ans = len(s)
        for ch in first_seen:
            if last_seen[ch] == first_seen[ch]:
                ans = min(ans, last_seen[ch])
        return ans if ans != len(s) else -1