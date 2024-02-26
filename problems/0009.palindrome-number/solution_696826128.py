# 0009 - Palindrome Number
# Date: 2022-05-10
# Runtime: 72 ms, Memory: 14 MB
# Submission Id: 696826128


class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        def reverse(num):
            ans = 0
            while num > 0:
                ans = ans * 10 + num % 10
                num //= 10
            return ans
        
        return x == reverse(x)