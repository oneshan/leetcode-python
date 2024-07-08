# 0046 - Permutations
# Date: 2024-05-18
# Runtime: 42 ms, Memory: 16.7 MB
# Submission Id: 1261284890


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(i):
            if i == n:
                ans.append(nums[:])
                return
            
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return ans