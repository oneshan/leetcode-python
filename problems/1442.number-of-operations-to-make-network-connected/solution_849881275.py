# 1442 - Number of Operations to Make Network Connected
# Date: 2022-11-26
# Runtime: 1360 ms, Memory: 34.4 MB
# Submission Id: 849881275


from collections import defaultdict

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
            
        if len(connections) < n-1:
            return -1
            
        seen = set()
        cluster = 0
        for i in range(n):
            if i in seen:
                continue
            cluster += 1
            seen.add(i)
            stack = [i]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
                        
        return cluster-1