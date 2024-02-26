# 0305 - Number of Islands II
# Date: 2022-10-23
# Runtime: 1214 ms, Memory: 19.9 MB
# Submission Id: 828544354


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
        
    def find(self, x):
        if x == self.root[x]:
            return x
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
            self.rank[root_x] += 1
            self.root[root_y] = root_x
        return True
    
    
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        if not positions:
            return []
        
        uf = UnionFind(m*n)
        ans = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen = set()
        count = 0
        
        for x, y in positions:
            if (x, y) in seen:
                ans.append(count)
                continue
            loc_1 = (x * n + y)
            seen.add((x, y))
            count += 1
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) in seen:
                    loc_2 = new_x * n + new_y
                    if uf.union(loc_1, loc_2):
                        count -= 1
            ans.append(count)
        return ans