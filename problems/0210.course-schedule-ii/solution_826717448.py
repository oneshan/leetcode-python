# 0210 - Course Schedule II
# Date: 2022-10-21
# Runtime: 246 ms, Memory: 15.4 MB
# Submission Id: 826717448


from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for q, p in prerequisites:
            graph[p].append(q)
            in_degree[q] += 1
        
        ans = []
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        while queue:
            node = queue.popleft()
            ans.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return ans if len(ans) == numCourses else []