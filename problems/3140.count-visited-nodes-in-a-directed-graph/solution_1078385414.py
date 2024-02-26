# 3140 - Count Visited Nodes in a Directed Graph
# Date: 2023-10-18
# Runtime: 1441 ms, Memory: 40.3 MB
# Submission Id: 1078385414


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ans = [0] * n
        
        for i in range(n):
            stack = []
            seen = {}
            
            j, count = i, 0
            while j not in seen and ans[j] == 0:
                stack.append(j)
                seen[j] = count
                count += 1
                j = edges[j]
            
            if j in seen:
                size = count - seen[j]
                for _ in range(size):
                    ans[stack.pop()] = size
            
            while stack:
                j = stack.pop()
                ans[j] = ans[edges[j]] + 1
        
        return ans