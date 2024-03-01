# 0108 - Convert Sorted Array to Binary Search Tree
# Date: 2024-02-29
# Runtime: 53 ms, Memory: 17.8 MB
# Submission Id: 1189257178


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build(left, mid-1)
            node.right = build(mid+1, right)
            return node
        
        return build(0, len(nums)-1)