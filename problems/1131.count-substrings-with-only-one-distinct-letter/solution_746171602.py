# 1131 - Count Substrings with Only One Distinct Letter
# Date: 2022-07-13
# Runtime: 56 ms, Memory: 13.8 MB
# Submission Id: 746171602


class Solution:
    def countLetters(self, s: str) -> int:
        prev = s[0]
        count = curr = 0
        for ch in s:
            if ch != prev:
                count += (curr + 1) * curr // 2
                curr = 1
            else:
                curr += 1
            prev = ch
        count += (curr + 1) * curr // 2
        return count