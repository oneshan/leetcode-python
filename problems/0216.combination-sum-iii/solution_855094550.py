# 0216 - Combination Sum III
# Date: 2022-12-05
# Runtime: 61 ms, Memory: 13.8 MB
# Submission Id: 855094550


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def dfs(mask, curr_sum, count, start):
            if count == k and curr_sum == n:
                ans.append([i for i in range(1, 10) if (1<<i) & mask])
                return
            if count == k or curr_sum > n:
                return
            
            for i in range(start, 10):
                dfs((1<<i) | mask, curr_sum+i, count+1, i+1)
        
        dfs(0, 0, 0, 1)
        return ans