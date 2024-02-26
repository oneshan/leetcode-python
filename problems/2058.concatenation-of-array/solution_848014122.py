# 2058 - Concatenation of Array
# Date: 2022-11-22
# Runtime: 187 ms, Memory: 14.1 MB
# Submission Id: 848014122


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (n*2)
        for i in range(n):
            ans[i] = ans[n+i] = nums[i]
        return ans