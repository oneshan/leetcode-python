# 0078 - Subsets
# Date: 2023-09-18
# Runtime: 48 ms, Memory: 16.4 MB
# Submission Id: 1052712542


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(1 << n):
            ans.append([nums[j] for j in range(n) if i & (1 << j)])
        return ans