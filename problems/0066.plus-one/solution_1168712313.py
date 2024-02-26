# 0066 - Plus One
# Date: 2024-02-07
# Runtime: 25 ms, Memory: 16.5 MB
# Submission Id: 1168712313


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        while n and carry:
            carry, digits[n-1] = divmod(digits[n-1] + carry, 10)
            n -= 1
        if carry:
            return [1] + digits
        return digits