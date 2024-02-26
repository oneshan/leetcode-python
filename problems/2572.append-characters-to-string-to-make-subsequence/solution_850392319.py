# 2572 - Append Characters to String to Make Subsequence
# Date: 2022-11-27
# Runtime: 217 ms, Memory: 15.1 MB
# Submission Id: 850392319


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pt, len_t = 0, len(t)
        for idx, ch in enumerate(s):
            if t[pt] == ch:
                pt += 1
            if pt == len_t:
                return 0
        return len_t - pt