# 0077 - Combinations
# Date: 2023-08-01
# Runtime: 272 ms, Memory: 18.3 MB
# Submission Id: 1009084490


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        
        def backtrack(idx, count, arr):
            if count == k:
                ans.append(arr[:])
                return
            
            for i in range(idx, n+1):
                arr.append(i)
                backtrack(i+1, count+1, arr)
                arr.pop()
        
        backtrack(1, 0, [])
        return ans