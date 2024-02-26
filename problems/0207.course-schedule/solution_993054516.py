# 0207 - Course Schedule
# Date: 2023-07-13
# Runtime: 127 ms, Memory: 17.7 MB
# Submission Id: 993054516


from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)
            
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken_course = 0
        while queue:
            course = queue.popleft()
            taken_course += 1
            if taken_course == numCourses:
                return True
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        return False