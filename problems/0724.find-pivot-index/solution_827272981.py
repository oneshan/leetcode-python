# 0724 - Find Pivot Index
# Date: 2022-10-21
# Runtime: 275 ms, Memory: 15.1 MB
# Submission Id: 827272981


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        if prefix_sum[-1] ==  prefix_sum[0]:
            return 0
        
        for i in range(1, n):
            if prefix_sum[i-1] == prefix_sum[-1] - prefix_sum[i]:
                return i
        return -1