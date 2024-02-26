# 1007 - Numbers With Same Consecutive Differences
# Date: 2023-09-19
# Runtime: 45 ms, Memory: 16.5 MB
# Submission Id: 1053609811


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        
        def backtrack(num, idx):
            if idx == n:
                ans.append(num)
                return
                
            digit = num % 10
            for next_d in {digit+k, digit-k}:
                if 0 <= next_d < 10:
                    backtrack(num * 10 + next_d, idx+1)
        
        for i in range(1, 10):
            backtrack(i, 1)
        return ans