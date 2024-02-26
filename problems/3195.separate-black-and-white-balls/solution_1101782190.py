# 3195 - Separate Black and White Balls
# Date: 2023-11-19
# Runtime: 135 ms, Memory: 17.4 MB
# Submission Id: 1101782190


class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        left, right = 0, n-1
        ans = 0
        while left < right:
            while left < right and s[left] == '0':
                left += 1
            while left < right and s[right] == '1':
                right -= 1
            ans += (right - left)
            left += 1
            right -= 1
        return ans