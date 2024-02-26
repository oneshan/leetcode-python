# 0151 - Reverse Words in a String
# Date: 2024-02-17
# Runtime: 42 ms, Memory: 16.7 MB
# Submission Id: 1177726184


class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s)-1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1

        stack, word = [], []
        while left <= right:
            if s[left] != ' ':
                word.append(s[left])
            elif word:
                stack.append(''.join(word))
                word = []
            left += 1
        stack.append(''.join(word))
        return ' '.join(stack[::-1])