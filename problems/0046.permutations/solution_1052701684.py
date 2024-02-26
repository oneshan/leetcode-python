# 0046 - Permutations
# Date: 2023-09-18
# Runtime: 40 ms, Memory: 16.3 MB
# Submission Id: 1052701684


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        end_mask = (1 << n) - 1
        ans = []
        
        def backtrack(arr, mask):
            if mask == end_mask:
                ans.append(arr[:])
                return
            for i in range(n):
                if mask & (1 << i):
                    continue
                arr.append(nums[i])
                backtrack(arr, mask | (1 << i))
                arr.pop()
        
        backtrack([], 0)
        return ans