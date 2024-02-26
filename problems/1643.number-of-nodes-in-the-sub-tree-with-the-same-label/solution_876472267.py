# 1643 - Number of Nodes in the Sub-Tree With the Same Label
# Date: 2023-01-12
# Runtime: 3084 ms, Memory: 201.5 MB
# Submission Id: 876472267


from collections import Counter

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(set)
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)
        
        ans = [0] * n
        
        def traverse(node, parent):
            counter = Counter()
            counter[labels[node]] = 1
            for child in tree[node]:
                if child == parent:
                    continue
                counter += traverse(child, node) 
            ans[node] = counter[labels[node]]
            return counter
        
        traverse(0, -1)
        return ans
        
            