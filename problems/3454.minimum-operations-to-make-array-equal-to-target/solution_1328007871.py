# 3454 - Minimum Operations to Make Array Equal to Target
# Date: 2024-07-21
# Runtime: 776 ms, Memory: 30.5 MB
# Submission Id: 1328007871


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        diff = [n-t for n, t in zip(nums, target)]
        
        ans = abs(diff[0])
        for i in range(1, n):
            if diff[i] * diff[i-1] <= 0:
                ans += abs(diff[i])
            else:
                ans += max(abs(diff[i]) - abs(diff[i-1]), 0)
                
        return ans