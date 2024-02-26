# 0646 - Maximum Length of Pair Chain
# Date: 2023-08-26
# Runtime: 202 ms, Memory: 16.7 MB
# Submission Id: 1032213399


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        
        ans, curr_end = 0, -1001
        for a, b in pairs:
            if a > curr_end:
                ans += 1
                curr_end = b
        return ans