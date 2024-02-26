# 1787 - Sum of Absolute Differences in a Sorted Array
# Date: 2023-11-25
# Runtime: 767 ms, Memory: 31.7 MB
# Submission Id: 1105803348


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        
        ans = [0] * n
        for i in range(n):
            left_sum = prefix[i] - nums[i]
            right_sum = prefix[-1] - prefix[i]
            
            left_total = i * nums[i] - left_sum
            right_total = right_sum - (n-1-i) * nums[i]
            ans[i] = left_total + right_total

        return ans