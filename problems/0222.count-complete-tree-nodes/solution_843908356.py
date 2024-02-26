# 0222 - Count Complete Tree Nodes
# Date: 2022-11-15
# Runtime: 198 ms, Memory: 21.4 MB
# Submission Id: 843908356


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
           
        # Compute depth
        depth, node = 0, root
        while node.left:
            node = node.left
            depth += 1
                
        # Find the last node 
        full_count = (1 << depth) - 1
        left, right = 1, full_count
        while left <= right:
            mid = (left + right) // 2
            if self.is_exist(mid, full_count, root):
                left = mid + 1
            else:
                right = mid - 1
        
        return full_count + left
    
    def is_exist(self, idx, full_count, node):
        left, right = 0, full_count
        while left < right:
            mid = (left + right) // 2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return bool(node)