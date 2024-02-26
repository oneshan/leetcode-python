# 0485 - Max Consecutive Ones
# Date: 2022-07-14
# Runtime: 489 ms, Memory: 14.3 MB
# Submission Id: 746521409


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, prev_0 = 0, -1
        for idx in range(len(nums)):
            if nums[idx] == 0:
                prev_0 = idx
            ans = max(ans, idx-prev_0)
        return ans