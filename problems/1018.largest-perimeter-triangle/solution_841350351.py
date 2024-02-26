# 1018 - Largest Perimeter Triangle
# Date: 2022-11-11
# Runtime: 434 ms, Memory: 15.5 MB
# Submission Id: 841350351


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0