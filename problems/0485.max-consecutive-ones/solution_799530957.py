# 0485 - Max Consecutive Ones
# Date: 2022-09-14
# Runtime: 715 ms, Memory: 14.4 MB
# Submission Id: 799530957


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = curr = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            ans = max(ans, curr)
        return ans