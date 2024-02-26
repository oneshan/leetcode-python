# 0198 - House Robber
# Date: 2022-10-08
# Runtime: 64 ms, Memory: 13.9 MB
# Submission Id: 817356760


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_two = prev_one = 0
        for num in nums:
            prev_two, prev_one = prev_one, max(prev_two+num, prev_one)
        return prev_one