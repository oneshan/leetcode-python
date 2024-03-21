# 1745 - Find Nearest Right Node in Binary Tree
# Date: 2024-03-20
# Runtime: 156 ms, Memory: 46.3 MB
# Submission Id: 1209249507


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        queue = deque([root])
        seen = False
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if seen:
                    return node
                if node == u:
                    seen = True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if seen:
                break
        return None