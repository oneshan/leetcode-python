# 0058 - Length of Last Word
# Date: 2023-10-18
# Runtime: 36 ms, Memory: 16.3 MB
# Submission Id: 1077670227


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = len(s) - 1
        while right >= 0 and s[right] == ' ':
            right -= 1

        left = right
        while left >= 0 and s[left] != ' ':
            left -= 1
        return right - left