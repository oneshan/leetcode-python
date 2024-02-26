# 0893 - All Nodes Distance K in Binary Tree
# Date: 2023-09-16
# Runtime: 52 ms, Memory: 16.5 MB
# Submission Id: 1050657823


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
        
        seen = {target}
        queue = deque([target])
        for _ in range(k):
            if not queue:
                break
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in (node.left, node.right, parents.get(node)):
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)

        return [node.val for node in queue]