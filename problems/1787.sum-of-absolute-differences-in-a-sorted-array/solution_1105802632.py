# 1787 - Sum of Absolute Differences in a Sorted Array
# Date: 2023-11-25
# Runtime: 734 ms, Memory: 31.2 MB
# Submission Id: 1105802632


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        left_sum = 0
        
        ans = [0] * n
        for i in range(n):
            right_sum = total - left_sum - nums[i]
            
            left_total = i * nums[i] - left_sum
            right_total = right_sum - (n-1-i) * nums[i]
            ans[i] = left_total + right_total
            left_sum += nums[i]
            
        return ans