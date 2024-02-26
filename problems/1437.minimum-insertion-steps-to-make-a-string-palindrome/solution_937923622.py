# 1437 - Minimum Insertion Steps to Make a String Palindrome
# Date: 2023-04-22
# Runtime: 824 ms, Memory: 183.3 MB
# Submission Id: 937923622


class Solution:
    def minInsertions(self, s: str) -> int:
        
        @cache
        def recur(left, right):
            if left >= right:
                return 0
            
            if s[left] == s[right]:
                return recur(left+1, right-1)
            return 1 + min(recur(left+1, right),
                           recur(left, right-1))
        
        return recur(0, len(s)-1)