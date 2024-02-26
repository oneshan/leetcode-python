# 0869 - Similar String Groups
# Date: 2023-04-28
# Runtime: 2009 ms, Memory: 16.5 MB
# Submission Id: 940952496


from collections import defaultdict, deque

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        ans = 0
        n = len(strs)
        seen = set()
        graph = defaultdict(list)

        def is_similar(s1, s2):
            return sum(c1 != c2 for c1, c2 in zip(s1, s2)) in (0, 2)
        
        for i in range(n):
            for j in range(i):
                if is_similar(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)
                
        for i in range(n):
            if i in seen:
                continue
            queue = deque([i])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            ans += 1
        return ans