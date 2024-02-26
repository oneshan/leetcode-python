# 1866 - Restore the Array From Adjacent Pairs
# Date: 2023-11-10
# Runtime: 875 ms, Memory: 64.8 MB
# Submission Id: 1095862724


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        
        root = None
        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break
        
        ans = []
        stack = [(None, root)]
        while stack:
            prev, node = stack.pop()
            ans.append(node)
            for neighbor in graph[node]:
                if neighbor != prev:
                    stack.append((node, neighbor))
        return ans