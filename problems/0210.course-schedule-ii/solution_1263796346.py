# 0210 - Course Schedule II
# Date: 2024-05-21
# Runtime: 91 ms, Memory: 18.2 MB
# Submission Id: 1263796346


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for _to, _from in prerequisites:
            graph[_from].append(_to)
            indegree[_to] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        ans = []
        while queue:
            course = queue.popleft()
            ans.append(course)
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return ans if len(ans) == numCourses else []