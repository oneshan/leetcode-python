# 2048 - Build Array from Permutation
# Date: 2024-06-03
# Runtime: 109 ms, Memory: 16.7 MB
# Submission Id: 1275862770


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for idx, num in enumerate(nums):
            nums[idx] += n * (nums[num] % n)
        
        for idx, num in enumerate(nums):
            nums[idx] //= n

        return nums