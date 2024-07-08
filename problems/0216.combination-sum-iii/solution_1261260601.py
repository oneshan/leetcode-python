# 0216 - Combination Sum III
# Date: 2024-05-18
# Runtime: 27 ms, Memory: 16.4 MB
# Submission Id: 1261260601


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(arr, i, curr_sum):
            if len(arr) == k:
                if curr_sum == n:
                    ans.append(arr[:])
                return
            
            for j in range(i, 10):
                if curr_sum + j > n:
                    break
                arr.append(j)
                backtrack(arr, j+1, curr_sum+j)
                arr.pop()

        backtrack([], 1, 0)
        return ans