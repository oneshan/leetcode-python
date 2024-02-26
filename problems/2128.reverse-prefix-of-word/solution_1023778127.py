# 2128 - Reverse Prefix of Word
# Date: 2023-08-17
# Runtime: 44 ms, Memory: 16.4 MB
# Submission Id: 1023778127


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s_char = list(word)
        
        def reverse(left, right):
            while left < right:
                s_char[left], s_char[right] = s_char[right], s_char[left]
                left += 1
                right -= 1
        
        for i in range(len(s_char)):
            if s_char[i] == ch:
                reverse(0, i)
                break
        return ''.join(s_char)