# 0039 - Combination Sum
# Date: 2024-02-28
# Runtime: 56 ms, Memory: 16.7 MB
# Submission Id: 1188289125


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        self.ans = []

        def backtrack(idx, arr, curr_sum):
            if curr_sum == target:
                self.ans.append(arr[:])
                return
            for j in range(idx, n):
                if curr_sum + candidates[j] > target:
                    break
                arr.append(candidates[j])
                backtrack(j, arr, curr_sum + candidates[j])
                arr.pop()
        
        backtrack(0, [], 0)
        return self.ans