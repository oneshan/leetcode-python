# 0953 - Reverse Only Letters
# Date: 2023-08-17
# Runtime: 34 ms, Memory: 16.1 MB
# Submission Id: 1023774563


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_char = list(s)
        n = len(s_char)
        left, right = 0, n-1
        while left < right:
            if not s_char[left].isalpha():
                left += 1
            elif not s_char[right].isalpha():
                right -= 1
            else:
                s_char[left], s_char[right] = s_char[right], s_char[left]
                left += 1
                right -= 1
        return ''.join(s_char)