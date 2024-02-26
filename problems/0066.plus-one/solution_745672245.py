# 0066 - Plus One
# Date: 2022-07-13
# Runtime: 32 ms, Memory: 13.8 MB
# Submission Id: 745672245


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        for idx in range(len(digits)-1, -1, -1):
            carry, digits[idx] = divmod(digits[idx]+carry, 10)
            if not carry:
                break
             
        if carry:
            return [1] + digits
        return digits