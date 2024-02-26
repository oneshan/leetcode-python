# 2213 - Find All People With Secret
# Date: 2024-02-24
# Runtime: 1586 ms, Memory: 66.7 MB
# Submission Id: 1184543194


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] > self.rank[ry]:
            self.root[ry] = rx
        elif self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            self.rank[rx] += 1
    
    def reset(self, x):
        self.root[x] = x


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        graph = defaultdict(list)
        for a, b, time in meetings:
            graph[a].append((time, b))
            graph[b].append((time, a))
        
        heap = []
        heapq.heappush(heap, (0, 0))
        heapq.heappush(heap, (0, firstPerson))

        seen = [False] * n
        while heap:
            time, person = heapq.heappop(heap)
            if seen[person]:
                continue
            seen[person] = True
            for next_time, neighbor in graph[person]:
                if not seen[neighbor] and next_time >= time:
                    heapq.heappush(heap, (next_time, neighbor))
        
        return [i for i in range(n) if seen[i]]