# 0269 - Alien Dictionary
# Date: 2023-09-29
# Runtime: 43 ms, Memory: 16.3 MB
# Submission Id: 1062057414


from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        
        unique_chars = set()
        for word in words:
            unique_chars |= set(word)
        
        n = len(words)
        for i in range(1, n):
            word1, word2 = words[i-1], words[i]
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        in_degree[c2] += 1
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(word2) < len(word1): return ""
                            
        queue = deque([ch for ch in unique_chars if in_degree[ch] == 0])
        ans = []
        while queue:
            ch = queue.popleft()
            ans.append(ch)
            for neighbor in graph[ch]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(ans) < len(unique_chars):
            return ''
        return ''.join(ans)