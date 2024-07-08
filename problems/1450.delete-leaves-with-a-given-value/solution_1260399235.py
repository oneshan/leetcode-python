# 1450 - Delete Leaves With a Given Value
# Date: 2024-05-17
# Runtime: 39 ms, Memory: 17.4 MB
# Submission Id: 1260399235


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [root]
        parents = {root: None}
        seen = set()

        while stack:
            node = stack.pop()
            
            if not node.left and not node.right:
                if node.val != target:
                    continue
                if not parents[node]:
                    return None
                parent = parents[node]
                if parent.left == node:
                    parent.left = None
                if parent.right == node:
                    parent.right = None
            elif node not in seen:
                stack.append(node)
                seen.add(node)
                if node.left:
                    parents[node.left] = node
                    stack.append(node.left)
                if node.right:
                    parents[node.right] = node
                    stack.append(node.right)
        
        return root