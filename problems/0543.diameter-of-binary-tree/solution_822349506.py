# 0543 - Diameter of Binary Tree
# Date: 2022-10-14
# Runtime: 74 ms, Memory: 15.4 MB
# Submission Id: 822349506


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        table = {}
        stack = [(root, False)]
        while stack:
            node, seen = stack.pop()
            if seen:
                left = table.get(node.left, 0)
                right = table.get(node.right, 0)
                ans = max(ans, left+right)
                table[node] = max(left, right) + 1
            else:
                stack.append((node, True))
                if node.left: stack.append((node.left, False))
                if node.right: stack.append((node.right, False))
        return ans