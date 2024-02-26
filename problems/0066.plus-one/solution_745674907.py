# 0066 - Plus One
# Date: 2022-07-13
# Runtime: 62 ms, Memory: 13.8 MB
# Submission Id: 745674907


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(len(digits)-1, -1, -1):
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
        return [1] + digits