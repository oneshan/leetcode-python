# 0547 - Number of Provinces
# Date: 2023-09-16
# Runtime: 204 ms, Memory: 17.6 MB
# Submission Id: 1050246056


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        
        def dfs(i):
            for j in range(n):
                if isConnected[i][j] and j not in seen:
                    seen.add(j)
                    dfs(j)
        
        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans