# 0040 - Combination Sum II
# Date: 2022-12-06
# Runtime: 86 ms, Memory: 13.9 MB
# Submission Id: 855097472


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()
        
        def dfs(arr, curr_sum, start):
            if curr_sum > target:
                return
            if curr_sum == target:
                ans.append(arr[:])
                return
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                arr.append(candidates[i])
                dfs(arr, curr_sum + candidates[i], i+1)
                arr.pop()
        
        dfs([], 0, 0)
        return ans