# 0077 - Combinations
# Date: 2023-08-01
# Runtime: 271 ms, Memory: 18.3 MB
# Submission Id: 1009482167


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, mask = [], 0
        
        def generate(curr, start, k):
            if k == 0:
                ans.append(curr[:])
                return
            for i in range(start, n):
                curr.append(i+1)
                generate(curr, i+1, k-1)
                curr.pop()
        
        generate([], 0, k)
        return ans