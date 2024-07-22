# 3493 - Maximum Number of Operations to Move Ones to the End
# Date: 2024-07-21
# Runtime: 126 ms, Memory: 17.4 MB
# Submission Id: 1327921615


class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)

        ans = ones = 0
        i = 0
        for i in range(n):
            if i and s[i] == s[i-1] == '0':
                continue
            if s[i] == '0':
                ans += ones
            else:
                ones += 1
        return ans