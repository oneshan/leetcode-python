# 0893 - All Nodes Distance K in Binary Tree
# Date: 2023-07-11
# Runtime: 50 ms, Memory: 16.7 MB
# Submission Id: 991396655


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def add_parent(curr, parent):
            if curr:
                curr.parent = parent
                add_parent(curr.left, curr)
                add_parent(curr.right, curr)
        
        add_parent(root, None)
        
        ans = []
        seen = set()
        
        def recur(curr, dist):
            if not curr or curr in seen:
                return
            seen.add(curr)
            if dist == 0:
                ans.append(curr.val)
                return
            recur(curr.parent, dist-1)
            recur(curr.left, dist-1)
            recur(curr.right, dist-1)
            
        recur(target, k)
        return ans