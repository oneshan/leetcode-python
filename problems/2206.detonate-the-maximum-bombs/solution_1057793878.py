# 2206 - Detonate the Maximum Bombs
# Date: 2023-09-24
# Runtime: 594 ms, Memory: 16.6 MB
# Submission Id: 1057793878


from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                dist = (bombs[i][0]-bombs[j][0]) ** 2 + (bombs[i][1]-bombs[j][1]) ** 2
                if dist <= bombs[i][2] ** 2:
                    graph[i].append(j)
                if dist <= bombs[j][2] ** 2:
                    graph[j].append(i)
         
        ans = 0
        for i in range(n):
            seen = {i}
            stack = [i]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            ans = max(ans, len(seen))
        return ans