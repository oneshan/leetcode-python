# 0623 - Add One Row to Tree
# Date: 2024-04-16
# Runtime: 43 ms, Memory: 17.8 MB
# Submission Id: 1233616578


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

        queue = deque([root])
        while depth:
            depth -= 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if depth == 1:
                    node.left = TreeNode(val, node.left, None)
                    node.right = TreeNode(val, None, node.right)
                    continue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root