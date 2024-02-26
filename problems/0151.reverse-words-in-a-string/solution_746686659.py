# 0151 - Reverse Words in a String
# Date: 2022-07-14
# Runtime: 114 ms, Memory: 13.9 MB
# Submission Id: 746686659


class Solution:
    def reverseWords(self, s: str) -> str:
        s_char = self.trim_space(s)
        left = 0
        for idx in range(len(s_char)):
            if s_char[idx] == ' ':
                self.reverse(s_char, left, idx-1)
                left = idx+1
            elif idx == len(s_char)-1:
                self.reverse(s_char, left, idx)
        self.reverse(s_char, 0, len(s_char)-1)
        return ''.join(s_char)
    
    def reverse(self, s_char, left, right):
        while left < right:
            s_char[left], s_char[right] = s_char[right], s_char[left]
            left, right = left+1, right-1
    
    def trim_space(self, s):
        left, right = 0, len(s)-1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        
        out = []
        while left <= right:
            if s[left] != ' ':
                out.append(s[left])
            elif out[-1] != ' ':
                out.append(s[left])
            left += 1
        return out