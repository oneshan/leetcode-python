# 0557 - Reverse Words in a String III
# Date: 2022-12-23
# Runtime: 376 ms, Memory: 14.6 MB
# Submission Id: 864239427


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
            begin, end = begin-1, begin-1
        return ''.join(s_lst)