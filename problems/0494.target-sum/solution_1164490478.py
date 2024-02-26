# 0494 - Target Sum
# Date: 2024-02-03
# Runtime: 213 ms, Memory: 16.6 MB
# Submission Id: 1164490478


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)        
        if n == 1:
            return (nums[0] == target) + (nums[0] == -target)
        
        targets = defaultdict(int)
        half_n = n >> 1
            
        for mask in range((1 << half_n) - 1, -1, -1):
            ct = target
            for k in range(half_n):
                if mask & (1 << k):
                    ct += nums[k]
                else:
                    ct -= nums[k]
            targets[ct] += 1
        
        ans = 0
        for mask in range((1 << (n-half_n)) - 1, -1, -1):
            ct = 0
            for k in range(half_n, n):
                if mask & (1 << (k - half_n)):
                    ct -= nums[k]
                else:
                    ct += nums[k]
            ans += targets[ct]
        
        return ans