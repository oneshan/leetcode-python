# 2678 - Design Graph With Shortest Path Calculator
# Date: 2024-06-09
# Runtime: 3559 ms, Memory: 19.5 MB
# Submission Id: 1282673876


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.matrix = [[float('inf')] * n for _ in range(n)]
        for start, end, cost in edges:
            self.matrix[start][end] = cost
        for i in range(n):
            self.matrix[i][i] = 0

        # calculate
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    self.matrix[j][k] = min(self.matrix[j][k], self.matrix[j][i] + self.matrix[i][k])

    def addEdge(self, edge: List[int]) -> None:
        start, end, cost = edge
        for j in range(self.n):
            for k in range(self.n):
                self.matrix[j][k] = min(self.matrix[j][k], self.matrix[j][start] + self.matrix[end][k] + cost)

    def shortestPath(self, node1: int, node2: int) -> int:
        if self.matrix[node1][node2] == float('inf'):
            return -1
        return self.matrix[node1][node2]

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)