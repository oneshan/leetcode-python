# 1729 - Binary Search Tree Iterator II
# Date: 2023-10-01
# Runtime: 330 ms, Memory: 48.6 MB
# Submission Id: 1064006640


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.arr = []
        self.curr_ptr = -1
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.curr_ptr < len(self.arr) - 1
        

    def next(self) -> int:
        self.curr_ptr += 1
        if self.curr_ptr == len(self.arr):
            node = self.stack.pop()
            if node.right:
                curr = node.right
                while curr:
                    self.stack.append(curr)
                    curr = curr.left
            self.arr.append(node.val)
        return self.arr[self.curr_ptr]
        

    def hasPrev(self) -> bool:
        return self.curr_ptr > 0

    def prev(self) -> int:
        self.curr_ptr -= 1
        return self.arr[self.curr_ptr]
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()