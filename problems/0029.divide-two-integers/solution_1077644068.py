# 0029 - Divide Two Integers
# Date: 2023-10-17
# Runtime: 40 ms, Memory: 16.3 MB
# Submission Id: 1077644068


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        
        ans = 0
        while dividend >= divisor:
            k, curr = 1, divisor
            while dividend >= curr:
                dividend -= curr
                ans += k
                k <<= 1
                curr <<= 1

        return min(max(-2147483648, ans * sign), 2147483647)