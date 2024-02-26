# 0646 - Maximum Length of Pair Chain
# Date: 2023-08-26
# Runtime: 1668 ms, Memory: 16.9 MB
# Submission Id: 1032216244


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        
        @cache
        def recur(i):
            count = 1
            for j in range(i+1, n):
                if pairs[i][1] < pairs[j][0]:
                    count = max(count, 1 + recur(j))
            return count
        
        ans = 0
        for i in range(n):
            ans = max(ans, recur(i))
        return ans