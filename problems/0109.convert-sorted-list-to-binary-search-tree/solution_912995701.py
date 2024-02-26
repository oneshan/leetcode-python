# 0109 - Convert Sorted List to Binary Search Tree
# Date: 2023-03-11
# Runtime: 123 ms, Memory: 17.8 MB
# Submission Id: 912995701


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        p1, p2 = dummy, head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        mid = p1.next
        p1.next = None
        root = TreeNode(mid.val)
        if head != mid:
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(mid.next)
        return root