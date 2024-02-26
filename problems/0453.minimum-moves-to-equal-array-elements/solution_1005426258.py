# 0453 - Minimum Moves to Equal Array Elements
# Date: 2023-07-27
# Runtime: 255 ms, Memory: 18 MB
# Submission Id: 1005426258


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(1, n):
            ans += (nums[i] - nums[0])
        return ans