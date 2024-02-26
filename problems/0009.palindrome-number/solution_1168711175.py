# 0009 - Palindrome Number
# Date: 2024-02-07
# Runtime: 71 ms, Memory: 16.4 MB
# Submission Id: 1168711175


class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        def get_reverse(num):
            res = 0
            while num:
                num, digit = divmod(num, 10)
                res = (res * 10) + digit
            return res

        if x < 0:
            return False
        return x == get_reverse(x)