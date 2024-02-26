# 0144 - Binary Tree Preorder Traversal
# Date: 2022-11-18
# Runtime: 55 ms, Memory: 13.8 MB
# Submission Id: 845739118


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, node = [], root
        while node:
            if not node.left:
                ans.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                    
                if predecessor.right:
                    predecessor.right = None
                    node = node.right
                else:
                    ans.append(node.val)
                    predecessor.right = node
                    node = node.left
        return ans