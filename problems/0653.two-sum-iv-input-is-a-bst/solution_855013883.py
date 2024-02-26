# 0653 - Two Sum IV - Input is a BST
# Date: 2022-12-05
# Runtime: 161 ms, Memory: 16.4 MB
# Submission Id: 855013883


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class InorderIterator:
    def __init__(self, root, is_reverse=False):
        self.is_reverse = is_reverse
        self.stack = []
        self.populate_iterator(root)

    def populate_iterator(self, node):
        while node:
            self.stack.append(node)
            if self.is_reverse:
                node = node.right
            else:
                node = node.left

    def getNext(self):
        if not self.stack:
            return None
        node = self.stack.pop()
        if self.is_reverse:
            self.populate_iterator(node.left)
        else:
            self.populate_iterator(node.right)
        return node

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder_iter = InorderIterator(root, False)
        inorder_rev_iter = InorderIterator(root, True)
        
        left, right = inorder_iter.getNext(), inorder_rev_iter.getNext()
        while left and right and left.val < right.val:
            two_sum = left.val + right.val
            if two_sum == k:
                return True
            if two_sum < k:
                left = inorder_iter.getNext()
            else:
                right = inorder_rev_iter.getNext()
        return False
        