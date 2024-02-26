# 0368 - Largest Divisible Subset
# Date: 2024-02-09
# Runtime: 221 ms, Memory: 16.8 MB
# Submission Id: 1170243048


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        subset = [[num] for num in nums]
        
        for i in range(n):
            for j in range(i):
                if (nums[i] % nums[j]) == 0 and len(subset[i]) < len(subset[j]) + 1:
                    subset[i] = subset[j] + [nums[i]]
                    
        return max(subset, key=len)