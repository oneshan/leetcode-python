# 2524 - Largest Positive Integer That Exists With Its Negative
# Date: 2024-05-02
# Runtime: 115 ms, Memory: 16.8 MB
# Submission Id: 1247040114


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] >= 0:
                break
            if nums[left] + nums[right] == 0:
                return nums[right]
            if nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1

        return -1