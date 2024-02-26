# 0216 - Combination Sum III
# Date: 2022-12-05
# Runtime: 60 ms, Memory: 13.9 MB
# Submission Id: 855092421


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def dfs(arr, curr_sum, count, start):
            if count == k and curr_sum == n:
                ans.append(arr[:])
                return
            if count == k or curr_sum > n:
                return
            
            for i in range(start, 10):
                arr.append(i)
                dfs(arr, curr_sum+i, count+1, i+1)
                arr.pop()
        
        dfs([], 0, 0, 1)
        return ans