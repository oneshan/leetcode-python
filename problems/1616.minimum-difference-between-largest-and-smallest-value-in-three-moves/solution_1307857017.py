# 1616 - Minimum Difference Between Largest and Smallest Value in Three Moves
# Date: 2024-07-03
# Runtime: 286 ms, Memory: 27.3 MB
# Submission Id: 1307857017


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0

        nums.sort()
        return min(
            nums[~0] - nums[3],
            nums[~1] - nums[2],
            nums[~2] - nums[1],
            nums[~3] - nums[0],
        )