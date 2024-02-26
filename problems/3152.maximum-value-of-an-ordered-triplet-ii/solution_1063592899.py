# 3152 - Maximum Value of an Ordered Triplet II
# Date: 2023-10-01
# Runtime: 884 ms, Memory: 28.7 MB
# Submission Id: 1063592899


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        
        max_diff = [0] * n
        curr_max = nums[0]
        for i in range(1, n-1):
            curr_max = max(curr_max, nums[i])
            max_diff[i] = max(max_diff[i-1], curr_max - nums[i])
        
        ans = 0
        for k in range(n-1, -1, -1):
            ans = max(ans, nums[k] * max_diff[k-1])

        return ans