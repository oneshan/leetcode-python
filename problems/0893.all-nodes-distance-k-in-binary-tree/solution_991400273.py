# 0893 - All Nodes Distance K in Binary Tree
# Date: 2023-07-11
# Runtime: 60 ms, Memory: 16.9 MB
# Submission Id: 991400273


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

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
        
        queue = deque([(target.val, 0)])
        while queue:
            curr, dist = queue.popleft()
            if dist == k:
                ans.append(curr)
                continue
            for neighbor in graph[curr]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append([neighbor, dist + 1])

        return ans