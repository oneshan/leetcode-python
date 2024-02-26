# 0009 - Palindrome Number
# Date: 2022-05-10
# Runtime: 56 ms, Memory: 13.9 MB
# Submission Id: 696828717


class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        
        revert_x = 0
        while x > revert_x:
            revert_x = revert_x * 10 + x % 10
            x //= 10
        
        # 121  -- x, revert_x: 1, 12
        # 1221 -- x, revert_x: 12, 12
        return x == revert_x or x == revert_x // 10
        