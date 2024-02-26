# 1428 - Jump Game III
# Date: 2023-09-16
# Runtime: 273 ms, Memory: 80.5 MB
# Submission Id: 1050891043


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        
        seen = {start}
        
        def dfs(i):
            if arr[i] == 0:
                return True
            for j in (i + arr[i], i - arr[i]):
                if 0 <= j < n and j not in seen:
                    seen.add(j)
                    if dfs(j):
                        return True
            return False
        
        return dfs(start)