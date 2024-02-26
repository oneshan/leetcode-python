# 1101 - Parallel Courses
# Date: 2023-08-31
# Runtime: 261 ms, Memory: 20.1 MB
# Submission Id: 1036612261


from collections import defaultdict, deque

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        
        for _from, _to in relations:
            graph[_from].add(_to)
            in_degree[_to] += 1
        
        ans = count = 0
        queue = deque({i for i in range(1, n+1) if in_degree[i] == 0})
        while queue:
            ans += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                count += 1
                for next_course in graph[course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
        return ans if count == n else -1