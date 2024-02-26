# 3262 - Find Polygon With the Largest Perimeter
# Date: 2024-02-15
# Runtime: 502 ms, Memory: 31.5 MB
# Submission Id: 1175728174


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        total = 0
        ans = -1
        for num in nums:
            if total > num:
                ans = total + num
            total += num
        return ans