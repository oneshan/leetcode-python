# 1101 - Parallel Courses
# Date: 2024-06-11
# Runtime: 219 ms, Memory: 19.3 MB
# Submission Id: 1284006175


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n

        for prev, nxt in relations:
            graph[prev-1].append(nxt-1)
            indegree[nxt-1] += 1

        queue = deque([i for i in range(n) if indegree[i] == 0])
        count = 0
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                count += 1
                for next_course in graph[course]:
                    indegree[next_course] -= 1
                    if indegree[next_course] == 0:
                        queue.append(next_course)

        return ans if count == n else -1