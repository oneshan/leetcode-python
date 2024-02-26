# 0125 - Valid Palindrome
# Date: 2022-10-18
# Runtime: 100 ms, Memory: 19.2 MB
# Submission Id: 825196445


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lst = [ch.lower() for ch in s if ch.isalnum()]
        left, right = 0, len(s_lst)-1
        while left < right:
            if s_lst[left] != s_lst[right]:
                return False
            left += 1
            right -= 1
        return True