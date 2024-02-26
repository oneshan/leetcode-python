# 1421 - Find Numbers with Even Number of Digits
# Date: 2022-09-14
# Runtime: 133 ms, Memory: 14 MB
# Submission Id: 799533078


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            digit = 0
            while num:
                num //= 10
                digit += 1
            if digit & 1 == 0:
                ans += 1
        return ans