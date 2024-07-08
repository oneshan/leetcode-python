# 0344 - Reverse String
# Date: 2024-06-02
# Runtime: 172 ms, Memory: 21 MB
# Submission Id: 1274902127


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