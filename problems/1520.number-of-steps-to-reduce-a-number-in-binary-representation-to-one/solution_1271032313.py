# 1520 - Number of Steps to Reduce a Number in Binary Representation to One
# Date: 2024-05-29
# Runtime: 33 ms, Memory: 16.5 MB
# Submission Id: 1271032313


class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        ans = carry = 0
        for i in range(n-1, 0, -1):
            digit = int(s[i]) + carry
            if digit & 1:
                ans +=2
                carry = 1
            else:
                ans += 1

        if carry:
            ans += 1

        return ans