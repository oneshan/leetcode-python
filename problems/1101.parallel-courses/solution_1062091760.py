# 1101 - Parallel Courses
# Date: 2023-09-29
# Runtime: 267 ms, Memory: 19.7 MB
# Submission Id: 1062091760


from collections import defaultdict, deque

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(set)
        in_degree = [0] * (n+1)
        for a, b in relations:
            graph[a].add(b)
            in_degree[b] += 1
            
        queue = deque([i for i in range(1, n) if in_degree[i] == 0])
        taken = ans = 0
        while queue:
            for _ in range(len(queue)):
                course = queue.popleft()
                taken += 1
                for next_course in graph[course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
            ans += 1
        return ans if taken == n else -1