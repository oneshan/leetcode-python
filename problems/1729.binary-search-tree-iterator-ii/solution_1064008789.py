# 1729 - Binary Search Tree Iterator II
# Date: 2023-10-01
# Runtime: 323 ms, Memory: 48.3 MB
# Submission Id: 1064008789


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
        self.last_one = root

    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.last_one or self.curr_ptr < len(self.arr) - 1
        

    def next(self) -> int:
        self.curr_ptr += 1
        if self.curr_ptr == len(self.arr):
            curr = self.last_one
            while curr:
                self.stack.append(curr)
                curr = curr.left
            curr = self.stack.pop()
            self.last_one = curr.right
            self.arr.append(curr.val)
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