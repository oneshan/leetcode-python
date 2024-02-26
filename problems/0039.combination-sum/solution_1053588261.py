# 0039 - Combination Sum
# Date: 2023-09-19
# Runtime: 47 ms, Memory: 16.2 MB
# Submission Id: 1053588261


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        
        def backtrack(arr, start, curr_sum):
            if curr_sum == target:
                ans.append(arr[:])
                return
            for i in range(start, n):
                if curr_sum + candidates[i] <= target:
                    arr.append(candidates[i])
                    backtrack(arr, i, curr_sum + candidates[i])
                    arr.pop()
                    
        backtrack([], 0, 0)
        return ans