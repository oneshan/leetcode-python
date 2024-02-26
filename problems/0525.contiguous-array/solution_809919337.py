# 0525 - Contiguous Array
# Date: 2022-09-28
# Runtime: 2105 ms, Memory: 19.6 MB
# Submission Id: 809919337


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