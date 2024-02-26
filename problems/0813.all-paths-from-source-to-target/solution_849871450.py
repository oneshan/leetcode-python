# 0813 - All Paths From Source to Target
# Date: 2022-11-26
# Runtime: 248 ms, Memory: 15.7 MB
# Submission Id: 849871450


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        start, end = 0, len(graph)-1
        
        stack = [(start, [start])]
        while stack:
            node, path = stack.pop()
            if node == end:
                ans.append(path)
            for neighbor in graph[node]:
                stack.append((neighbor, path+[neighbor]))
        return ans