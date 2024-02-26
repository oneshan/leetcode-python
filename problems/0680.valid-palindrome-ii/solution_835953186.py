# 0680 - Valid Palindrome II
# Date: 2022-11-03
# Runtime: 558 ms, Memory: 17.3 MB
# Submission Id: 835953186


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(left, right, has_delete=False):
            while left < right:
                if s[left] != s[right]:
                    if has_delete:
                        return False
                    return check(left+1, right, True) or check(left, right-1, True)
                left += 1
                right -= 1
            return True
        
        return check(0, len(s)-1)