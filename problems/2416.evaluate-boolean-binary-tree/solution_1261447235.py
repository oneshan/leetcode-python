# 2416 - Evaluate Boolean Binary Tree
# Date: 2024-05-19
# Runtime: 48 ms, Memory: 16.9 MB
# Submission Id: 1261447235


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        TRUE, FALSE, OR, AND = 1, 0, 2, 3

        stack = [root]
        res = []
        last_visited = None
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack[-1]
            if node.right and node.right != last_visited:
                node = node.right
                continue

            stack.pop()

            if not node.left and not node.right:
                res.append(node.val)
            else:
                a, b = res.pop(), res.pop()
                if node.val == OR:
                    res.append(a | b)
                else:
                    res.append(a & b)

            last_visited = node
            node = None

        return res[0]