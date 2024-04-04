# 3034 - Points That Intersect With Cars
# Date: 2024-04-02
# Runtime: 81 ms, Memory: 16.6 MB
# Submission Id: 1220879165


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        ans = 0
        curr = [0, 0]
        for start, end in nums:
            if start > curr[1]:
                ans += curr[1] - curr[0] + 1
                curr = [start, end]
            else:
                curr[1] = max(curr[1], end)

        ans += curr[1] - curr[0]
        return ans