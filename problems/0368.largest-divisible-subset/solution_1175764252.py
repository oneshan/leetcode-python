# 0368 - Largest Divisible Subset
# Date: 2024-02-15
# Runtime: 218 ms, Memory: 16.9 MB
# Submission Id: 1175764252


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        nums.sort()
        dp = [0] * n
        
        for i, num in enumerate(nums):
            count = 0
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    count = max(count, dp[j])
            dp[i] = count + 1

        curr_size, curr_idx = max([(val, idx) for idx, val in enumerate(dp)])
        
        ans = []
        for i in range(curr_idx, -1, -1):
            if curr_size == dp[i] and nums[curr_idx] % nums[i] == 0:
                ans.append(nums[i])
                curr_size, curr_idx = curr_size-1, i

        return ans[::-1]