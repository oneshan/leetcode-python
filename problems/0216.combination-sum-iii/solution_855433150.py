# 0216 - Combination Sum III
# Date: 2022-12-06
# Runtime: 49 ms, Memory: 13.8 MB
# Submission Id: 855433150


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtracking(arr, start, digits, curr_sum):
            if digits == k and curr_sum == n:
                ans.append(arr[:])
                return
            if curr_sum >= n or digits == k:
                return
            
            for i in range(start, 10):
                arr.append(i)
                backtracking(arr, i+1, digits+1, curr_sum+i)
                arr.pop()
        
        ans = []
        backtracking([], 1, 0, 0)
        return ans