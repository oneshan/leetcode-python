# 0643 - Maximum Average Subarray I
# Date: 2022-09-24
# Runtime: 3604 ms, Memory: 25.8 MB
# Submission Id: 806922924


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr += nums[i]
            
        max_sum = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            max_sum = max(max_sum, curr)
        
        return max_sum / k