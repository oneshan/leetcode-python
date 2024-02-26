# 0869 - Similar String Groups
# Date: 2023-04-28
# Runtime: 1996 ms, Memory: 16.7 MB
# Submission Id: 940951948


from collections import defaultdict

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
            stack = [i]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            ans += 1
        return ans