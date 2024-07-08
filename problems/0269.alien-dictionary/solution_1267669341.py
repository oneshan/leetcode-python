# 0269 - Alien Dictionary
# Date: 2024-05-25
# Runtime: 30 ms, Memory: 16.6 MB
# Submission Id: 1267669341


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
        
        color = {ch: 0 for ch in unique_chars}  # 0 WHITE, 1 GRAY, 2 BLACK
        ans = []
        
        def dfs(node):
            if color[node]:
                return color[node] == 2
            color[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            color[node] = 2
            ans.append(node)
            return True
        
        for node in unique_chars:
            if not dfs(node):
                return ''
        return ''.join(ans)