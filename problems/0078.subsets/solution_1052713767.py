# 0078 - Subsets
# Date: 2023-09-18
# Runtime: 43 ms, Memory: 16.5 MB
# Submission Id: 1052713767


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        def backtrack(arr, i):
            if i > len(nums):
                return
            ans.append(arr[:])
            for j in range(i, n):
                arr.append(nums[j])
                backtrack(arr, j + 1)
                arr.pop()

        ans = []
        backtrack([], 0)
        return ans