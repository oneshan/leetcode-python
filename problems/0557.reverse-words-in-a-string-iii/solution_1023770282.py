# 0557 - Reverse Words in a String III
# Date: 2023-08-17
# Runtime: 75 ms, Memory: 16.9 MB
# Submission Id: 1023770282


class Solution:
    def reverseWords(self, s: str) -> str:
        lst = list(s)
        n = len(s)
        
        def reverse(i, j):
            while i < j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1

        
        left = 0
        for right in range(n):
            if lst[right] == ' ':
                reverse(left, right-1)
                left = right + 1
        reverse(left, right)
        return ''.join(lst)