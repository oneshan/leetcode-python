# 0039 - Combination Sum
# Date: 2024-05-18
# Runtime: 46 ms, Memory: 16.7 MB
# Submission Id: 1261241789


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []

        def backtrack(arr, i, curr_sum):
            if curr_sum == target:
                ans.append(arr[:])
                return
            for j in range(i, n):
                if curr_sum + candidates[j] > target:
                    break
                arr.append(candidates[j])
                backtrack(arr, j, curr_sum + candidates[j])
                arr.pop()

        backtrack([], 0, 0)
        return ans