# 0217 - Contains Duplicate
# Date: 2022-11-03
# Runtime: 1158 ms, Memory: 26.3 MB
# Submission Id: 835898698


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False