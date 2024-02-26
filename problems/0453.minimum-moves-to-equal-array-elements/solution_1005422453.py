# 0453 - Minimum Moves to Equal Array Elements
# Date: 2023-07-27
# Runtime: 230 ms, Memory: 17.9 MB
# Submission Id: 1005422453


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        min_num = min(nums)
        for num in nums:
            ans += num - min_num
        return ans