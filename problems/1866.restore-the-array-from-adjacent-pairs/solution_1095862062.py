# 1866 - Restore the Array From Adjacent Pairs
# Date: 2023-11-10
# Runtime: 898 ms, Memory: 64.9 MB
# Submission Id: 1095862062


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        seen = defaultdict(int)
        for a, b in adjacentPairs:
            seen[a] += 1
            seen[b] += 1
            graph[a].append(b)
            graph[b].append(a)
            
        corner_nums = [node for node in seen if seen[node] == 1]        
        ans = []
        
        stack = [(None, corner_nums[0])]
        while stack:
            prev, node = stack.pop()
            ans.append(node)
            for neighbor in graph[node]:
                if neighbor != prev:
                    stack.append((node, neighbor))
        return ans