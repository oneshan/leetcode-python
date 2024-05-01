# 2128 - Reverse Prefix of Word
# Date: 2024-05-01
# Runtime: 27 ms, Memory: 16.5 MB
# Submission Id: 1246102562


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        n = len(word)

        def reverse(start, end):
            while start < end:
                word[start], word[end] = word[end], word[start]
                start += 1
                end -= 1

        for i in range(n):
            if word[i] == ch:
                reverse(0, i)
                break
        return ''.join(word)