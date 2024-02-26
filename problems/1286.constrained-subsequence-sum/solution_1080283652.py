# 1286 - Constrained Subsequence Sum
# Date: 2023-10-21
# Runtime: 2219 ms, Memory: 30.3 MB
# Submission Id: 1080283652


from sortedcontainers import SortedList

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        window = SortedList([0])
        
        for i in range(n):
            dp[i] = nums[i] + window[-1]
            window.add(dp[i])
            if i >= k:
                window.remove(dp[i-k])
        return max(dp)