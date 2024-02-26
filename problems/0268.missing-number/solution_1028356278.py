# 0268 - Missing Number
# Date: 2023-08-22
# Runtime: 116 ms, Memory: 18.2 MB
# Submission Id: 1028356278


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for num in range(len(nums)+1):
            if num not in nums_set:
                return num