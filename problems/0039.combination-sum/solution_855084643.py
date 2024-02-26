# 0039 - Combination Sum
# Date: 2022-12-05
# Runtime: 64 ms, Memory: 13.9 MB
# Submission Id: 855084643


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        
        def dfs(path, curr_sum, start):
            if curr_sum > target:
                return
            if curr_sum == target:
                ans.append(path[:])
                return
            
            for i in range(start, n):
                path.append(candidates[i])
                dfs(path, curr_sum + candidates[i], i)
                path.pop()
        
        dfs([], 0, 0)
        return ans