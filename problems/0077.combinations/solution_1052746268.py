# 0077 - Combinations
# Date: 2023-09-18
# Runtime: 915 ms, Memory: 64.8 MB
# Submission Id: 1052746268


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, mask = [], 0
        
        def backtrack(arr, start):
            if len(arr) == k:
                ans.append(arr[:])
                return
            for i in range(start, n):
                arr.append(i+1)
                backtrack(arr, i+1)
                arr.pop()
        
        backtrack([], 0)
        return ans