# 0525 - Contiguous Array
# Date: 2024-01-26
# Runtime: 627 ms, Memory: 22.3 MB
# Submission Id: 1157383227


#calculate prefix sum,
#find the subarrays that sum up to 0 (k=0)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = {0: -1}
        
        ans = curr_sum = 0
        for idx, num in enumerate(nums):
            curr_sum += 1 if num else -1
            if curr_sum in prefix_sum:
                ans = max(ans, idx - prefix_sum[curr_sum])
            else:
                prefix_sum[curr_sum] = idx
        return ans