# 0040 - Combination Sum II
# Date: 2024-05-18
# Runtime: 56 ms, Memory: 16.6 MB
# Submission Id: 1261246779


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []

        def backtrack(arr, i, curr_sum):
            if curr_sum == target:
                ans.append(arr[:])
                return
            
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if curr_sum + candidates[j] > target:
                    break
                arr.append(candidates[j])
                backtrack(arr, j+1, curr_sum + candidates[j])
                arr.pop()


        backtrack([], 0, 0)
        return ans