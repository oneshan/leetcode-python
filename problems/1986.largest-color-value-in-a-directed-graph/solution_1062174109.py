# 1986 - Largest Color Value in a Directed Graph
# Date: 2023-09-29
# Runtime: 2106 ms, Memory: 84.3 MB
# Submission Id: 1062174109


from collections import defaultdict, deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        dp = [[0] * 26 for _ in range(n)]
        
        indegree = [0] * n
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1
        
        queue = deque([i for i in range(n) if indegree[i] == 0])
        
        ans = seen = 0
        while queue:
            node = queue.popleft()
            dp[node][ord(colors[node])-ord('a')] += 1
            ans = max(ans, max(dp[node]))
            seen += 1
            for neighbor in graph[node]:
                # update dp
                for i in range(26):
                    dp[neighbor][i] = max(dp[neighbor][i], dp[node][i])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            
        return ans if seen == n else -1