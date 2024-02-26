# 0216 - Combination Sum III
# Date: 2023-09-19
# Runtime: 35 ms, Memory: 16.1 MB
# Submission Id: 1053615651


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def backtrack(arr, curr_sum, start):
            if len(arr) == k and curr_sum == n:
                ans.append(arr[:])
                return
            if len(arr) > k:
                return
            for i in range(start, 10):
                if curr_sum + i <= n:
                    arr.append(i)
                    backtrack(arr, curr_sum + i, i+1)
                    arr.pop()
        
        backtrack([], 0, 1)
        return ans