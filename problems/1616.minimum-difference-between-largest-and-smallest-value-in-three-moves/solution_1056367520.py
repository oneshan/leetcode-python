# 1616 - Minimum Difference Between Largest and Smallest Value in Three Moves
# Date: 2023-09-22
# Runtime: 307 ms, Memory: 27.5 MB
# Submission Id: 1056367520


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        
        nums.sort()
        ans = float('inf')
        for i in range(4):
            for j in range(1, 4-i+1):
                ans = min(ans, nums[-j] - nums[i])
        return ans