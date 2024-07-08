# 0269 - Alien Dictionary
# Date: 2024-05-26
# Runtime: 36 ms, Memory: 16.6 MB
# Submission Id: 1267675021


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        
        unique_chars = set()
        for word in words:
            unique_chars |= set(word)

        n = len(words)
        for i in range(n-1):
            for c1, c2 in zip(words[i], words[i+1]):
                if c1 != c2:
                    graph[c2].add(c1)
                    break
            else:
                if len(words[i]) > len(words[i+1]):
                    return ''
        
        visited = {}  # False: visited, True: current path
        ans = []
        
        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = True
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            visited[node] = False
            ans.append(node)
            return False
        
        for node in unique_chars:
            if dfs(node):
                return ''
        return ''.join(ans)