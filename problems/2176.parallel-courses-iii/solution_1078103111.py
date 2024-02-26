# 2176 - Parallel Courses III
# Date: 2023-10-18
# Runtime: 1429 ms, Memory: 45.4 MB
# Submission Id: 1078103111


from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for prev_c, next_c in relations:
            graph[prev_c-1].append(next_c-1)
            in_degree[next_c-1] += 1
            
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        max_time = time[:]
        
        while queue:
            for _ in range(len(queue)):
                course = queue.popleft()
                for next_course in graph[course]:
                    max_time[next_course] = max(max_time[next_course], max_time[course] + time[next_course])
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
        return max(max_time)