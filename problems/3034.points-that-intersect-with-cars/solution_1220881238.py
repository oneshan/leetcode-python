# 3034 - Points That Intersect With Cars
# Date: 2024-04-02
# Runtime: 75 ms, Memory: 16.6 MB
# Submission Id: 1220881238


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        ans = right = 0
        for start, end in nums:
            ans += max(0, end - max(start-1, right))
            right = max(right, end)
        return ans