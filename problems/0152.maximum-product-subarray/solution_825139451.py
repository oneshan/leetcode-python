# 0152 - Maximum Product Subarray
# Date: 2022-10-18
# Runtime: 84 ms, Memory: 14.4 MB
# Submission Id: 825139451


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = curr_min = curr_max = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            curr_min, curr_max = (
                min(num, curr_min * num, curr_max * num),
                max(num, curr_min * num, curr_max * num)
            )
            ans = max(ans, curr_max)
        return ans