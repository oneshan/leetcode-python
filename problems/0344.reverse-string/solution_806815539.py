# 0344 - Reverse String
# Date: 2022-09-23
# Runtime: 437 ms, Memory: 18.5 MB
# Submission Id: 806815539


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