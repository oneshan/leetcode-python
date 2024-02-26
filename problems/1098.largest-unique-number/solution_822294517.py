# 1098 - Largest Unique Number
# Date: 2022-10-14
# Runtime: 70 ms, Memory: 14.2 MB
# Submission Id: 822294517


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        i = len(nums)-1
        while i >= 0:
            if i == 0 or nums[i] != nums[i-1]:
                return nums[i]
            # skip duplicate
            while i > 0 and nums[i] == nums[i-1]:
                i -= 1
            i -= 1
        return -1