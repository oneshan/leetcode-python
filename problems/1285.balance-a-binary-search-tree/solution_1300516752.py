# 1285 - Balance a Binary Search Tree
# Date: 2024-06-26
# Runtime: 197 ms, Memory: 22.1 MB
# Submission Id: 1300516752


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        def build(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = ListNode(arr[mid])
            node.left = build(left, mid-1)
            node.right = build(mid+1, right)
            return node

        inorder(root)
        return build(0, len(arr)-1)