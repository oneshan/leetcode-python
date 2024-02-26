# 1986 - Largest Color Value in a Directed Graph
# Date: 2023-04-09
# Runtime: 2731 ms, Memory: 81.9 MB
# Submission Id: 930546262


from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        count = [[0] * 26 for _ in range(n)]
        
        indegree = [0] * n
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1
        
        zero_indegree = set(i for i in range(n) if indegree[i] == 0)
        
        ans = seen = 0
        while zero_indegree:
            node = zero_indegree.pop()
            count[node][ord(colors[node])-ord('a')] += 1
            ans = max(ans, max(count[node]))
            seen += 1
            for neighbor in graph[node]:
                for i in range(26):
                    count[neighbor][i] = max(count[neighbor][i], count[node][i])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    zero_indegree.add(neighbor)
            
        return ans if seen == n else -1