# 0344 - Reverse String
# Date: 2022-07-14
# Runtime: 246 ms, Memory: 18.4 MB
# Submission Id: 746516850


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left+1, right-1