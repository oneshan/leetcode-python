# 2678 - Design Graph With Shortest Path Calculator
# Date: 2023-11-11
# Runtime: 619 ms, Memory: 19.7 MB
# Submission Id: 1096281610


import heapq

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for _from, _to, _cost in edges:
            self.graph[_from].append((_to, _cost))

    def addEdge(self, edge: List[int]) -> None:
        _from, _to, _cost = edge 
        self.graph[_from].append((_to, _cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        seen = {node1: 0}
        while heap:
            curr_cost, node = heapq.heappop(heap)
            if node == node2:
                return curr_cost
            for neighbor, cost in self.graph[node]:
                if neighbor not in seen or seen[neighbor] > curr_cost + cost:
                    seen[neighbor] = curr_cost + cost
                    heapq.heappush(heap, (curr_cost + cost, neighbor))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)