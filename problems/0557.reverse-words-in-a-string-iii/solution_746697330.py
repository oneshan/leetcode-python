# 0557 - Reverse Words in a String III
# Date: 2022-07-14
# Runtime: 152 ms, Memory: 14.6 MB
# Submission Id: 746697330


class Solution:
    def reverseWords(self, s: str) -> str:
        s_char = list(s)
        
        left = 0
        for idx in range(len(s)):
            if s[idx] == ' ':
                self.reverse(s_char, left, idx-1)
                left = idx + 1
            elif idx == len(s)-1:
                self.reverse(s_char, left, idx)
            
        return ''.join(s_char)
    
    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left+1, right-1