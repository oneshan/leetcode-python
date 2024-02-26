# 0125 - Valid Palindrome
# Date: 2024-02-10
# Runtime: 38 ms, Memory: 17 MB
# Submission Id: 1171070149


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True