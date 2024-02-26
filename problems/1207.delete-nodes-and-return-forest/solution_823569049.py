# 1207 - Delete Nodes And Return Forest
# Date: 2022-10-16
# Runtime: 139 ms, Memory: 14.6 MB
# Submission Id: 823569049


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)
        prev = None
        
        queue = deque([(root, True)])
        while queue:
            node, is_root = queue.popleft()
            if node is None:
                continue

            if node.val not in to_delete and is_root:
                ans.append(node)
                is_root = False
            
            left, right = node.left, node.right
            if left:
                if left.val in to_delete:
                    node.left = None
                    queue.append((left.right, True))
                    queue.append((left.left, True))
                else:
                    queue.append((left, is_root))
            if right:
                if right.val in to_delete:
                    node.right = None
                    queue.append((right.right, True))
                    queue.append((right.left, True))
                else:
                    queue.append((right, is_root))

        return ans