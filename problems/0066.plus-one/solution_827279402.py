# 0066 - Plus One
# Date: 2022-10-21
# Runtime: 58 ms, Memory: 13.8 MB
# Submission Id: 827279402


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        else:
            return [1] + digits