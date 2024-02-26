# 0547 - Number of Provinces
# Date: 2023-09-16
# Runtime: 240 ms, Memory: 17.1 MB
# Submission Id: 1050249637


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()        
        ans = 0
        for node in range(n):
            if node in seen:
                continue
            ans += 1
            stack = [node]
            while stack:
                i = stack.pop()
                seen.add(i)
                for j in range(n):
                    if isConnected[i][j] and j not in seen:
                        stack.append(j)
        return ans