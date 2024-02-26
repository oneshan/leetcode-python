# 0152 - Maximum Product Subarray
# Date: 2022-10-26
# Runtime: 155 ms, Memory: 14.4 MB
# Submission Id: 830650999


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = curr_min = curr_max = nums[0]
        for i in range(1, len(nums)):
            n1, n2, n3 = nums[i], curr_min * nums[i], curr_max * nums[i]
            curr_min = min(n1, n2, n3)
            curr_max = max(n1, n2, n3)
            ans = max(ans, curr_max)
        return ans