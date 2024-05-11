# 0414 - Third Maximum Number
# Date: 2024-05-10
# Runtime: 51 ms, Memory: 17.5 MB
# Submission Id: 1254454260


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = None
        for num in nums:
            if num in (max1, max2, max3):
                continue
            if max1 is None or max1 < num:
                max1, max2, max3 = num, max1, max2
            elif max2 is None or max2 < num:
                max2, max3 = num, max2
            elif max3 is None or max3 < num:
                max3 = num
        
        return max3 if max3 is not None else max1