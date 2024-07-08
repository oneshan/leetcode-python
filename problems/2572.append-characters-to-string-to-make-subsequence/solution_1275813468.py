# 2572 - Append Characters to String to Make Subsequence
# Date: 2024-06-03
# Runtime: 50 ms, Memory: 17.6 MB
# Submission Id: 1275813468


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for ch in s:
            if ch == t[i]:
                i += 1
                if i == len(t):
                    return 0
        return len(t)-i