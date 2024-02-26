# 0557 - Reverse Words in a String III
# Date: 2023-10-01
# Runtime: 78 ms, Memory: 17 MB
# Submission Id: 1063556822


class Solution:
    def reverseWords(self, s: str) -> str:
        s_lst = list(s)
        
        def reverse(left, right):
            while left < right:
                s_lst[left], s_lst[right] = s_lst[right], s_lst[left]
                left += 1
                right -= 1
        
        left = 0
        for right, ch in enumerate(s):
            if ch == ' ':
                reverse(left, right-1)
                left = right + 1
        reverse(left, len(s)-1)
        return ''.join(s_lst)