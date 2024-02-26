# 0077 - Combinations
# Date: 2022-10-13
# Runtime: 1127 ms, Memory: 16 MB
# Submission Id: 821608059


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, mask = [], 0
        
        def generate(curr, start, k):
            if k == 0:
                ans.append(curr)
                return
            for i in range(start, n):
                generate(curr+[i+1], i+1, k-1)
        
        generate([], 0, k)
        return ans