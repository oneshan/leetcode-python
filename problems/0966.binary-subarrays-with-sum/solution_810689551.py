# 0966 - Binary Subarrays With Sum
# Date: 2022-09-29
# Runtime: 589 ms, Memory: 17.9 MB
# Submission Id: 810689551


from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        ans = curr = 0
        for num in nums:
            curr += num
            ans += prefix_sum[curr-goal]
            prefix_sum[curr] += 1
        return ans