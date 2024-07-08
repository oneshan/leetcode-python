# 0152 - Maximum Product Subarray
# Date: 2024-05-25
# Runtime: 77 ms, Memory: 17 MB
# Submission Id: 1267266586


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ans = float('-inf')
        curr_max = curr_min = 1
        for num in nums:
            t1, t2 = curr_max * num, curr_min * num
            curr_max = max(num, t1, t2)
            curr_min = min(num, t1, t2)
            ans = max(ans, curr_max)
        return ans