# 1257 - Rank Transform of a Matrix
# Date: 2023-10-26
# Runtime: 1425 ms, Memory: 63.8 MB
# Submission Id: 1084581639


class UnionFind:
    def __init__(self, graph):
        self.rank = {i: 0 for i in graph}
        self.root = {i: i for i in graph}
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:  # already merged
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
      
    @property
    def groups(self):
        res = defaultdict(list)
        for i in self.root:
            res[self.find(i)].append(i)
        return res.values()

    
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(matrix), len(matrix[0])
        ans = [[0] * len_c for _ in range(len_r)]
        rank = [0] * (len_r + len_c)
        
        graph = defaultdict(list)
        for r in range(len_r):
            for c in range(len_c):
                graph[matrix[r][c]].append((r, c))
                
        for num in sorted(graph):
            same_lst = []
            for r, c in graph[num]:
                same_lst.append(r)
                same_lst.append(len_r + c)

            dsu = UnionFind(same_lst)
            for r, c in graph[num]:
                dsu.union(r, len_r + c)
            
            for _group in dsu.groups:
                mx = max(rank[i] for i in _group)
                for i in _group:
                    rank[i] = mx + 1
            
            for r, c in graph[num]:
                ans[r][c] = rank[r]
                
        return ans