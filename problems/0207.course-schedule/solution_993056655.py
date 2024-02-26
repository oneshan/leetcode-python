# 0207 - Course Schedule
# Date: 2023-07-13
# Runtime: 126 ms, Memory: 19.4 MB
# Submission Id: 993056655


from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        def check_cycle(curr, path):
            if curr in path:
                return True
            if curr in seen:
                return False
            path.add(curr)
            for child in graph[curr]:
                if check_cycle(child, path):
                    return True
            path.remove(curr)
            seen.add(curr)
            return False
        
        seen = set()
        for curr in range(numCourses):
            if check_cycle(curr, set()):
                return False
        return True