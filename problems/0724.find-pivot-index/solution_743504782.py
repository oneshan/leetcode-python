# 0724 - Find Pivot Index
# Date: 2022-07-10
# Runtime: 328 ms, Memory: 15.3 MB
# Submission Id: 743504782


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx-1]
            
        if nums[-1] == nums[0]:
            return 0        
        for idx in range(1, len(nums)):
            if nums[idx-1] + nums[idx] == nums[-1]:
                return idx
        if len(nums) > 1 and nums[-2] == 0:
            return len(nums) -1
        return -1