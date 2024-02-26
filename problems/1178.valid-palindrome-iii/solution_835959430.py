# 1178 - Valid Palindrome III
# Date: 2022-11-03
# Runtime: 1436 ms, Memory: 87.8 MB
# Submission Id: 835959430


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        memo = {}
        
        def check(left, right):
            if left == right:
                return 0
            if left == right-1:
                return 1 if s[left] != s[right] else 0
            
            if (left, right) not in memo:
                if s[left] == s[right]:
                    memo[(left, right)] = check(left+1, right-1)
                else:
                    memo[(left, right)] = 1 + min(check(left+1, right), check(left, right-1))
            return memo[(left,right)]
        
        return check(0, len(s)-1) <= k