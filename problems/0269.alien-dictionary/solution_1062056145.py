# 0269 - Alien Dictionary
# Date: 2023-09-29
# Runtime: 35 ms, Memory: 16.3 MB
# Submission Id: 1062056145


from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        
        unique_chars = set()
        for word in words:
            unique_chars |= set(word)
        
        n = len(words)
        for i in range(1, n):
            word1, word2 = words[i-1], words[i]
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    graph[c1].append(c2)
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(word2) < len(word1):
                    return ""
        
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
        return ''.join(ans[::-1])