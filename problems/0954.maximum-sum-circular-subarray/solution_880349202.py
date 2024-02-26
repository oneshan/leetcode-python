# 0954 - Maximum Sum Circular Subarray
# Date: 2023-01-18
# Runtime: 680 ms, Memory: 19.1 MB
# Submission Id: 880349202


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        
        ans1 = curr = float('-inf')
        for num in nums:
            curr = max(curr+num, num)
            ans1 = max(ans1, curr)
        
        # kadane-min - nums[1:]
        diff = curr = float('inf')
        for i in range(1, n):
            curr = min(curr+nums[i], nums[i])
            diff = min(diff, curr)
        ans2 = total - diff
        
        # kadane-min - nums[:-1]
        diff = curr = float('inf')
        for i in range(n-1):
            curr = min(curr+nums[i], nums[i])
            diff = min(diff, curr)
        ans3 = total - diff
        
        return max(ans1, ans2, ans3)