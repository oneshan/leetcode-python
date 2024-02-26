# 0560 - Subarray Sum Equals K
# Date: 2022-09-27
# Runtime: 863 ms, Memory: 18.2 MB
# Submission Id: 809869985


from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        current_sum = 0
        for num in nums:
            current_sum += num
            ans += prefix_sum[current_sum-k]
            prefix_sum[current_sum] +=1
        return ans