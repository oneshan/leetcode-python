# 0560 - Subarray Sum Equals K
# Date: 2022-07-11
# Runtime: 676 ms, Memory: 16.5 MB
# Submission Id: 743520468


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = current_sum = 0
        table = {0: 1}
        for num in nums:
            current_sum += num
            ans += table.get(current_sum-k, 0)
            table[current_sum] = table.get(current_sum, 0) + 1
        return ans