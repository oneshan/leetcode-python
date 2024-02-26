# 0869 - Similar String Groups
# Date: 2023-04-28
# Runtime: 2000 ms, Memory: 16.8 MB
# Submission Id: 940951391


from collections import defaultdict

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        ans = 0
        n = len(strs)
        seen = set()
        graph = defaultdict(list)

        def is_similar(s1, s2):
            return sum(c1 != c2 for c1, c2 in zip(s1, s2)) in (0, 2)
        
        def dfs(i):
            seen.add(i)
            for j in graph[i]:
                if j not in seen:
                    dfs(j)        

        for i in range(n):
            for j in range(i):
                if is_similar(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)
                
        for i in range(n):
            if i in seen:
                continue
            dfs(i)
            ans += 1
        return ans