# 2176 - Parallel Courses III
# Date: 2023-10-18
# Runtime: 1473 ms, Memory: 95.9 MB
# Submission Id: 1078106264


from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)        
        for prev_c, next_c in relations:
            graph[prev_c-1].append(next_c-1)

        @cache
        def dfs(i):
            if not graph[i]:
                return time[i]
            res = 0
            for neighbor in graph[i]:
                res = max(res, dfs(neighbor))
            return res + time[i]
        
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans