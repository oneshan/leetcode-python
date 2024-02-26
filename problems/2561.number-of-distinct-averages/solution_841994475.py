# 2561 - Number of Distinct Averages
# Date: 2022-11-12
# Runtime: 70 ms, Memory: 13.9 MB
# Submission Id: 841994475


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        diff = set()
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            diff.add(nums[right]+nums[left])
            left += 1
            right -= 1
        return len(diff)