# 0547 - Number of Provinces
# Date: 2022-10-04
# Runtime: 582 ms, Memory: 14.9 MB
# Submission Id: 815035982


from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        ans = 0
        
        def dfs(p):
            for q in range(n):
                if isConnected[p][q] and q not in seen:
                    seen.add(q)
                    dfs(q)

        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)
                
        return ans