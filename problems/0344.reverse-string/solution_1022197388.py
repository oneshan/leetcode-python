# 0344 - Reverse String
# Date: 2023-08-15
# Runtime: 198 ms, Memory: 20.6 MB
# Submission Id: 1022197388


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1