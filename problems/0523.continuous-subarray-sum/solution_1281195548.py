# 0523 - Continuous Subarray Sum
# Date: 2024-06-08
# Runtime: 823 ms, Memory: 36.1 MB
# Submission Id: 1281195548


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        first_seen = {0: -1}
        curr = 0
        for i in range(n):
            curr = (curr + nums[i]) % k
            if curr in first_seen:
                if i - first_seen[curr] >= 2:
                    return True
            else:
                first_seen[curr] = i
        return False