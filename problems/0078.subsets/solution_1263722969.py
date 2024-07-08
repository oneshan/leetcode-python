# 0078 - Subsets
# Date: 2024-05-21
# Runtime: 39 ms, Memory: 16.7 MB
# Submission Id: 1263722969


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(arr, i):
            ans.append(arr[:])
            for j in range(i, n):
                arr.append(nums[j])
                backtrack(arr, j+1)
                arr.pop()

        backtrack([], 0)
        return ans