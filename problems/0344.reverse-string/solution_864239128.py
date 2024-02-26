# 0344 - Reverse String
# Date: 2022-12-23
# Runtime: 205 ms, Memory: 18.4 MB
# Submission Id: 864239128


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