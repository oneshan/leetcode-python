# 0151 - Reverse Words in a String
# Date: 2022-07-14
# Runtime: 48 ms, Memory: 14.1 MB
# Submission Id: 746691510


from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s)-1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        
        tokens, word = deque(), []
        while left <= right:
            if s[left] != ' ':
                word += s[left]
            elif word:
                tokens.appendleft(''.join(word))
                word = []
            left += 1
        tokens.appendleft(''.join(word))
        return ' '.join(tokens)
            
    def trim_space(self, s):
        
        out = []
        while left <= right:
            if s[left] != ' ':
                out.append(s[left])
            elif out[-1] != ' ':
                out.append(s[left])
            left += 1
        return out