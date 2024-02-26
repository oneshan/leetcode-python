# 3246 - Check if Bitwise OR Has Trailing Zeros
# Date: 2023-12-31
# Runtime: 90 ms, Memory: 17.4 MB
# Submission Id: 1132626825


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count = 0
        for num in nums:
            if num & 1 == 0:
                count += 1
        return count >= 2