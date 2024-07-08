# 0173 - Binary Search Tree Iterator
# Date: 2024-06-09
# Runtime: 76 ms, Memory: 22.4 MB
# Submission Id: 1282582234


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.generator = self.inorder(root)
        self.curr = next(self.generator, None)

    def inorder(self, root):
        if not root:
            return
        yield from self.inorder(root.left)
        yield root.val
        yield from self.inorder(root.right)

    def next(self) -> int:
        val = self.curr
        self.curr = next(self.generator, None)
        return val

    def hasNext(self) -> bool:
        return self.curr is not None

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()