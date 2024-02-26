# 0039 - Combination Sum
# Date: 2022-12-05
# Runtime: 102 ms, Memory: 14.1 MB
# Submission Id: 855083852


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()
        
        def dfs(path, curr_sum, start):
            if curr_sum == target:
                ans.append(path[:])
                return
            
            for i in range(start, n):
                new_sum = curr_sum + candidates[i]
                if new_sum > target:
                    break
                path.append(candidates[i])
                dfs(path, new_sum, i)
                path.pop()
        
        dfs([], 0, 0)
        return ans