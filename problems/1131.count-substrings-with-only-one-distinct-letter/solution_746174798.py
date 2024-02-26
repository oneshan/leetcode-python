# 1131 - Count Substrings with Only One Distinct Letter
# Date: 2022-07-13
# Runtime: 55 ms, Memory: 13.8 MB
# Submission Id: 746174798


class Solution:
    def countLetters(self, s: str) -> int:
        total = left = 0
        for right in range(len(s)+1):
            if right == len(s) or s[left] != s[right]:
                len_sub = right - left
                total += (len_sub + 1) * len_sub // 2
                left = right
        return total