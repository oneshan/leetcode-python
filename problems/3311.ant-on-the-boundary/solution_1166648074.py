# 3311 - Ant on the Boundary
# Date: 2024-02-05
# Runtime: 37 ms, Memory: 16.6 MB
# Submission Id: 1166648074


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = curr = 0
        for num in nums:
            curr += num
            if curr == 0:
                ans += 1
        return ans