# 0557 - Reverse Words in a String III
# Date: 2023-08-04
# Runtime: 86 ms, Memory: 16.9 MB
# Submission Id: 1012188005


class Solution:
    def reverseWords(self, s: str) -> str:
        s_lst = list(s)
        
        def reverse(left, right):
            while left < right:
                s_lst[left], s_lst[right] = s_lst[right], s_lst[left]
                left += 1
                right -= 1
        
        begin = end = len(s)-1
        while begin >= 0:
            while begin >= 0 and s[begin] != ' ':
                begin -= 1
            reverse(begin+1, end)
            begin = end = begin-1
        return ''.join(s_lst)