# 2206 - Detonate the Maximum Bombs
# Date: 2024-06-10
# Runtime: 358 ms, Memory: 16.8 MB
# Submission Id: 1283852078


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def get_dist(i, j):
            return ((bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2) ** 0.5

        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                dist = get_dist(i, j)
                if dist <= bombs[i][2]:
                    graph[i].append(j)
                if dist <= bombs[j][2]:
                    graph[j].append(i)

        def dfs(i):
            seen = {i}
            stack = [i]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor in seen:
                        continue
                    seen.add(neighbor)
                    stack.append(neighbor)
            return len(seen)

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans