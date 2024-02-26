# 0151 - Reverse Words in a String
# Date: 2022-07-14
# Runtime: 43 ms, Memory: 13.9 MB
# Submission Id: 746695024


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
                word += s[left]
            elif word:
                stack.append(''.join(word))
                word = []
            left += 1
        stack.append(''.join(word))
        
        return ' '.join(stack[::-1])
            
    def trim_space(self, s):
        
        out = []
        while left <= right:
            if s[left] != ' ':
                out.append(s[left])
            elif out[-1] != ' ':
                out.append(s[left])
            left += 1
        return out