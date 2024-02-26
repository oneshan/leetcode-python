# 1178 - Valid Palindrome III
# Date: 2023-10-27
# Runtime: 296 ms, Memory: 90.7 MB
# Submission Id: 1085047474


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        @cache
        def recur(left, right):
            if left > right:
                return 0
            if left == right:
                return 1
            if s[left] == s[right]:
                return recur(left+1, right-1) + 2
            return max(recur(left+1, right), recur(left, right-1))
        
        return (len(s) - recur(0, len(s)-1)) <= k