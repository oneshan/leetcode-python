# 0077 - Combinations
# Date: 2023-09-18
# Runtime: 893 ms, Memory: 64.9 MB
# Submission Id: 1052748305


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, mask = [], 0
        
        def backtrack(arr, start):
            if len(arr) == k:
                ans.append(arr[:])
                return
            for i in range(start, n+1):
                arr.append(i)
                backtrack(arr, i+1)
                arr.pop()
        
        backtrack([], 1)
        return ans