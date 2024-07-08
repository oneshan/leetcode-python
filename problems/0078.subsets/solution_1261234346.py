# 0078 - Subsets
# Date: 2024-05-18
# Runtime: 36 ms, Memory: 16.7 MB
# Submission Id: 1261234346


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        ans = []
        for i in range((1 << n)):
            arr = [nums[j] for j in range(n) if (1 << j) & i]
            ans.append(arr)
        return ans