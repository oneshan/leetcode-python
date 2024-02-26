# 0896 - Smallest Subtree with all the Deepest Nodes
# Date: 2023-10-28
# Runtime: 34 ms, Memory: 16.5 MB
# Submission Id: 1086050324


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def lcs(node, p, q):
            if not node or node == p or node == q:
                return node
            left = lcs(node.left, p, q)
            right = lcs(node.right, p, q)
            if left and right:
                return node
            return left or right
        
        queue = deque([root])
        while queue:
            leaves = []
            for _ in range(len(queue)):
                node = queue.popleft()
                leaves.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        ans = leaves[0]
        for i in range(1, len(leaves)):
            ans = lcs(root, ans, leaves[i])
        return ans