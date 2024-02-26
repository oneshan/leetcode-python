# 0922 - Possible Bipartition
# Date: 2022-12-02
# Runtime: 969 ms, Memory: 19.9 MB
# Submission Id: 853408487


from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [0] * size
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
        return True
            
            
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
               
        uf = UnionFind(n+1)
        for node in range(1, n+1):
            for neighbor in graph[node]:
                if uf.find(node) == uf.find(neighbor):
                    return False
                uf.union(graph[node][0], neighbor)
        return True