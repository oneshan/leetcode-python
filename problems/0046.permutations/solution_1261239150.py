# 0046 - Permutations
# Date: 2024-05-18
# Runtime: 37 ms, Memory: 16.8 MB
# Submission Id: 1261239150


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(mask, arr):
            if len(arr) == n:
                ans.append(arr[:])
                return
            
            for i in range(n):
                if (1 << i) & mask == 0:
                    arr.append(nums[i])
                    backtrack(mask | (1 << i), arr)
                    arr.pop()

        backtrack(0, [])
        return ans