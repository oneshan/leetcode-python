# 0547 - Number of Provinces
# Date: 2022-10-04
# Runtime: 480 ms, Memory: 14.3 MB
# Submission Id: 815033603


from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.seen = set()
        self.ans = 0
        for node in range(len(isConnected)):
            if node not in self.seen:
                self.ans += 1
                self.dfs(isConnected, node)
        return self.ans
    
    def dfs(self, isConnected, p):
        for q in range(len(isConnected)):
            if isConnected[p][q] and q not in self.seen:
                self.seen.add(q)
                self.dfs(isConnected, q)