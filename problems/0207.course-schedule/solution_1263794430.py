# 0207 - Course Schedule
# Date: 2024-05-21
# Runtime: 89 ms, Memory: 18.5 MB
# Submission Id: 1263794430


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for _to, _from in prerequisites:
            graph[_from].append(_to)
            indegree[_to] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        return count == numCourses