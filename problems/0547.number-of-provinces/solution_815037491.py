# 0547 - Number of Provinces
# Date: 2022-10-04
# Runtime: 934 ms, Memory: 14.3 MB
# Submission Id: 815037491


from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        ans = 0
        
        stack = []
        for i in range(n):
            if i in seen:
                continue
            ans += 1
            stack.append(i)
            while stack:
                p = stack.pop()
                for q in range(n):
                    if isConnected[p][q] and q not in seen:
                        stack.append(q)
                seen.add(p)
                
        return ans