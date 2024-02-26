# 0560 - Subarray Sum Equals K
# Date: 2022-08-27
# Runtime: 573 ms, Memory: 16.7 MB
# Submission Id: 784639630


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix_sum = {0: 1}
        
        current_sum = 0
        for num in nums:
            current_sum += num
            ans += prefix_sum.get(current_sum-k, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        return ans