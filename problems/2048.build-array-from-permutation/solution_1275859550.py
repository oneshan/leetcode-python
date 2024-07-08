# 2048 - Build Array from Permutation
# Date: 2024-06-03
# Runtime: 93 ms, Memory: 16.8 MB
# Submission Id: 1275859550


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]

        return ans