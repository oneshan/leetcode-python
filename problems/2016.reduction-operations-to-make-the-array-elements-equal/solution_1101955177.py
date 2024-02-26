# 2016 - Reduction Operations to Make the Array Elements Equal
# Date: 2023-11-19
# Runtime: 809 ms, Memory: 23.9 MB
# Submission Id: 1101955177


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = 0
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                ans += i
        return ans