# 0046 - Permutations
# Date: 2024-02-28
# Runtime: 40 ms, Memory: 16.8 MB
# Submission Id: 1188287446


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        n = len(nums)
        def backtrack(mask, arr):
            if mask == (1 << n) - 1:
                self.ans.append(arr[:])
                return
            for i in range(n):
                if mask & (1 << i) == 0:
                    arr.append(nums[i])
                    backtrack(mask | (1 <<i), arr)
                    arr.pop()
        
        backtrack(0, [])
        return self.ans