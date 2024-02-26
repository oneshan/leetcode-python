# 2342 - Minimum Average Difference
# Date: 2022-09-24
# Runtime: 2226 ms, Memory: 25 MB
# Submission Id: 807334860


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total = sum(nums) 
        left_sum = 0
        n = len(nums)
        ans_idx, min_avg = 0, total
        for i in range(n - 1):
            left_sum += nums[i] 
            avg_diff = abs((left_sum // (i+1)) - (total - left_sum) // (n-i-1))
            if avg_diff < min_avg:
                ans_idx, min_avg = i, avg_diff
        
        if total / n < min_avg:
            ans_idx = n-1
        return ans_idx