# 0077 - Combinations
# Date: 2024-02-28
# Runtime: 721 ms, Memory: 64.7 MB
# Submission Id: 1188286177


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []

        def backtrack(i, arr):
            if len(arr) == k:
                self.ans.append(arr[:])
                return
            for j in range(i, n+1):
                arr.append(j)
                backtrack(j+1, arr)
                arr.pop()
        
        backtrack(1, [])
        return self.ans