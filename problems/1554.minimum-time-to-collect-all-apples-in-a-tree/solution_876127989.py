# 1554 - Minimum Time to Collect All Apples in a Tree
# Date: 2023-01-11
# Runtime: 797 ms, Memory: 65.5 MB
# Submission Id: 876127989


from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(set)
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)
            
        def traverse(node, parent):
            total = 0
            for child in tree[node]:
                if child == parent:
                    continue
                sub_total = traverse(child, node)
                if sub_total or hasApple[child]:
                    total += sub_total + 2
            return total
        
        return traverse(0, -1)