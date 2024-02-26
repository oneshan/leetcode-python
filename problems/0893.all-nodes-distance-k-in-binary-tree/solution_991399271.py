# 0893 - All Nodes Distance K in Binary Tree
# Date: 2023-07-11
# Runtime: 61 ms, Memory: 16.9 MB
# Submission Id: 991399271


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        
        def build_graph(curr, parent):
            if not curr:
                return
            if parent:
                graph[curr.val].append(parent.val)
                graph[parent.val].append(curr.val)
            build_graph(curr.left, curr)
            build_graph(curr.right, curr)
            
        build_graph(root, None)
        
        ans = []
        seen = {target.val}
        
        def recur(curr, dist):
            if dist == k:
                ans.append(curr)
                return
            
            for neighbor in graph[curr]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    recur(neighbor, dist + 1)
            
        recur(target.val, 0)
        return ans