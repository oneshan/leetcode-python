# 1178 - Valid Palindrome III
# Date: 2022-11-03
# Runtime: 1541 ms, Memory: 87.9 MB
# Submission Id: 835958870


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        memo = {}
        
        def check(left, right):
            if left == right:
                return 0
            if left == right-1:
                return s[left] != s[right]
            
            if (left, right) not in memo:
                if s[left] == s[right]:
                    memo[(left, right)] = check(left+1, right-1)
                else:
                    memo[(left, right)] = 1 + min(check(left+1, right), check(left, right-1))
            return memo[(left,right)]
        
        return check(0, len(s)-1) <= k