# 0268 - Missing Number
# Date: 2022-09-26
# Runtime: 315 ms, Memory: 15.8 MB
# Submission Id: 809111778


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for num in range(len(nums)+1):
            if num not in nums_set:
                return num