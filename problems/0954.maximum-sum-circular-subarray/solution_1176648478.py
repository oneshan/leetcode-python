# 0954 - Maximum Sum Circular Subarray
# Date: 2024-02-16
# Runtime: 445 ms, Memory: 21.9 MB
# Submission Id: 1176648478


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        ans1, curr = float('-inf'), 0
        for num in nums:
            curr = max(curr+num, num)
            ans1 = max(ans1, curr)
        
        diff, curr = float('inf'), 0
        for i in range(1, n):
            curr = min(curr+nums[i], nums[i])
            diff = min(diff, curr)
        ans2 = total - diff

        diff, curr = float('inf'), 0
        for i in range(n-1):
            curr = min(curr+nums[i], nums[i])
            diff = min(diff, curr)
        ans3 = total - diff

        return max(ans1, ans2, ans3)
