# 0501 - Find Mode in Binary Search Tree
# Date: 2023-11-01
# Runtime: 52 ms, Memory: 20.2 MB
# Submission Id: 1088806445


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
            
        inorder(root)
            
        curr_freq, max_freq, ans = 0, 0, []
        prev = None
        for num in arr:
            if num == prev:
                curr_freq += 1
            else:
                curr_freq, prev = 1, num
                
            if curr_freq > max_freq:
                ans = []
                max_freq = curr_freq
            if curr_freq == max_freq:
                ans.append(num)
        return ans