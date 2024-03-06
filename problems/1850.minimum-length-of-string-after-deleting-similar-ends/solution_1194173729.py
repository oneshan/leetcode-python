# 1850 - Minimum Length of String After Deleting Similar Ends
# Date: 2024-03-05
# Runtime: 59 ms, Memory: 17.2 MB
# Submission Id: 1194173729


class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            value = s[left]
            while left <= right and s[left] == value:
                left += 1
            while left <= right and s[right] == value:
                right -= 1

        return right - left + 1