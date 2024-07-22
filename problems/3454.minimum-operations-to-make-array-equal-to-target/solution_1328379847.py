# 3454 - Minimum Operations to Make Array Equal to Target
# Date: 2024-07-21
# Runtime: 736 ms, Memory: 30.4 MB
# Submission Id: 1328379847


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)

        ans = prev = 0
        for i in range(n):
            diff = target[i] - nums[i]
            ans += max(0, diff - prev)
            prev = diff

        return ans + max(-prev, 0)