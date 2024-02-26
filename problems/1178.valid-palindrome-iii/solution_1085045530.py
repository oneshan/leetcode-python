# 1178 - Valid Palindrome III
# Date: 2023-10-27
# Runtime: 306 ms, Memory: 84.5 MB
# Submission Id: 1085045530


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        @cache
        def recur(left, right):
            if left == right:
                return 0
            if left == right - 1:
                return 1 if s[left] != s[right] else 0
            
            if s[left] == s[right]:
                return recur(left+1, right-1)
            return 1 + min(recur(left, right-1), recur(left+1, right))
        
        return recur(0, len(s)-1) <= k