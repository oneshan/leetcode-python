# 0039 - Combination Sum
# Date: 2023-08-01
# Runtime: 57 ms, Memory: 16.3 MB
# Submission Id: 1009484485


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        
        def backtrack(arr, start, curr_sum):
            if curr_sum > target:
                return
            if curr_sum == target:
                ans.append(arr[:])
                return
            for i in range(start, n):
                arr.append(candidates[i])
                backtrack(arr, i, curr_sum + candidates[i])
                arr.pop()
        
        backtrack([], 0, 0)
        return ans