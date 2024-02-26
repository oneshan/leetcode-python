# 1986 - Largest Color Value in a Directed Graph
# Date: 2023-09-29
# Runtime: 2241 ms, Memory: 197.2 MB
# Submission Id: 1062184258


from collections import defaultdict, deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        if not edges:
            return 1
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        
        n = len(colors)
        dp = [[0] * 26 for _ in range(n)]        
        state = [0] * n  # WHITE 0, GRAY 1, BLACK 2
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if state[node]:
                return state[node] == 2
            state[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
                for i in range(26):
                    dp[node][i] = max(dp[node][i], dp[neighbor][i])
            
            curr_color = ord(colors[node])-ord('a')
            dp[node][curr_color] += 1
            ans = max(ans, dp[node][curr_color])
            state[node] = 2
            return True
        
        for i in range(n):
            if state[i] == 0:
                if not dfs(i):
                    return -1
        return ans