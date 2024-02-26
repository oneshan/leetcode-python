# 1616 - Minimum Difference Between Largest and Smallest Value in Three Moves
# Date: 2023-09-22
# Runtime: 305 ms, Memory: 27.7 MB
# Submission Id: 1056367954


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        
        nums.sort()
        ans = float('inf')
        for i in range(4):
            for j in range(4-i):
                ans = min(ans, nums[-j-1] - nums[i])
        return ans