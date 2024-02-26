# 1866 - Restore the Array From Adjacent Pairs
# Date: 2023-11-10
# Runtime: 1012 ms, Memory: 66.2 MB
# Submission Id: 1095860759


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        for a, b in adjacentPairs:
            in_degree[a] += 1
            in_degree[b] += 1
            graph[a].append(b)
            graph[b].append(a)
            
        corner_nums = [node for node in graph if in_degree[node] == 1]        
        ans = []
        
        stack = [corner_nums[0]]
        while stack:
            node = stack.pop()
            ans.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 1:
                    stack.append(neighbor)
        ans.append(corner_nums[1])
        return ans